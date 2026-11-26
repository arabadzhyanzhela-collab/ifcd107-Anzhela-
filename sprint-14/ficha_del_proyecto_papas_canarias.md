# Ficha del proyecto · Equipo 5 Green

## 1\. Equipo y roles iniciales

- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri, Anzhela).  
- **Roles iniciales:** Scrum Master (Miguel), Responsable técnico (Fran), Responsable de datos (Andri), Responsable de IA responsable (Cristina) y Documentación/entrega (Anzhela), con rotación al cierre de cada sprint (S14 \-\> S15 \-\> S16 \-\> S17).

## 2\. Brief y pregunta de negocio

- **Brief elegido:** Salud de cultivos — Monitoreo de la salud de las **papas canarias** (*«¿Hoja sana o enferma, y cuándo no fiarnos del modelo?»*).  
- **Pregunta de negocio (en una frase):** Ayudamos al personal técnico y agricultor de papas canarias a priorizar qué parcelas o plantas revisar o tratar con un modelo que distingue hojas sanas y enfermas e indica cuándo no fiarse de la predicción, medido con `F1_macro` y revisión humana en casos dudosos frente a un baseline simple.

## 3\. Cliente y decisión

- **Cliente:** agricultor o responsable técnico del cultivo de papas canarias.  
- **Decisión que apoya:** decidir qué zonas del cultivo revisar o proteger y qué fotos enviar a inspección humana cuando haya dudas.  
- **Qué pasa hoy sin el modelo:** la inspección visual manual en parcela exige más tiempo y puede verse afectada por el volumen de plantas o cambios de luz.

## 4\. Datos

- **¿Es legal usarla? (Licencia):** Tiene una licencia abierta como *CC0 (Dominio Público)*  
- **Fuente :** base de partida en `PlantVillage-Dataset` (`https://github.com/spMohanty/PlantVillage-Dataset`, enfocada en subconjunto de papa y complementada con validación para variedades y condiciones de papas canarias; revisamos la licencia y condiciones de uso directamente en el repositorio antes de entrenar en producción, y usamos respaldo sintético reproducible con `SEMILLA = 42` si aún no está clonado en Colab).  
- **Tamaño y periodo:** conjunto de imágenes de hojas de papa clasificadas en `sana` y `enferma`, junto con métricas básicas de imagen (`brillo`, `contraste`, `indice_verdor`) y hash `MD5`.  
- **Límites:** `PlantVillage-Dataset` no recoge por sí solo todas las variedades tradicionales de papa canaria ni las condiciones de niebla, viento o suelo de todas las islas; por eso es clave indicar cuándo no fiarse del modelo.

## 5\. Métrica y baseline

- **Métrica de negocio:** reducción del tiempo de criba visual y menor riesgo de actuar a ciegas en imágenes dudosas de papas canarias.  
- **Métrica técnica:** `F1_macro` (fijada antes de ver resultados), apoyada por `accuracy` y matriz de confusión.  
- **Umbral de éxito:** superar con claridad al baseline (`DummyClassifier` y modelo base) y marcar como `no_fiarse` las predicciones con baja confianza o bajo contraste.  
- **Baseline previsto:** `DummyClassifier` (`most_frequent`) y modelo base sobre descriptores de imagen (`02_baseline.ipynb`), con partición estratificada y `SEMILLA = 42`.

## 6\. Modelos previstos

- Baseline simple (`DummyClassifier`), modelo base de color/contraste y red neuronal (`CNN` / transferencia de aprendizaje en S15) adaptada a hojas de papa con criterio explícito de cuándo no fiarse.

## 7\. Demostrador previsto

- **Tecnología:** aplicación sencilla en Python/Colab/interfaz ligera para subir una foto de hoja de papa, ver `sana` o `enferma` y mostrar un aviso claro de «no fiarse / revisar» si la confianza o el contraste son bajos.

## 8\. Riesgos y mitigación

- **Baja calidad visual o niebla/sombra en parcela:** comprobar contraste/confianza y activar `no_fiarse` para revisión humana.  
- **Diferencia entre imágenes de referencia y variedades de papas canarias:** documentar el límite de dominio y validar con muestras de papas canarias.  
- **Desequilibrio entre clases:** revisar en el EDA, usar estratificación y evaluar con `F1_macro`.  
- **Clasificación preliminar AI Act / RGPD:** sin datos personales de personas; sistema de apoyo con supervisión humana ante dudas y transparencia sobre sus límites.

## 9\. Backlog y objetivos por sprint

- **Sprint 14:** cerrar ficha de papas canarias, plan de datos y licencias (`PlantVillage-Dataset`), `01_eda.ipynb`, `02_baseline.ipynb`, backlog, plan ético y repositorio.  
- **Sprint 15:** entrenar y comparar al menos 3 modelos (incluida red neuronal) y registrar experimentos.  
- **Sprint 16:** evaluación con gráficos, análisis de cuándo no fiarnos, demostrador y memoria técnica.  
- **Sprint 17:** presentación (≤ 12 diapositivas), ensayo y defensa oral de todo el equipo.

&nbsp;