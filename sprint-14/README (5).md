# Proyecto Final · Monitoreo de la Salud de las Papas Canarias · Equipo 5 Green

- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri, Anzhela)
- **Proyecto:** Monitoreo de la salud de las **papas canarias** — *«¿Hoja sana o enferma, y cuándo no fiarnos del modelo?»*
- **Base de datos de partida:** `PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`)
- **Carpeta del Sprint 14:** https://github.com/cCoolBoox/IFCD107-alumnado/tree/main/sprints/S14

## Cómo ejecutar el Sprint 14
1. Abrir `sprint-14/01_eda.ipynb` en Google Colab.
2. Si queréis usar las imágenes de `PlantVillage-Dataset`, clonad `https://github.com/spMohanty/PlantVillage-Dataset.git` en `data/PlantVillage-Dataset`; si aún no está clonado, el cuaderno usa un respaldo sintético reproducible (`SEMILLA = 42`) para papas canarias.
3. Ejecutar `sprint-14/01_eda.ipynb` de arriba abajo para revisar calidad, clases (`sana` / `enferma`) y contraste.
4. Ejecutar `sprint-14/02_baseline.ipynb` de arriba abajo para ver la partición estratificada, el baseline (`F1_macro` y `accuracy`) y la regla de «cuándo no fiarse».
5. Revisar los documentos y hojas individuales de autoevaluación/coevaluación en `sprint-14/`.

## Uso de IA en este sprint
- **Qué pedimos a la IA:** borradores de estructura documental, celdas de exploración/baseline con `SEMILLA = 42` y ejemplos de reglas de confianza para hojas de papa.
- **Qué comprobamos a mano:** revisamos el código, comprobamos que no haya fuga de datos en la partición y verificamos que la licencia y los límites respecto a las papas canarias estén claros.
- **Qué cambiamos:** adaptamos los textos y ejemplos a un lenguaje sencillo de estudiantes y al monitoreo de la salud de las papas canarias.

## Revisión con la rúbrica (Sprint 14)
- **Corrección técnica (Nivel 3–4):** `01_eda.ipynb` y `02_baseline.ipynb` se ejecutan de arriba abajo con `SEMILLA = 42`, métrica (`F1_macro`) y partición estratificada definidas antes de evaluar, informe de calidad y regla de cuándo no fiarse.
- **Reproducibilidad (Nivel 3–4):** referencia a `PlantVillage-Dataset` y respaldo sintético de papas canarias si no está clonado en Colab, `requirements.txt` y `README.md`.
- **Análisis y comunicación al cliente (Nivel 3–4):** pregunta clara en una frase, cliente, decisión y explicación sencilla de cuándo pedir revisión humana si el modelo duda.
- **IA responsable (Nivel 3–4):** uso de IA declarado y revisado a mano, clasificación RGPD/AI Act y 6 riesgos específicos vinculados a papas canarias.