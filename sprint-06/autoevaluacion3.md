# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

## 1\. Autoevaluación

**Nombre:** Migel (5Green)

### Repaso rápido («Antes de entregar»)

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | Sí |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | Sí |
| ¿Imputación, escalado y codificación se ajustan solo con train? | Sí |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | Sí |
| ¿El README tiene instrucciones y versiones de librerías? | Sí |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | Sí |
| ¿Está subido a Git, con autoevaluación y coevaluación? | Sí |

### Puntúate de 1 a 4

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | Todos los tests y aserciones pasados con éxito. | Optimizar la velocidad del script. |
| Reproducibilidad | 4 | Fijada la semilla (SEMILLA \= 42\) en todo el código. | Incluir conda environment.yml. |
| Análisis y comunicación al cliente | 3 | Comunicación directa aunque concisa. | Desarrollar más las recomendaciones. |
| IA responsable | 4 | Cobertura amplia de los aspectos éticos del proyecto. | Añadir ejemplos de mitigación. |

- **Lo que más me costó fue** estructurar la tabla del informe de calidad con las 8 columnas requeridas, **porque** había que resumir causa, riesgo y solución técnica en poco espacio.  
- **He usado IA para** redactar explicaciones de negocio sencillas, **y lo que he comprobado a mano es** el resultado numérico de cada aserción.

---

## 2\. Coevaluación

**Trabajo revisado de:** Equipo 4 (Amarillo) \| **Revisado por:** Migel

### Checklist de Entregables

| Entregable | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| `informe_calidad.md` | ✔ | Bien estructurado. |
| `reto_S06.ipynb` | ✔ | Corre sin errores. |
| `README.md` | ✔ | Documentación suficiente. |

### Puntuación (1–4) de quien revisa

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Buen ajuste de clasificadores. |
| Reproducibilidad | 4 | Sin dependencias locales. |
| Análisis y comunicación al cliente | 3 | Podría incluir más gráficos explicativos. |
| IA responsable | 4 | Muy completo en sesgo geográfico. |

- **Lo que está muy bien:** La respuesta clara a las preguntas que se deben trasladar al cliente.  
- **Lo que yo cambiaría, y por qué:** Incluiría un diagrama de cajas adicional para comparar precios por tipo de habitación.