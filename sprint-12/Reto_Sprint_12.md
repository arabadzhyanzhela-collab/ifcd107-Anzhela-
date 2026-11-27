# Reto Sprint 12 · Equipo 5 Green

- **Equipo:** 5 Green  
- **Integrantes:** Cristina, Miguel, Fran, Andri, Anzhela  
- **Contexto:** TurisData Canarias  
- **Fecha:** 24-25.11.2026  
- **scrum master** Miguel, técnico Anzela&nbsp;

## ¿Qué hemos hecho en este sprint?

En el Sprint 12 hemos trabajado paso a paso las técnicas de Procesamiento del Lenguaje Natural (NLP), recuperación de información con RAG, cómo funcionan por dentro los Transformers/LLMs y la detección de semanas raras de ocupación con autoencoders:

1. **NLP clásico y exploración de reseñas (`S12_03`):** limpiamos textos conservando tildes y la «ñ» sin borrar el «no», contamos las palabras más repetidas, entrenamos Regresión Logística y Naive Bayes para clasificar sentimientos y vimos por qué fallan las bolsas de palabras simples ante negaciones como «no es impecable».  
2. **Embeddings con LSA (`S12_04`):** comprimimos la matriz dispersa de TF-IDF a 12 dimensiones con `TruncatedSVD`, medimos similitud con el coseno (evitando que cada reseña salga igual a sí misma), comparamos la exactitud con 12 ejes frente a TF-IDF completo sin fuga de datos y creamos un buscador de reseñas por parecido.  
3. **Tokenización BPE, atención y temperatura (`S12_05`):** vimos cómo BPE junta pares frecuentes para formar trozos útiles y ahorrar tokens, calculamos atención con `Q`, `K` y `V` paso a paso, aplicamos máscara causal para no mirar al futuro y probamos cómo cambia la distribución al variar la temperatura (`T = 0.3` frente a `T = 2.5`).  
4. **Mini RAG con citas, evaluación y seguridad (`S12_06`):** troceamos la política del alojamiento en frases con su sección, recuperamos fragmentos parecidos, ampliamos consultas con sinónimos, añadimos un umbral para responder «No consta…» cuando no hay base, medimos alucinaciones y probamos un filtro básico contra *prompt injection*.  
5. **Autoencoder para detectar semanas atípicas (`S12_07`):** partimos las semanas de ocupación en orden temporal (80 % entrenamiento / 20 % prueba), escalamos solo con entrenamiento (`MinMaxScaler`), entrenamos un autoencoder `7 -> 4 -> 2 -> 4 -> 7` y fijamos un umbral (percentil 95\) para detectar anomalías inyectadas y semanas reales a revisar.

## Aprendizajes clave

- **Limpiar bien evita errores tontos:** quitar tildes o borrar «no» cambia el significado; ajustar escaladores, vectorizadores o LSA solo con entrenamiento evita colar información del test.  
- **Comprimir tiene un precio:** pasar a pocas dimensiones o usar pocos tokens ahorra espacio o coste, pero puede perder matices o unos puntos de acierto.  
- **Un asistente útil no debe inventar:** en RAG, poner un umbral y exigir citas ayuda a decir «No consta…» cuando falta información y a revisar qué dice el documento.  
- **Seguridad y ética siempre presentes:** no subir claves de API al código, no mandar datos personales de clientes sin permiso y revisar siempre los resultados antes de tomar decisiones.