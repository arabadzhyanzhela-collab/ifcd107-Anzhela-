# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

## 1\. Autoevaluación

**Nombre:** Fran (5Green)

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
| Corrección técnica | 4 | Preprocesado y modelo estructurados sin errores. | Añadir evaluación de falsos negativos. |
| Reproducibilidad | 4 | Cero dependencias locales; descarga vía URL. | Probar con distintas versiones de Pandas. |
| Análisis y comunicación al cliente | 4 | Redacción enfocada a negocio hotelero. | Incluir simulación de impacto en euros. |
| IA responsable | 4 | Justificación ética y técnica clara sobre sesgos. | Documentar riesgos de overfitting. |

- **Lo que más me costó fue** identificar los outliers de precio en la visualización, **porque** los valores extremos aplastaban la distribución inicial.  
- **He usado IA para** escribir el código de Seaborn, **y lo que he comprobado a mano es** que los rangos de precios razonables estuvieran entre 1 € y 1,000 €.

---

## 2\. Coevaluación

**Trabajo revisado de:** Equipo 6 (Naranja) \| **Revisado por:** Fran

### Checklist de Entregables

| Entregable | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| `informe_calidad.md` | ✔ | Excelente calidad y detalle. |
| `reto_S06.ipynb` | ✔ | Funciona correctamente. |
| `README.md` | ✔ | Claro y conciso. |

### Puntuación (1–4) de quien revisa

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Clasificador bien configurado. |
| Reproducibilidad | 4 | Cero fallos de importación. |
| Análisis y comunicación al cliente | 4 | Gráficos limpios y legibles. |
| IA responsable | 4 | Respuestas éticas completas. |

- **Lo que está muy bien:** Las gráficas exploratorias y la presentación limpia del cuaderno.  
- **Lo que yo cambiaría, y por qué:** Unificaría el esquema de colores de las gráficas para seguir una línea corporativa.