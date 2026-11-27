# Plan de datos y licencias · Equipo 5 Green (Corregido según dictamen S14)

**Proyecto:** ¿Hoja sana o enferma, y cuándo no fiarnos del modelo? Papas · **Responsable de datos:** Andri · **Última actualización:** 27/11/2026

> Sin licencia clara no hay proyecto (R2). Los datos sintéticos nunca se usan para la evaluación final.

## 1\. Inventario de fuentes y contraste de licencia (Corrección 2\)

| ID | Nombre del conjunto | Fuente / enlace original | Fecha de descarga | Licencia contrastada y condiciones | ¿Permite uso académico / redistribución? | Formato y tamaño | ¿Datos personales? |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| D1 | PlantVillage-Dataset (subconjunto patata: `Potato___healthy`, `Potato___Early_blight`, `Potato___Late_blight`) | Repositorio GitHub: [https\://github.com/spMohanty/PlantVillage-Dataset](https://github.com/spMohanty/PlantVillage-Dataset) (dataset original: Hughes & Salathé, 2015, *PlantVillage*) | 27/11/2026 (descargado en Colab vía `sprint-14/descargar_datos.py`) | **No es CC0 sin verificar:** en el repositorio `spMohanty/PlantVillage-Dataset` (y su archivo `LICENSE` / README en GitHub) se distribuye con fines de investigación y uso académico citando a los autores originales; antes de redistribuir copias completas se debe respetar la licencia del repositorio original. | **Sí para uso académico y entrenamiento** citando la fuente; **no subimos las imágenes crudas a nuestro GitHub** (solo `descargar_datos.py`). | Imágenes JPG/PNG RGB (`256×256` px; \~2.152 imágenes en las 3 clases de patata) | no |
| D2 | Respaldo sintético técnico (`SEMILLA = 42`) | Generado localmente en `01_eda.ipynb` / `02_baseline.ipynb` | 27/11/2026 | Uso interno exclusivo del equipo para depuración técnica en Colab | **Solo fallback técnico** si falla la conexión/descarga de GitHub en Colab. **Prohibido usarlo en evaluación final.** | Tabla sintética de prueba (1.200 filas simuladas) | no |

**Declaración explícita sobre datos sintéticos (Corrección 2):**

- El dataset real del proyecto es **`PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`)**, descargado mediante `sprint-14/descargar_datos.py`.  
- El generador sintético (`SEMILLA = 42`) **solo se activa si falla la descarga** de `PlantVillage-Dataset` en el entorno de Colab para comprobar que el código ejecuta sin errores, y **nunca se utiliza para entrenar ni evaluar el modelo candidato final**.

## 2\. Descripción de las variables (diccionario de datos)

| Variable | Tipo | Unidad | Significado | Valores válidos | % nulos |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `ruta_imagen` / `archivo` | texto (`str`) | — | Ruta relativa y nombre del fichero de imagen en `PlantVillage-Dataset` | `.jpg`, `.jpeg`, `.png` | 0 % |
| `clase_original` | categórica (`str`) | — | Nombre de la subcarpeta original de `PlantVillage-Dataset` | `Potato___healthy`, `Potato___Early_blight`, `Potato___Late_blight` | 0 % |
| `hoja_enferma` | binaria (`int`) | `0` / `1` | Variable objetivo tras reducción binaria (`0` \= `Potato___healthy`, `1` \= `Early_blight` o `Late_blight`) | `0` (sana) o `1` (enferma) | 0 % |
| `ancho` / `alto` | entero (`int`) | píxeles (`px`) | Dimensiones espaciales de la imagen | `> 0` (estándar `256 × 256`) | 0 % |
| `brillo` | numérico (`float`) | `[0, 1]` | Media normalizada de intensidad RGB | `[0.0, 1.0]` (`< 0.20` o `> 0.85` marca baja fiabilidad) | 0 % |
| `contraste` | numérico (`float`) | `[0, 1]` | Desviación estándar de intensidad RGB | `[0.0, 1.0]` (`< 0.10` marca baja fiabilidad) | 0 % |
| `verdor` | numérico (`float`) | `[-1, 1]` | Índice cromático `(G - R) / (G + R + 1e-5)` | `[-1.0, 1.0]` | 0 % |
| `md5` | texto (`str`) | hash hex | Huella MD5 del archivo de imagen para detectar duplicados exactos | Hash hexadecimal de 32 caracteres | 0 % |

## 3\. Informe de calidad del dato (resumen del EDA)

| Aspecto | Hallazgo | Acción tomada y justificación |
| :---- | :---- | :---- |
| Nulos | `0` valores nulos en metadatos; posibles ficheros corruptos al leer imágenes | Filtro `try/except` al abrir con `PIL.Image` en `01_eda.ipynb` para descartar imágenes dañadas |
| Duplicados | Posibles imágenes idénticas detectadas mediante hash `md5` del fichero | Eliminación de duplicados exactos por `md5` antes de particionar para evitar fuga entre `train` y `test` |
| Valores imposibles / outliers | Imágenes con contraste muy bajo (`< 0.10`) o brillo extremo (`< 0.20` o `> 0.85`) | No se eliminan de la evaluación; se etiquetan con la regla `no_fiable` para derivarlas a revisión humana |
| Formatos y tipos | Imágenes RGB uniformes (`256×256` px en `color/`) y variables numéricas derivadas | Conversión explícita a `.convert("RGB")` y validación de dimensiones |
| **Sesgo de muestreo** (¿quién o qué falta?) | `PlantVillage-Dataset` contiene hojas individuales fotografiadas sobre fondo liso en condiciones controladas; faltan variedades locales de papa canaria, hojas en planta entera y condiciones de campo (niebla, sombra, suelo volcánico) | Documentar el límite «no es papa canaria» en `ficha_proyecto.md` y `riesgos_eticos.md`, y realizar prueba fuera de `PlantVillage` en S16 |
| Desequilibrio de clases | Al agrupar `Early_blight` \+ `Late_blight` frente a `healthy`, la clase `enferma (1)` tiene mayor proporción (\~85 % en el subconjunto completo de patata si no se balancea) | Usar partición estratificada (`stratify=y`) y evaluar con `F1_macro` (que penaliza ignorar la clase minoritaria `sana`) |
| **Fuga de datos potencial** | El nombre de la carpeta y del archivo contiene la etiqueta (`healthy` / `blight`) | Excluir `clase_original` y `archivo` de las variables predictoras `X`; ajustar escalados/umbrales solo en `train` |

## 4\. Linaje del dato (de dónde viene y qué le hemos hecho)

```
1. Fuente original: https://github.com/spMohanty/PlantVillage-Dataset (raw/color/Potato___*)
   ↓
2. Descarga automática: sprint-14/descargar_datos.py (clona con --depth 1 y filtra únicamente las 3 carpetas Potato___*)
   ↓
3. Reducción de clases y limpieza (01_eda.ipynb): Potato___healthy -> 0 (sana); Potato___Early_blight y Potato___Late_blight -> 1 (enferma); eliminación de duplicados MD5 y cálculo de brillo, contraste y verdor
   ↓
4. Partición estratificada (02_baseline.ipynb, SEMILLA=42): 70% train / 15% val / 15% test (reservado sin tocar)
   ↓
5. Baseline y regla de fiabilidad (02_baseline.ipynb) -> Modelos CNN / Transfer Learning (S15) -> Evaluación final solo con datos reales (S16)
```

- **Script de descarga / preparación:** `sprint-14/descargar_datos.py`.  
- **Huella (hash) del conjunto final:** lista ordenada de hashes `md5` de las imágenes reales filtradas exportada en `01_eda.ipynb` / `S15_01`.  
- **¿Se puede recrear todo desde el README?** **Sí**, ejecutando `python sprint-14/descargar_datos.py` y los cuadernos `01_eda.ipynb` y `02_baseline.ipynb` con `requirements.txt` y `SEMILLA = 42`.

## 5\. Partición y umbral de éxito (Corrección 1 — idéntico a la Ficha)

- **Estrategia:** aleatoria estratificada (`train_test_split(..., stratify=y, random_state=42)`), deduplicando antes por `md5`.  
- **Tamaños:** entrenamiento **70 %** · validación **15 %** · test **15 %** (**el test real no se toca hasta tener un modelo candidato definitivo**, y entonces se evalúa una sola vez).  
- **Umbral de éxito acordado por las 5 personas antes del baseline:**  
  - **`F1_macro > 0.80` (80,0 %)** sobre el conjunto de validación y sobre el **test real**, superando en al menos **\+15 puntos porcentuales** al baseline (`DummyClassifier(strategy="most_frequent")` / regla de verdor).  
  - **Tasa de error `< 10 %`** en el subconjunto marcado como **fiable** tras aplicar el filtro de incertidumbre (`probabilidad fuera de [0.35, 0.65]`, `contraste >= 0.10` y `0.20 <= brillo <= 0.85`).

## 6\. Privacidad y RGPD

- **¿Hay datos personales?** **No.**  
- **¿Hay datos de menores, salud, biometría u otras categorías especiales?** **No** (imágenes de hojas vegetales).  
- **Datos que no subiremos al repositorio (en `.gitignore`):** `datos/`, `data/`, `PlantVillage-Dataset/`, `*.jpg`, `*.png`, `*.h5`, `*.pt`.

## 7\. Atribución y cita (pegar tal cual en la memoria)

> Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016). *Using Deep Learning for Image-Based Plant Disease Detection*. Frontiers in Plant Science, 7:1419. Repositorio de datos *PlantVillage-Dataset*: [https\://github.com/spMohanty/PlantVillage-Dataset](https://github.com/spMohanty/PlantVillage-Dataset) (consultado el 27/11/2026; sujeto a los términos y licencia indicados en el repositorio original).