# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

## 1\. Autoevaluación

**Nombre:** Cristina (5Green)

### Repaso rápido («Antes de entregar»)

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | Sí |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | Sí |
| ¿Imputación, escalado y codificación se ajustan solo con train? | A medias |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | Sí |
| ¿El README tiene instrucciones y versiones de librerías? | Sí |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | Sí |
| ¿Está subido a Git, con autoevaluación y coevaluación? | Sí |

### Puntúate de 1 a 4

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 3 | Se completó el pipeline aunque falta afinar el tuning. | Revisar los hiperparámetros del Random Forest. |
| Reproducibilidad | 4 | Ejecución limpia comprobada en Colab de principio a fin. | Verificar en entorno virtual local. |
| Análisis y comunicación al cliente | 4 | Lenguaje sencillo y conciso adaptado al cliente. | Agregar gráficos de dispersión. |
| IA responsable | 4 | Propuesta anti-discriminación por origen bien justificada. | Ampliar implicaciones legales GDPR. |

- **Lo que más me costó fue** imputar valores nulos categóricos sin perder filas útiles, **porque** algunas columnas tenían más de 100 nulos.  
- **He usado IA para** formatear el Markdown, **y lo que he comprobado a mano es** el rendimiento del modelo frente al baseline.

---

## 2\. Coevaluación

**Trabajo revisado de:** Equipo 1 (Verde) \| **Revisado por:** Cristina

### Checklist de Entregables

| Entregable | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| `informe_calidad.md` | ✔ | Muy detallado y limpio. |
| `reto_S06.ipynb` | ✔ | Se ejecuta perfectamente. |
| `README.md` | ✔ | Instrucciones completas. |

### Puntuación (1–4) de quien revisa

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Sin fugas de datos de train/test. |
| Reproducibilidad | 4 | Ejecución uniforme. |
| Análisis y comunicación al cliente | 4 | Excelente análisis exploratorio. |
| IA responsable | 4 | Muy bien argumentado. |

- **Lo que está muy bien:** La sección de IA responsable y la justificación de no utilizar el país como predictor discriminatorio.  
- **Lo que yo cambiaría, y por qué:** Incluiría una matriz de confusión visualizada con Seaborn en el cuaderno.