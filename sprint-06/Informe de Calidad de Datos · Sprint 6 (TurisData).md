# Informe de Calidad de Datos · Sprint 6 (TurisData)

## 1. Resumen para el gerente
El fichero `reservas_sucio.csv` (1545 filas iniciales) presenta múltiples problemas de calidad derivados de exportaciones manuales y mezclas de sistemas (fechas en dos formatos, precios con comas decimales, duplicados exactos, valores negativos imposibles y categorías con múltiples variaciones de mayúsculas/minúsculas). Tras aplicar reglas de limpieza fijas, el dataset queda en 1500 filas válidas. **El defecto más grave detectado es la presencia de precios de noche nulos, negativos o extremos (hasta 9999 €)**, que afectan de manera directa a la estimación financiera y al comportamiento del modelo predictivo si no se tratan adecuadamente.

## 2. Tabla de inventario de defectos
| Nº | Defecto | Columna(s) | Filas afectadas | Cómo se detectó | Causa probable | Tratamiento aplicado | Por qué (y riesgo) |
|---|---|---|---|---|---|---|---|
| **1** | **Precios con formato de coma decimal** | `precio_noche` | 153 | `resumen_calidad` (tipo `object`) y `.str.contains(",")` | Exportación manual desde un Excel localizado en español | Reemplazo de `,` por `.` y conversión a tipo numérico | **Riesgo alto**: Si no se convierte, pandas lo lee como texto y los precios altos o decimales se pierden o dan error. |
| **2** | **Fechas de reserva con doble formato** | `fecha_reserva` | 1545 (totalidad) | Intentos de conversión fallidos con formato único (`%Y-%m-%d`) | Exportaciones combinadas de sistemas antiguos y nuevos | Doble parseo (`iso` y `espanol`) fusionado mediante `fillna` | Evita que registros válidos se conviertan en nulos por variaciones en el formato de fecha. |
| **3** | **Duplicados exactos** | *Todas* | 45 | `crudo.duplicated().sum()` | Clics repetidos al exportar o solapamiento de peticiones | Eliminación mediante `drop_duplicates()` | Sesgan el entrenamiento dando más peso artificial a ciertas reservas idénticas. |
| **4** | **Categorías de canal inconsistentes** | `canal` | ~100 | `.value_counts()` (ej. `Directo`, `directo`, `DIRECTO`) | Introducción manual o desalineación de APIs | Pasar a minúsculas, quitar espacios y unificar mediante estandarización | Unifica grupos dispersos para que el modelo no los trate como variables independientes. |
| **5** | **Países de origen mal codificados** | `pais_origen` | ~70 | `.value_counts()` (ej. `ES`, `España`, `es`, `UK`, `Reino Unido`) | Distintas fuentes de origen de los clientes | Mapeo mediante diccionario de equivalencias (`EQUIV_PAIS`) | Reduce la dimensionalidad artificial y agrupa correctamente la procedencia. |
| **6** | **Valores imposibles (precios negativos/altos)** | `precio_noche` | 8 | Filtro lógico (`precio <= 0` o `> 1000`) | Errores de tecleo o datos de prueba erróneos | Conversión a nulos con `.where()` dentro de rango razonable (20-1000 €) | **Riesgo crítico**: Distorsionan la media y confunden al algoritmo. Se pasan a nulo para imputarlos después de forma segura. |
| 7 | Noches de estancia negativas o cero | `noches` | 6 | Filtro lógico (`noches <= 0`) | Fallo en la selección del selector de fechas | Conversión a nulos mediante `.where()` (rango 1-60) | Evita estancias lógicamente imposibles sin descartar la fila completa. |
| 8 | Antelación negativa | `antelacion_dias` | 5 | Comparación de fechas (`fecha_llegada < fecha_reserva`) | Desincronización horaria o errores de registro | Recálculo directo: `(fecha_llegada - fecha_reserva).dt.days` | Restablece la lógica temporal restando las fechas reales. |

## 3. Antes y después de la limpieza
| Métrica / Columna | Antes | Después |
|---|---|---|
| **Filas totales** | 1545 | 1500 |
| **Duplicados exactos** | 45 | 0 |
| **Valores distintos de `canal`** | 9 | 4 |
| **Valores distintos de `pais_origen`** | 12 | 8 |
| **Nulos en `precio_noche`** | 84 | 90 (tras acotar imposibles) |

## 4. Pipeline y modelo de referencia (Baseline)
- **Preprocesamiento:** Se separaron las variables numéricas (`antelacion_dias`, `noches`, `adultos`, `ninos`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `mes_llegada`) y categóricas (`tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`). El *pipeline* aplica imputación por mediana (numérica) y moda (categórica), seguido de `StandardScaler` y `OneHotEncoder`.
- **Fuga evitada:** Todas las operaciones de imputación y escala se ajustaron **exclusivamente sobre el conjunto de entrenamiento (`X_train`)** a través de los pasos del pipeline en la validación cruzada, evitando cualquier tipo de fuga de datos (*data leakage*) desde el conjunto de test.
- **Resultado comparativo:** 
  > *«Nuestro modelo obtiene un AUC medio de 0,758 ± 0,025 frente a 0,500 del modelo tonto (DummyClassifier). Eso significa que ordena las reservas de forma robusta y supera con claridad al azar.»*

## 5. Preguntas para el cliente
1. ¿Un precio por noche de 0 € o inferior debe interpretarse como una tarifa cortesía/gratuita o como un error de registro?
2. ¿Por qué motivo existen desincronizaciones de hasta 3 días negativos en la antelación de las reservas?
3. ¿Cómo se gestionan habitualmente las reservas procedentes de agencias externas que llegan sin el país de origen especificado?

*(Acción mientras no responden: Imputación mediante la moda/mediana estadística y conservación de los registros para no perder volumen de datos).*

## 6. IA responsable (Análisis del país de origen)
- **Análisis de sesgo:** Los datos muestran diferencias en la tasa de cancelación según el origen (ej. Italia presenta una tasa de cancelación superior a la media frente a otros mercados). 
- **Riesgo:** Si el modelo utiliza de forma ciega el país de origen o imputa sistemáticamente los valores nulos con el país mayoritario (`ES`), puede reforzar sesgos o penalizar indirectamente a ciertos colectivos de clientes. Se recomienda supervisar métricas de equidad por grupo de origen en iteraciones futuras del modelo.

## 7. Cómo reproducirlo
- **Versiones:** Python 3.10+, Pandas 2.x, Scikit-learn 1.x.
- **Orden de ejecución:** Cargar librerías y datos con `dato("reservas_sucio.csv")` -> Definir y aplicar `limpiar_reservas(crudo)` -> Particionar con `train_test_split` (fijando `SEMILLA = 42`) -> Ejecutar el Pipeline de preprocesamiento y los modelos con validación cruzada estratificada.

---

## 8. Revisión con la rúbrica
| Criterio | Nivel (1-4) | Prueba comprobada | Lo primero que mejoraríamos |
|---|---|---|---|
| **1. Calidad de datos e inventario** | 4 | Tabla completa con 8 defectos, causas y tratamientos justificados. | Incluir validaciones automáticas de esquema al leer nuevos CSV. |
| **2. Limpieza y partición** | 4 | Función `limpiar_reservas` testeada sin alterar `crudo`; separación correcta de train/test. | Añadir logs detallados en tiempo de ejecución por cada bloque de limpieza. |
| **3. Pipeline y Baseline** | 4 | Pipeline robusto sin fugas; comparación formal con DummyClassifier mediante validación cruzada. | Probar algoritmos adicionales basados en árboles (Random Forest / LightGBM). |
| **4. Informe y Reproducibilidad** | 4 | Cuaderno verificado con *Reiniciar y ejecutar todo*; README y métricas documentadas. | Automatizar la generación de gráficos directamente en formato PDF/Markdown. |