# Sprint 12 · 5 Green — NLP, embeddings, Transformers, RAG y generativos

- **Equipo:** 5 Green  
- **Miembros:** Cristina, Miguel, Fran, Andri y Anzhela  
- **Fecha:** 24-25.11.2026  
- **scrum master** Miguel, **técnico** Anzela&nbsp;

## Qué hemos hecho en este sprint

En el Sprint 12 hemos trabajado con textos y modelos generativos aplicados al caso de **TurisData** (reseñas de clientes, política del alojamiento y semanas de ocupación):

1. **NLP clásico (`S12_03`):** limpiamos reseñas sin borrar el «no», probamos bolsa de palabras y TF-IDF con regresión logística y Naive Bayes, vimos que la bolsa de palabras falla con negaciones como «no es impecable» y medimos temas con palabras clave (viendo que `ruido` tenía falsos positivos por coincidir con «ruidosa»).  
2. **Embeddings con LSA (`S12_04`):** pasamos de matrices TF-IDF largas y llenas de ceros a vectores densos de 12 dimensiones con `TruncatedSVD`, calculamos similitud por coseno y montamos un buscador de reseñas parecidas (por ejemplo, quejas por ruido nocturno).  
3. **Transformers y atención (`S12_05`):** vimos cómo funciona BPE para partir palabras en tokens y ahorrar espacio, calculamos `Q`, `K` y `V` paso a paso, aplicamos máscara causal para no mirar al futuro y probamos cómo cambia la distribución al subir o bajar la temperatura.  
4. **Mini RAG (`S12_06`):** troceamos la política del alojamiento, recuperamos fragmentos por similitud, añadimos expansión con sinónimos y regla de «No consta…», comprobamos cómo detectar alucinaciones, probamos ataques de *prompt injection* con un filtro sencillo y elegimos un umbral razonable (`0.1`).  
5. **Autoencoder y generativos (`S12_07`):** entrenamos un autoencoder pequeño para detectar semanas atípicas de ocupación por error de reconstrucción, marcamos las semanas de prueba a revisar y repasamos GAN, difusión y buenas prácticas de IA responsable.

## Archivos de esta carpeta

- `S12_03_nlp_clasico.ipynb` (ejecutado)  
- `S12_04_embeddings_lsa.ipynb` (ejecutado)  
- `S12_05_transformers_atencion.ipynb` (ejecutado)  
- `S12_06_mini_rag.ipynb` (ejecutado)  
- `S12_07_autoencoder_generativos.ipynb` (ejecutado)  
- `informe_sprint_12.md`  
- `autoevaluacion_y_coevaluacion.md`  
- `README.md`

## Cómo reproducirlo

1. Abre cualquiera de los cuadernos `.ipynb` en **Google Colab** (o súbelo desde tu ordenador).  
2. Ejecuta de arriba abajo comenzando por la celda **A1 · PREPARACIÓN** (descarga automáticamente los archivos necesarios desde la carpeta `datos/` del repositorio del curso).