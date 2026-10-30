# Sprint 3 · Primer modelo en producción — 5Green

- **Reto:** «¿Puede un modelo avisar de las reservas con riesgo de cancelarse y que mi equipo lo consulte desde otra aplicación?»
- **Fechas:** 28-30/10/2026 · **Roles:** Scrum Master: Cristina · Responsable técnico: Andrii

## Qué se entrega (pendiente)

| Archivo | Contenido | Estado |
|---|---|---|
| `informe_mejor_modelo.md` | Todo en un documento (máx. 4 pág.): consulta SQL y variable objetivo, columnas «trampa» eliminadas (fuga de datos), comparación de modelos de AutoML, umbral de alerta justificado en euros | si |
| `evidencia_api.png` / `.md` | Captura o salida de una llamada real al modelo publicado como API | si |
| `informe_costes.md` | Recursos usados, coste estimado y prueba de que se borraron al terminar | si |

## Quién hizo qué

| Persona | GitHub | Aportación |
|---|---|---|
| Cristina | [@usuario] | Scrum Master. Columnas «trampa» y fuga de datos |
| Andrii| [@usuario] | Responsable técnico. Consulta SQL y variable objetivo |
| Fran | [@usuario] | Experimento de AutoML y publicación de la API |
| Miguel | [@usuario] | Umbral de alerta pensado en dinero |
| Anzhela | [@usuario] | Informe de recursos y costes, prueba del cierre |

## Cómo reproducirlo

No hay código. Los documentos se leen directamente en GitHub.

## Autoevaluación (0–4)

| Criterio | Nota | Justificación |
|---|---|---|
| Corrección técnica | 3 | Cada caso tiene modalidad, tipo de aprendizaje y familia de algoritmos; incluye un caso sin IA |
| Reproducibilidad | 3 | Documentos autocontenidos con fuentes (entrevista y datos del curso) |
| Análisis y comunicación al cliente | 3 | Recomendación clara del piloto con coste, plazo y próximos pasos |
| IA responsable | 3 | Semáforo por caso y checklist v1 con 4 riesgos, medidas y responsables |

## Coevaluación (1–4)

| Valorada / Valora | Anzhela | Cristina | Miguel | Fran | Andrii |
|---|---|---|---|---|---|
| Anzhela | 4 | | | | |
| Cristina | | 4 | | | |
| Miguel | | | 4 | | |
| Fran | | | | 4 | |
| Andrii | | | | | 4 |

## Retrospectiva

| Mantener | Mejorar | Probar |
|---|---|---|
| [El dinamismo y el compromiso individual con los plazos pactados desde el inicio] | [Leer con atención toda la información antes de empezar] | [Repartir las tareas al principio del sprint] |

## Declaración de uso de IA

Uso específico:
Optimización de la consulta SQL de porcentajes por canal.
Apoyo en el ajuste del tono redactado a lenguaje ejecutivo y estructuración de la tabla Markdown.
Comprobación manual efectuada:
Se ejecutó el script de SQL directamente en la base turisdata.db.
Todas las cifras numéricas, métricas (ROC-AUC 0,722), costes (100 € / 40 €) y respuestas JSON de la API coinciden exactamente con los resultados de las capturas de Colab.
