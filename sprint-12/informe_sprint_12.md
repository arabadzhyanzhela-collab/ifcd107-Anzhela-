# Informe del Sprint 12 · Equipo 5 Green

- **Equipo:** 5 Green  
- **Integrantes:** Cristina, Miguel, Fran, Andri, Anzhela  
- **Contexto:** TurisData Canarias  
- **Fecha:** 24-25.11.2026  
- **scrum master** Miguel, técnico Anzela&nbsp;

## 1\. Resumen sencillo de lo que probamos y qué salió

- **Clasificación de reseñas y temas (`S12_03`):** La regresión logística con TF-IDF (`0.992`) y Naive Bayes con bolsa de palabras (`0.989`) acertaron casi todo en el conjunto de prueba, aunque hay que tener en cuenta que las reseñas son sintéticas y bastante repetitivas. Cuando probamos frases con negación («La limpieza no es impecable»), el modelo falló porque mira palabras sueltas y no el orden. En los temas, `ruido` fue el que peor F1 obtuvo (`0.94`) porque la clave `ruid` también saltaba en frases como «La zona es ruidosa…».  
- **Embeddings con LSA y buscador (`S12_04`):** Comprimir de 105 columnas TF-IDF a 12 ejes de LSA recogió el `0.438` de la varianza y bajó la exactitud del clasificador de `0.995` a `0.891`, pero nos dio vectores compactos y densos. Al buscar «no me dejó dormir el ruido», el coseno devolvió reseñas relacionadas con ruido nocturno sin pedir palabras exactas.  
- **Tokenización BPE, atención y temperatura (`S12_05`):** En el mini corpus de 8 palabras (67 letras), 12 fusiones dejaron `22` tokens (`3.05x` de compresión), empezando por el par `('d', 'e')` con 4 apariciones. En la autoatención, al multiplicar por 2 la fila de «limpio» (`X2`), la atención de «hotel» hacia «limpio» subió de `0.446` a `0.932`. Con `T = 0.3` la probabilidad máxima fue `0.816` y con `T = 2.5` bajó a `0.302`: temperatura baja conviene cuando buscamos respuestas más estables y predecibles.  
- **Mini RAG y seguridad (`S12_06`):** Trocear la política en 25 frases y recuperar con TF-IDF \+ raíces de 5 letras mejoró al añadir expansión con sinónimos (pasando del `84%` al `95%` de acierto en primera posición). Al evaluar umbrales `[0.0, 0.1, 0.15, 0.3, 0.5]`, elegimos `0.1` porque es el menor umbral que logra el máximo de aciertos (`19/20`) con `0` alucinaciones. También vimos que un filtro de patrones bloquea los ataques de prueba, pero en un sistema real hace falta combinar capas y no fiarse de un solo filtro.  
- **Autoencoder y modelos generativos (`S12_07`):** Partiendo las 156 semanas en orden temporal (`124` de entrenamiento y `32` de prueba) y escalando solo con entrenamiento (`MinMaxScaler`), el umbral del percentil 95 quedó en `0.0154`. Detectó `3/3` anomalías inyectadas y marcó `3/32` semanas reales de prueba (encabezadas por `2025-07-13` con error `0.0284`).

## 2\. Nota de IA responsable (en palabras sencillas)

- **No inventar ni engañar al cliente:** En el asistente RAG es mejor decir «No consta en la política del alojamiento.» que inventar una norma o un horario falso.  
- **Datos personales y privacidad:** Nunca debemos mandar datos personales de huéspedes (nombres, DNI, correos, reservas) a servicios o APIs externas sin permiso ni anonimizar, y las claves de API jamás deben escribirse dentro del código ni subirse a GitHub.  
- **Revisión humana:** Tanto las alertas de semanas raras como los contenidos generados por IA (imágenes o textos) deben revisarse por una persona antes de tomar decisiones o publicar.

## 3\. Revisión rápida con la rúbrica

- **Corrección técnica:** Todos los ejercicios y mini-retos pasan sus comprobaciones (`✔`) y los cálculos siguen el orden temporal y la separación entrenamiento/prueba sin fuga de datos.  
- **Reproducibilidad:** Los cuadernos fijan semilla (`SEMILLA = 42`) y cargan los datos de forma automática desde la URL del curso.  
- **Comunicación sencilla y ética:** Explicamos qué significa cada resultado sin exagerarlo (por ejemplo, que una semana marcada merece revisarse, no que haya un fallo seguro) y recogemos las medidas básicas de seguridad y privacidad.