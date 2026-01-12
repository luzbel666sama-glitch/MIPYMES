import json

def cargar_datos(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta}")
        return None


def obtener_mipymes_por_municipio(datos, municipio_buscado):
    todos_los_municipios = datos.get('municipios', {})
    for nombre_real in todos_los_municipios.keys():
        if nombre_real.lower() == municipio_buscado.lower():
            return todos_los_municipios[nombre_real].get('mipymes', [])
    return []


def obtener_precios_de_producto(lista_mipymes, nombre_producto):
    precios = []
    for m in lista_mipymes:
        precio = m['precios'].get(nombre_producto)
        if precio is not None:
            precios.append(precio)
    return precios


def calcular_promedio(lista_precios):
    if not lista_precios:
        return 0
    return sum(lista_precios) / len(lista_precios)


def obtener_min_max(lista_precios):
    if not lista_precios:
        return 0, 0
    minimo = min(lista_precios)
    maximo = max(lista_precios)
    return minimo, maximo


def calcular_costo_canasta_basica(datos, municipio, lista_productos_interes):
    costo_total = 0
    mipymes = obtener_mipymes_por_municipio(datos, municipio)
    for producto in lista_productos_interes:
        precios = obtener_precios_de_producto(mipymes, producto)
        promedio = calcular_promedio(precios)
        costo_total += promedio
    return costo_total
