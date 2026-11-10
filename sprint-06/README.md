# Sprint 6 · Datos sucios, cliente impaciente — 5Green

* **Reto:** «¿Están los datos en condiciones de entrenar algo fiable sin incurrir en data leakage?»

* **Fechas:** 09-10/11/2026 · **Roles:** Scrum Master: Miguel · Responsable técnico: Andrii

## Qué se entrega (pendiente)

| Archivo | Contenido | Estado | 
| ----- | ----- | ----- | 
| `informe_calidad.md` | Reporte completo de calidad de datos, inventario de defectos, análisis de IA responsable y auditoría ético-técnica | Sí | 
| `reto_S06.ipynb` | Cuaderno Jupyter ejecutable de principio a fin con EDA, función `limpiar_reservas(df)`, `ColumnTransformer` (fit solo en train) y validación cruzada | Sí | 
| `autoevaluacion_*.md` | Archivos de autoevaluación y coevaluación individual de cada integrante del equipo | Sí | 



## Quién hizo qué

| Persona | GitHub | Aportación | 
| ----- | ----- | ----- | 
| Miguel | \[@usuario\] | Scrum Master. Evaluación comparativa del modelo Baseline (`DummyClassifier`) frente al clasificador y consolidación de métricas ($\text{media} \pm \text{desviación}$) | 
| Andrii | \[@usuario\] | Responsable técnico. Estructura del cuaderno `reto_S06.ipynb`, diseño del `Pipeline` con `ColumnTransformer` evitando data leakage y validación cruzada | 
| Cristina | \[@usuario\] | Desarrollo y documentación de la función modular `limpiar_reservas(df)` con docstrings y resumen de cambios | 
| Anzhela | \[@usuario\] | Redacción del inventario de defectos de calidad y análisis de IA Responsable en `informe_calidad.md` | 
| Fran | \[@usuario\] | Moderación del tablero Kanban, pruebas de integración del cuaderno y revisión integral de la Definition of Done (DoD) | 

## Cómo reproducirlo

1. Ubicar el archivo `reservas_sucio.csv` en la carpeta `data/` en la raíz del repositorio (`../data/reservas_sucio.csv`).

2. Abrir `sprint-06/reto_S06.ipynb` en Google Colab o Jupyter Notebook.

3. Ejecutar el cuaderno secuencialmente (**`Entorno de ejecución` -> `Reiniciar y ejecutar todo`**).

## Autoevaluación (0–4)

| Criterio | Nota | Justificación | 
| ----- | ----- | ----- | 
| Corrección técnica | 4 | Limpieza auditable y pipeline de preprocesamiento con `ColumnTransformer` ajustado exclusivamente sobre *train*, evitando cualquier tipo de *data leakage* | 
| Reproducibilidad | 4 | Cuaderno 100% reproducible y ejecutable de principio a fin sin dependencias externas complejas | 
| Análisis y comunicación al cliente | 3 | Clasificación clara de los defectos de calidad de los datos y reporte conciso para TurisData Canarias | 
| IA responsable | 4 | Evaluación de sesgos en variables sociodemográficas/origen y checklist ético integrado en la auditoría | 

## Coevaluación (1–4)

| Valorada / Valora | Anzhela | Cristina | Miguel | Fran | Andrii | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| Anzhela | 4 |  |  |  |  | 
| Cristina |  | 4 |  |  |  | 
| Miguel |  |  | 4 |  |  | 
| Fran |  |  |  | 4 |  | 
| Andrii |  |  |  |  | 4 | 

## Retrospectiva

| Mantener | Mejorar | Probar | 
| ----- | ----- | ----- | 
| Mantenimiento estricto del aislamiento entre datos de entrenamiento y prueba desde la partición inicial | Anticipar la detección de valores atípicos complejos antes del pipeline final | Automatizar la comprobación de tipos de datos en la carga inicial mediante tests unitarios | 

## Declaración de uso de IA

Uso específico:

* Generación de borradores de docstrings para la función de limpieza `limpiar_reservas(df)`.

* Apoyo en la optimización de sintaxis para `ColumnTransformer` en scikit-learn.

Comprobación manual efectuada:

* Se verificó manualmente que no existiera *data leakage* (que el ajuste de imputación y escalado se realizara únicamente tras el `train_test_split`).

* Todas las métricas del clasificador final frente al *DummyClassifier* coinciden exactamente con la salida obtenida tras ejecutar la validación cruzada en el cuaderno.
