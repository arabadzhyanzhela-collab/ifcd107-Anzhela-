# Autoevaluación y coevaluación · «¿Vale la pena la red?»

Equipo 5 Green · Se puntúa con la [rúbrica del reto](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S10), de 1 a 4\.

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

&nbsp;

---

## 1\. Autoevaluación

**Nombre:** Cristina

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
| Corrección técnica | 4 | Los cuatro ejercicios pasan, una sola partición, 3 variantes elegidas con validación y modelo guardado y recargado con el mismo resultado | Probar una validación cruzada estratificada (K-Fold) en lugar de una única partición |
| Reproducibilidad | 3 | El README explica cómo repetirlo; confirmado tras reiniciar y ejecutar todo en Colab que salen las cifras del informe | Comprobar que otra persona en otro entorno obtiene las mismas cifras |
| Análisis y comunicación al cliente | 3 | Responde a «¿vale la pena?» con media ± desviación, intervalo, coste y límites | Añadir cuándo cambiaría la recomendación con un coste real de *overbooking* |
| IA responsable | 3 | Tres riesgos concretos con medida; además medimos el AUC por país y canal y el efecto del umbral | Detectar y corregir la caída de AUC (0,643) en el grupo de país «otros» |

- **Lo que más me costó fue:** evitar la fuga de datos en el preprocesado y cuadrar los `assert` de los ejercicios 1 y 2, asegurando que el `StandardScaler` se ajustara solo con entrenamiento.  
- **Sobre el uso de IA:** he usado IA para generar el cuaderno completo y los borradores del informe y del README; he comprobado a mano la ejecución limpia en Colab y el paso de todos los `assert`.

---

## 2\. Coevaluación (durante la review)

**Trabajo revisado de (persona o equipo):** Miguel (Equipo 5 Green)  **Revisado por (yo):** Cristina

| Entregable (nómbralo) | ¿Está y se entiende? ✔ / ✘ / — | Comentario breve |
| :---- | :---- | :---- |
| Cuaderno `reto_vale_la_pena.ipynb` | ✔ | Muy limpio, estructurado y con todas las celdas de código ejecutadas correctamente. |
| Gráfica `curvas_aprendizaje.png` | ✔ | Se visualizan claramente las tres curvas y el diagnóstico de la parada temprana. |
| Modelo `mlp_final.keras` | ✔ | Se guarda y recarga sin errores, manteniendo las métricas intactas. |

&nbsp;

| Criterio | Puntuación (1–4) | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Implementación impecable de las variantes del MLP con L2 y validación correcta. |
| Reproducibilidad | 4 | El cuaderno corre de principio a fin en Colab sin requerir modificaciones manuales. |
| Análisis y comunicación al cliente | 3 | Explica muy bien los resultados técnicos adaptados al contexto de negocio. |
| IA responsable | 3 | Incorpora análisis riguroso de hiperparámetros y control de sobreajuste. |

- **Lo que está muy bien:** Me ha ayudado mucho cómo Miguel estructuró la función de diagnóstico de sobreajuste en el ejercicio 3, facilitando la interpretación visual de las pérdidas.  
- **Lo que yo cambiaría, y por qué:** Yo añadiría una breve nota textual en el gráfico de curvas detallando el número exacto de época en el que actuó el *early stopping* para cada semilla.