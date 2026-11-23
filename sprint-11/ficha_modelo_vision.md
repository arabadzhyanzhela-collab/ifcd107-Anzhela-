# Ficha del Modelo de Visión Artificial · TurisData Canarias

**Equipo:** 5 Green (Cristina, Miguel, Fran, Andri, Anzhela) · **Sprint 11**

- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

---

## 1\. Resumen del problema y datos

- **Objetivo:** Clasificar automáticamente las fotos que suben propietarios y huéspedes en 5 categorías: `hotel`, `apartamentos`, `casa_rural`, `camping` y `piscina`.  
- **Dataset:** 300 imágenes sintéticas (60 por clase, tamaño 48×48 RGB) con ruido y un **12 % de imágenes ambiguas** (dibujos muy parecidos a otra categoría que simulan fotos difíciles o mal etiquetadas).  
- **Reparto de datos:** 60 % entrenamiento (180 fotos), 20 % validación (60 fotos, usada para elegir modelo y umbral) y 20 % prueba (60 fotos, mirada una sola vez al final).

---

## 2\. Comparación de modelos y resultados en prueba

Comparamos entrenar una CNN desde cero (con solo 180 fotos) frente a reutilizar una base preentrenada en formas y texturas (*transfer learning*) y ajustar su último bloque (*fine-tuning* con tasa `1e-4`):

| Estrategia | Exactitud en prueba | F1 macro | Observaciones |
| :---- | :---- | :---- | :---- |
| **CNN desde cero** | \~0,75 – 0,80 | \~0,75 | Con pocas imágenes le cuesta aprender bordes y formas desde cero |
| **Transfer learning \+ fine-tuning** | **\~0,85 – 0,88** | **\~0,86** | Reutiliza los filtros aprendidos y mejora tanto la exactitud como la estabilidad |

### Rendimiento por clase (Prueba)

- **Clases más fáciles (`piscina`, `camping`):** Tienen colores y formas muy distintas (el azul de la piscina o el triángulo de la tienda de campaña), alcanzando precisiones y *recalls* cercanos al 0,90–0,95.  
- **Clase más difícil (`hotel` / `apartamentos`):** Son las que tienen menor *recall* (alrededor de 0,75–0,80) porque comparten estructura rectangular, ventanas y colores claros.

---

## 3\. Análisis de errores (¿Dónde y por qué falla?)

Al revisar las imágenes mal clasificadas y la matriz de confusión observamos:

1. **Confusiones lógicas entre clases parecidas:** La mayoría de los fallos ocurren entre **`hotel` ↔ `apartamentos`** y **`casa_rural` ↔ `camping`**. Son errores razonables incluso para una persona cuando la foto tiene mucho ruido o el edificio se ve pequeño.  
2. **Impacto de las imágenes ambiguas:** El 12 % de etiquetas cruzadas del dataset provoca algunos errores con confianza alta; esto demuestra que **limpiar y revisar las etiquetas** antes de entrenar es clave en un proyecto real.  
3. **Hipótesis de mejora:** Para llevarlo a producción con fotos reales de TurisData usaríamos **MobileNetV2 preentrenada en ImageNet** (con imágenes de al menos 128×128 px), *data augmentation* (giros suaves y cambios de brillo) y al menos 100–200 fotos reales revisadas por categoría.

---

## 4\. IA Responsable: Abstención y riesgos

### Regla de abstención (Umbral \= 0,70 elegido en validación)

Para no publicar fotos mal etiquetadas en la web de TurisData, si la red tiene menos de un **70 % de seguridad**, devuelve `"revisar a mano"`:

- **Cobertura en prueba:** \~78 % – 83 % de las fotos se clasifican solas sin intervención humana.  
- **Exactitud en las aceptadas:** \~92 % – 95 % de acierto (sube unos 7–10 puntos respecto a no filtrar).

### Riesgos específicos y medidas

1. **Sesgo de representación:** Si entrenamos solo con fotos de hoteles grandes o piscinas de lujo, la red fallará con alojamientos rurales modestos. *Medida:* Auditar el *recall* por cada tipo de alojamiento y recoger muestras equilibradas de todas las islas.  
2. **Privacidad en fotos reales:** Las fotos subidas por huéspedes pueden mostrar caras de personas o matrículas de coches. *Medida:* Aplicar un filtro automático de anonimizado/desenfoque de rostros antes de guardar las imágenes.  
3. **Alucinaciones por cambio de dominio:** Fotos nocturnas, de interiores o muy borrosas pueden confundir al modelo. *Medida:* Mantener siempre el umbral de abstención (`0,70`) y permitir que el propietario corrija la etiqueta sugerida.

---

## 5\. Declaración de uso de IA

- **Qué se pidió:** Apoyo para completar las funciones de los ejercicios 1 al 5 del cuaderno `S11_04_reto_vision_cliente.ipynb` y estructurar esta ficha en Markdown.  
- **Qué se revisó y cambió:** Todo el equipo ejecutó el cuaderno en Google Colab de principio a fin (`Reiniciar y ejecutar todo`), verificando que pasaran todos los `assert`, comprobando que el umbral se eligiera únicamente con `X_val` y revisando los gráficos de errores reales generados por nuestro modelo.

---

## 6\. Revisión con la rúbrica (Auditoría interna del equipo)

*Revisión cruzada realizada antes de la entrega:*

| Criterio | Nivel (1–4) | Prueba escrita |
| :---- | :---- | :---- |
| **Corrección técnica** | **3** | Todos los `assert` de los 5 ejercicios pasan sin errores; se compara *transfer learning \+ fine-tuning* frente a entrenamiento desde cero y se calcula precisión/recall por clase. |
| **Reproducibilidad** | **3** | Al pulsar *Reiniciar y ejecutar todo* en Colab con `SEMILLA = 42` se regenera el dataset y se obtienen exactamente las mismas métricas y gráficas; no se suben datos temporales al repo. |
| **Análisis y comunicación al cliente** | **3** | La ficha identifica las clases más difíciles (`hotel`/`apartamentos`), explica los errores con hipótesis visuales y propone una solución práctica para TurisData. |
| **IA responsable** | **3** | El umbral de abstención (`0,70`) se elige exclusivamente en validación y se evalúa en prueba; se detallan 3 riesgos reales (sesgo, privacidad, cambio de dominio) y sus medidas, además del uso de IA. |

&nbsp;