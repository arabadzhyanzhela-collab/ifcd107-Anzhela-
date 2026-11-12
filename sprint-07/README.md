# Sprint 7 · Precio y cancelación — 5Green

- **Reto:** «Precio y cancelación: predecir la tarifa recomendada y la probabilidad de cancelación en TurisData»  
- **Fechas:**  11-12 de noviembre 2026 · **Roles:** Scrum Master: Andrii · Responsable técnico: Cristina

## Qué se entrega

| Archivo | Contenido | Estado |
| :---- | :---- | :---- |
| `informe_modelado.md` | Informe completo redactado en lenguaje sencillo para el cliente con la comparación de modelos, tabla de tarifas, matriz de confusión, hipótesis de coste en euros, análisis de sensibilidad y apartado de IA responsable. | Completado |
| `reto_S07.ipynb` | Cuaderno principal de Python en Google Colab con todo el código de carga, EDA, preprocesado con pipelines, modelos de regresión y clasificación, optimización de umbrales y generación automática del JSON de cifras. | Completado |
| `autoevaluacion_andri.md` | Autoevaluación individual y coevaluación del miembro Andri. | Completado |
| `autoevaluacion_anzhela.md` | Autoevaluación individual y coevaluación de la miembro Anzhela. | Completado |
| `autoevaluacion_cristina.md` | Autoevaluación individual y coevaluación de la miembro Cristina. | Completado |
| `autoevaluacion_fran.md` | Autoevaluación individual y coevaluación del miembro Fran. | Completado |
| `autoevaluacion_miguel.md` | Autoevaluación individual y coevaluación del miembro Miguel. | Completado |

## Quién hizo qué

| Persona | GitHub | Aportación |
| :---- | :---- | :---- |
| Andri | \[@andri-5green\] | Scrum Master. Coordinación general, hipótesis de costes financieros (`COSTE_FN`, `COSTE_FP`), optimización del umbral en euros y redacción del README. |
| Cristina | \[@cristina-5green\] | Responsable técnico. Carga de datos, inspección de variables trampa para evitar *data leakage*, preprocesado inicial y matriz de correlaciones. |
| Anzhela | \[@anzhela-5green\] | Construcción del modelo de regresión lineal con interacciones para la tarifa recomendada y elaboración de la tabla de precios por temporada. |
| Fran | \[@fran-5green\] | Entrenamiento del modelo de clasificación (Regresión Logística vs k-NN), curvas AUC/AP y evaluación de matrices de confusión a distintos umbrales. |
| Miguel | \[@miguel-5green\] | Análisis de IA responsable, cuantificación de brechas de falsos positivos por canal/país y redacción de medidas éticas anti-discriminación. |

Cómo reproducirlo

1. Abrir el cuaderno `reto_S07.ipynb` en Google Colab.  
2. Asegurarse de mantener la primera celda de descarga automática para cargar `reservas_turisdata.csv` desde GitHub.  
3. En el menú superior de Colab, seleccionar **Entorno de ejecución → Reiniciar y ejecutar todo**.  
4. El cuaderno se ejecutará de principio a fin de forma lineal (en unos 2 minutos), generando los gráficos, las tablas de métricas y el archivo `cifras_informe.json`.

### Requisitos del entorno y librerías:

- **Python:** 3.10+  
- **pandas:** \>= 2.0.0  
- **numpy:** \>= 1.24.0  
- **scikit-learn:** \>= 1.2.0  
- **matplotlib / seaborn:** versiones estándar de Colab

## Autoevaluación (0–4)

| Criterio | Nota | Justificación |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Separación estricta de *train/test*, pipelines sin fuga de datos y optimización de umbrales por validación cruzada. |
| Reproducibilidad | 4 | Cuaderno 100 % lineal, con semilla `SEMILLA = 42` fijada y descarga de datos desde la nube. |
| Análisis y comunicación al cliente | 4 | Informe en lenguaje sencillo con tablas de tarifas claras y cuantificación del ahorro en euros (43.875 €). |
| IA responsable | 4 | Medición concreta del sesgo por canal (brecha de 41,4 puntos) y recomendaciones operativas sin discriminación. |

## Coevaluación (1–4)

| Valorada / Valora | Andri | Anzhela | Cristina | Fran | Miguel |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Andri | 4 |  |  |  |  |
| Anzhela |  | 4 |  |  |  |
| Cristina |  |  | 4 |  |  |
| Fran |  |  |  | 4 |  |
| Miguel |  |  |  |  | 4 |

## Retrospectiva

| Mantener | Mejorar | Probar |
| :---- | :---- | :---- |
| La comunicación fluida y constante en el grupo durante todo el desarrollo del sprint. | Coordinar con más antelación la integración final de los resultados en el cuaderno. | Probar herramientas de visualización interactiva para presentar las hipótesis de coste al cliente. |

## Declaración de uso de IA

**Uso específico:**

- Ayuda en la estructuración fluida de las explicaciones de negocio en el informe y en las hojas de autoevaluación.  
- Soporte para generar código limpio de gráficos con Seaborn y comprobaciones con `assert`.

**Comprobación manual efectuada:**

- Se ejecutó el cuaderno `reto_S07.ipynb` completo en un entorno limpio de Google Colab.  
- Todas las cifras de las tablas (error MAE de 6,76 €, AUC de 0,758, umbral óptimo de 0,32 y ahorros de 43.875 €) coinciden exactamente con los datos extraídos del archivo `cifras_informe.json`.