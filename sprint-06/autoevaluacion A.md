# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

## 1. Autoevaluación
**Nombre:** Anzhela (Scrum Master)

### Repaso rápido («Antes de entregar»)
| Pregunta | Mi respuesta |
|---|---|
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | Sí |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | Sí |
| ¿Imputación, escalado y codificación se ajustan solo con train? | Sí |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | Sí |
| ¿El README tiene instrucciones y versiones de librerías? | Sí |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | Sí |
| ¿Está subido a Git, con autoevaluación y coevaluación? | Sí |

### Puntúate de 1 a 4
| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
|---|---|---|---|
| Corrección técnica | 4 | Pipeline de preprocesamiento impecable sin data leakage. | Tuning fino de hiperparámetros. |
| Reproducibilidad | 4 | La Celda 1 prepara y descarga los datos directamente de GitHub. | Probar en un entorno fuera de Colab. |
| Análisis y comunicación al cliente | 4 | Informe detallado con 6+ defectos explicados para negocio. | Añadir resumen visual para la directiva. |
| IA responsable | 4 | Reflexión ética sólida sobre el impacto del país de origen. | Profundizar en métricas por subgrupos. |

- **Lo que más me costó fue** asegurar que no hubiera data leakage en el pipeline con `OneHotEncoder`, **porque** había que ajustar los transformadores únicamente con el conjunto de entrenamiento.
- **He usado IA para** generar borradores de código de inspección, **y lo que he comprobado a mano es** cada uno de los recuentos de nulos, duplicados y aserciones.

---

## 2. Coevaluación
**Trabajo revisado de:** Equipo 2 (Rojo) | **Revisado por:** Anzhela

### Checklist de Entregables
| Entregable | ¿Está y se entiende? | Comentario breve |
|---|---|---|
| `informe_calidad.md` | ✔ | Completo, bien estructurado y con causas probables. |
| `reto_S06.ipynb` | ✔ | Ejecución limpia sin errores de principio a fin. |
| `README.md` | ✔ | Instrucciones claras para reproducir el cuaderno. |

### Puntuación (1–4) de quien revisa
| Criterio | Puntuación | Comentario breve |
|---|---|---|
| Corrección técnica | 4 | Pipeline robusto y validación cruzada correcta. |
| Reproducibilidad | 4 | Descarga de datos automática en la primera celda. |
| Análisis y comunicación al cliente | 4 | Gráficos exploratorios y tabla de calidad muy claros. |
| IA responsable | 4 | Reflexión ética completa sobre el sesgo de origen. |

- **Lo que está muy bien:** La claridad en la identificación de formatos de fecha mezclados y la estructura del informe.
- **Lo que yo cambiaría, y por qué:** Explicaría de forma más explícita el tratamiento de duplicados en la introducción del cuaderno.