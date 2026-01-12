# ¿Alcanza el salario? Análisis de MIPYMES en La Habana
Este proyecto nace de una duda existencial que compartimos todos en la calle: ¿Cuánto de nuestro salario se queda realmente en la tablilla de una MIPYME? A través de un análisis de datos real, hemos mapeado precios en 53 establecimientos de los municipios Plaza de la Revolución y Playa para contrastarlos con el salario medio estatal. No es solo un ejercicio de programación; es una fotografía de la supervivencia económica actual.

# Estructura del Proyecto
El proyecto está organizado de forma modular para separar los datos crudos de la lógica de análisis:

data/: Contiene el archivo general.json con los precios recolectados, salarios de referencia y la estructura de la canasta básica.

src/: Aquí reside icd_module.py, la libreria con las funciones

evidencia/: Fotos de las pizarras y tablillas de los establecimientos visitados (evidencia de campo).

main.ipynb: El Notebook principal donde se cruzan los datos y se cuenta la historia visualmente.

# Hallazgos Principales
El análisis se centra en varios puntos críticos:

Brecha de Precios: La diferencia abismal entre el lugar más barato y el más caro para un mismo producto (como el arroz).

Duelo de Supervivencia: Una comparativa de cuánto rinde el salario si basamos la dieta en Arroz vs. Espagueti.

El Impacto del "Carrito": ¿Qué porcentaje del sueldo se evapora al comprar solo una unidad de los 13 productos básicos?
