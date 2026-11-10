# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

## 1\. Autoevaluación

**Nombre:** Andrii (5Green)

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
| Corrección técnica | 4 | Modelado correcto y cross-val sin fugas. | Probar algoritmos adicionales. |
| Reproducibilidad | 4 | Ejecución lineal limpia comprobada en Colab. | Documentar más el entorno local. |
| Análisis y comunicación al cliente | 4 | Tabla de informe completa y fácil de interpretar. | Mejorar la estética de los gráficos. |
| IA responsable | 4 | Análisis detallado de sesgos por nacionalidad. | Incluir matriz de confusión ética. |

- **Lo que más me costó fue** identificar las incoherencias en las antelaciones por mezclar formatos de fechas, **porque** requería parsear individualmente ambas normas (ISO y DD/MM/YYYY).  
- **He usado IA para** crear funciones auxiliares de calidad, **y lo que he comprobado a mano es** el funcionamiento correcto de `value_counts()` en las columnas categóricas.

---

## 2\. Coevaluación

**Trabajo revisado de:** Equipo 3 (Azul) \| **Revisado por:** Andrii

### Checklist de Entregables

| Entregable | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| `informe_calidad.md` | ✔ | Tabla de calidad muy completa. |
| `reto_S06.ipynb` | ✔ | Se ejecuta correctamente. |
| `README.md` | ✔ | Todo detallado paso a paso. |

### Puntuación (1–4) de quien revisa

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Preprocesado impecable. |
| Reproducibilidad | 4 | 100 % reproducible. |
| Análisis y comunicación al cliente | 4 | Redacción muy profesional. |
| IA responsable | 4 | Justificación ética sólida. |

- **Lo que está muy bien:** El uso de Scikit-Learn Pipelines y la modularidad del código.  
- **Lo que yo cambiaría, y por qué:** Añadiría una frase aclaratoria sobre los nulos imputados en la columna de régimen.