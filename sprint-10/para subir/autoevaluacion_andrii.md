# Autoevaluación y coevaluación · «¿Vale la pena la red?»

Equipo 5 Green · Se puntúa con la [rúbrica del reto](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S10), de 1 a 4\.

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

---

## 1\. Autoevaluación

**Nombre:** Andri

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
| Corrección técnica | 4 | Los cuatro ejercicios pasan, una sola partición, 3 variantes elegidas con validación y modelo guardado y recargado con el mismo resultado | Incluir también los intervalos de confianza en la variante opcional de regresión |
| Reproducibilidad | 3 | El README explica cómo repetirlo; confirmado tras reiniciar y ejecutar todo en Colab que salen las cifras del informe | Comprobar que otra persona en otro entorno obtiene las mismas cifras |
| Análisis y comunicación al cliente | 3 | Responde a «¿vale la pena?» con media ± desviación, intervalo, coste y límites | Añadir cuándo cambiaría la recomendación con un coste real de *overbooking* |
| IA responsable | 3 | Tres riesgos concretos con medida; además medimos el AUC por país y canal y el efecto del umbral | Detectar que el modelo deja 183 cancelaciones sin detectar con el umbral por defecto (0,5) |

- **Lo que más me costó fue:** sintetizar todas las métricas técnicas y tiempos en un lenguaje claro para dirección en el informe comparativo.  
- **Sobre el uso de IA:** utilicé borradores generados por IA y verifiqué minuciosamente que cada número, tabla y conclusión de `informe_comparativo.md` coincidiera con las salidas reales del cuaderno.

---

## 2\. Coevaluación (durante la review)

**Trabajo revisado de (persona o equipo):** Anzhela (Equipo 5 Green)  **Revisado por (yo):** Andri

| Entregable (nómbralo) | ¿Está y se entiende? ✔ / ✘ / — | Comentario breve |
| :---- | :---- | :---- |
| `README.md` | ✔ | Completo, estructurado y detalla perfectamente los roles y dependencias. |
| Modelo guardado (`mlp_final.keras`) | ✔ | Verificada su correcta serialización y carga sin pérdida de precisión. |
| Análisis de extras (país y canal) | ✔ | Desglose impecable de métricas por segmentos de datos. |

&nbsp;

| Criterio | Puntuación (1–4) | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Excelente control en la exportación e importación del modelo de Keras. |
| Reproducibilidad | 4 | Documentación impecable en el README facilitando la ejecución en cualquier entorno. |
| Análisis y comunicación al cliente | 3 | Presentación clara de los metadatos y requerimientos técnicos del proyecto. |
| IA responsable | 4 | Gran rigor al identificar disparidades en subgrupos de clientes (país/canal). |

- **Lo que está muy bien:** Me ha ayudado mucho el trabajo de Anzhela organizando todos los metadatos del repositorio y asegurando que los archivos complementarios (`.keras` y `.png`) funcionen de manera integrada.  
- **Lo que yo cambiaría, y por qué:** Yo añadiría una pequeña nota en el README sobre los requisitos mínimos de versión de TensorFlow/Keras para evitar avisos de advertencia en entornos antiguos.