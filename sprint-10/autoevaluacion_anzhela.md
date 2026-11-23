# Autoevaluación y coevaluación · «¿Vale la pena la red?»

Equipo 5 Green · Se puntúa con la [rúbrica del reto](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S10), de 1 a 4\.

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

&nbsp;

---

## 1\. Autoevaluación

**Nombre:** Anzhela

**Repaso rápido** (Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | Sí: comprobado tras Reiniciar y ejecutar todo con semillas fijas (42 y 1, 2, 3\) |
| ¿La partición es única y la prueba se usa una sola vez? | Sí: una sola partición (semilla 42\) y la prueba solo se usa en la sección 6 |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | Sí: MLP y boosting, con AUC, AP, F1 y exactitud |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | Sí: sin sobreajuste claro |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | Sí: 3 semillas (0,748 ± 0,001 en validación) y bootstrap con intervalo \[−0,005, \+0,020\] |
| ¿El informe recomienda algo concreto, con coste y límites? | Sí: mantener el boosting |
| ¿Hay al menos dos riesgos de IA responsable específicos? | Sí: tres, con su medida |

**Puntúate de 1 a 4**:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | Los cuatro ejercicios pasan, una sola partición, 3 variantes elegidas con validación y modelo guardado y recargado con el mismo resultado | Añadir pruebas automáticas adicionales para verificar la recarga del archivo `.keras` |
| Reproducibilidad | 3 | El README explica cómo repetirlo; confirmado tras reiniciar y ejecutar todo en Colab que salen las cifras del informe | Comprobar que otra persona en otro entorno obtiene las mismas cifras |
| Análisis y comunicación al cliente | 3 | Responde a «¿vale la pena?» con media ± desviación, intervalo, coste y límites | Añadir cuándo cambiaría la recomendación con un coste real de *overbooking* |
| IA responsable | 3 | Tres riesgos concretos con medida; además medimos el AUC por país y canal y el efecto del umbral | Comprobar la disparidad de rendimiento entre Países Bajos (AUC 0,896) y Alemania (0,701) |

- **Lo que más me costó fue:** revisar los sesgos por país y canal en los extras y organizar toda la estructura de archivos para GitHub.  
- **Sobre el uso de IA:** empleé asistencia de IA para estructurar el README y comprobé a mano la ejecución completa en Colab y la correcta generación de los archivos `.png` y `.keras`.

---

## 2\. Coevaluación (durante la review)

**Trabajo revisado de (persona o equipo):** Cristina (Equipo 5 Green)  **Revisado por (yo):** Anzhela

| Entregable (nómbralo) | ¿Está y se entiende? ✔ / ✘ / — | Comentario breve |
| :---- | :---- | :---- |
| Cuaderno `reto_vale_la_pena.ipynb` (Ejercicios 1 y 2\) | ✔ | Funciones bien documentadas y con todos los tests superados. |
| Preprocesado y Escalado | ✔ | Uso correcto del `StandardScaler` ajustado únicamente en el conjunto de entrenamiento. |
| Estructura y legibilidad | ✔ | Excelente uso de marcas Markdown y celdas organizadas. |

&nbsp;

| Criterio | Punctuation (1–4) | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Excelente estructuración de las funciones iniciales y prevención de fugas de datos. |
| Reproducibilidad | 4 | Semillas fijadas correctamente y bloques de código listos para su ejecución automatizada. |
| Análisis y comunicación al cliente | 4 | Claridad en la exposición de las primeras etapas del pipeline de machine learning. |
| IA responsable | 3 | Buen cumplimiento de las buenas prácticas de partición de datos. |

- **Lo que está muy bien:** Me ha ayudado mucho el trabajo inicial de Cristina implementando el preprocesado de datos sin fugas y superando los `assert` de los primeros ejercicios.  
- **Lo que yo cambiaría, y por qué:** Yo añadiría comentarios adicionales en las líneas de transformación de variables categóricas para clarificar el manejo de codificación *One-Hot*.