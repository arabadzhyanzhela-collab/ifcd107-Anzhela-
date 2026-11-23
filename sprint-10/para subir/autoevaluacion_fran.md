# Autoevaluación y coevaluación · «¿Vale la pena la red?»

Equipo 5 Green · Se puntúa con la [rúbrica del reto](https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S10), de 1 a 4\.

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

&nbsp;

---

## 1\. Autoevaluación

**Nombre:** Fran

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
| Corrección técnica | 4 | Los cuatro ejercicios pasan, una sola partición, 3 variantes elegidas con validación y modelo guardado y recargado con el mismo resultado | Aumentar las repeticiones de bootstrap a 1.000 para estabilizar aún más los percentiles |
| Reproducibilidad | 3 | El README explica cómo repetirlo; confirmado tras reiniciar y ejecutar todo en Colab que salen las cifras del informe | Comprobar que otra persona en otro entorno obtiene las mismas cifras |
| Análisis y comunicación al cliente | 3 | Responde a «¿vale la pena?» con media ± desviación, intervalo, coste y límites | Añadir cuándo cambiaría la recomendación con un coste real de *overbooking* |
| IA responsable | 3 | Tres riesgos concretos con medida; además medimos el AUC por país y canal y el efecto del umbral | Mostrar cómo con umbral 0,3 se disparan las falsas alarmas a 303 generando riesgo de *overbooking* |

- **Lo que más me costó fue:** entender la interpretación estadística del intervalo bootstrap en el ejercicio 4, ya que una diferencia aparente de \+0,007 requería comprobar si cruzaba el cero.  
- **Sobre o uso de IA:** generamos la base con IA y comprobé a mano el cálculo del intervalo al 95 %, los tiempos de entrenamiento y el veredicto final.

---

## 2\. Coevaluación (durante la review)

**Trabajo revisado de (persona o equipo):** Andri (Equipo 5 Green)  **Revisado por (yo):** Fran

| Entregable (nómbralo) | ¿Está y se entiende? ✔ / ✘ / — | Comentario breve |
| :---- | :---- | :---- |
| Informe comparativo (`informe_comparativo.md`) | ✔ | Redacción fluida, estructurada y muy clara para cualquier perfil directivo. |
| Coherencia de métricas | ✔ | Todos los valores de AUC, AP y tiempos coinciden exactamente con el cuaderno. |
| Análisis de riesgos e IA responsable | ✔ | Se abordan de forma crítica los sesgos por país y canal. |

&nbsp;

| Criterio | Puntuación (1–4) | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Rigor absoluto en la validación cruzada de datos y métricas reportadas. |
| Reproducibilidad | 4 | Instrucciones claras y trazabilidad total con el cuaderno ejecutado. |
| Análisis y comunicación al cliente | 4 | Excelente síntesis respondiendo directamente a la pregunta de negocio ("¿vale la pena?"). |
| IA responsable | 4 | Muy buen desglose de los riesgos operacionales (umbral de decisión y costes de overbooking). |

- **Lo que está muy bien:** Me ha ayudado mucho cómo Andri estructuró la sección de IA responsable desglosando los impactos del umbral de clasificación sobre los falsos positivos.  
- **Lo que yo cambiaría, y por qué:** Yo añadiría una pequeña tabla resumen de los costes estimados por cada error de clasificación para redondear el apartado económico.