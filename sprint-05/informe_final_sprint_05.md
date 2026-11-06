# 📊 Informe Final · Sprint 05: «¿La ocupación depende de esto? (Matemáticas en Código y Gradiente)»

**Consultora:** 5Green (Anzhela, Cristina, Miguel, Fran y Andrii)  
**Cliente:** TurisData Canarias  
**Curso:** IFCD107 · Especialista en Inteligencia Artificial y Big Data (Servicio Canario de Empleo)  
**Fecha:** Noviembre de 2026

---

## 1\. Resumen Ejecutivo del Sprint

Durante el **Sprint 05**, el equipo **5Green** ha dado el salto conceptual desde el análisis de datos puramente descriptivo hacia la **fundamentación matemática subyacente de los modelos de Machine Learning**.

Hemos respondido a la pregunta clave de negocio de *TurisData Canarias*: **¿Cómo se relacionan de forma matemática las variables operativas (como la antelación de reserva o los precios) con la ocupación hotelera y el riesgo de cancelación?** Para ello, hemos implementado desde cero y sin librerías "caja negra" los conceptos de correlación estadística, regresión lineal y el algoritmo de optimización por **Descenso del Gradiente**.

---

## 📋 1.1. Objetivo del Sprint

Demostrar mediante código en Python los conceptos matemáticos y estadísticos que sustentan el aprendizaje automático (Machine Learning). En este sprint analizamos la relación entre el precio por noche, las noches reservadas y la tasa de ocupación, implementando un algoritmo de **Descenso del Gradiente desde cero** y realizando análisis de correlación lineal para el cliente TurisData Canarias.

---

## 📁 1.2. Estructura de Ficheros (`sprint-05/`)

* `S05_Ocupacion_y_Gradiente.ipynb`: Notebook principal con la teoría, código interactivo y experimentos en Google Colab.  
* `README.md`: Instrucciones y explicación general del sprint.  
* `autoevaluacion_sprint_05.md`: Matriz de verificación individual de la Definition of Done.  
* `coevaluacion_sprint_05.md`: Matriz de evaluación cruzada entre miembros del equipo 5Green.

---

## 🛠️ 1.3. Contenido Técnico y Experimentos

1. **Álgebra Lineal con NumPy:** Operaciones matriciales para calcular ingresos totales y promedios de estancia.  
2. **Estadística Descriptiva y Correlación:** Cálculo de media, mediana, desviación estándar y correlación de Pearson entre precio y ocupación.  
3. **Descenso del Gradiente desde Cero:** Optimización de una función de coste $MSE(w,b)$ para encontrar la recta de ajuste de la demanda sin usar librerías avanzadas de ML.

&nbsp;

## 2\. Bloques de Trabajo Desarrollados

### 2.1. Análisis Exploratorio y Correlación de Pearson ($r$)

* **Objetivo:** Medir la fuerza y dirección de la relación lineal entre variables numéricas clave de las reservas de TurisData (por ejemplo, entre los días de antelación y el precio por noche, o la ocupación y las cancelaciones).  
* **Fundamento matemático:** $$r=\frac{\sum\limits_{}^{}({x}_{i}-\bar{x})({y}_{i}-\bar{y})}{\sqrt{\sum\limits_{}^{}({x}_{i}-\bar{x}{)}^{2}\sum\limits_{}^{}({y}_{i}-\bar{y}{)}^{2}}}$$  
* **Hallazgos:** Las reservas de última hora (menor antelación) en canales OTA presentan una correlación positiva fuerte con tarifas rebajadas de última hora, lo que incrementa la volatilidad de la ocupación en los establecimientos de Tenerife y Gran Canaria.

### 2.2. Regresión Lineal Simple y Mínimos Cuadrados

* **Objetivo:** Ajustar una línea recta $y=w\cdot x+b$ para predecir el comportamiento del ingreso o la ocupación en función de variables independientes.  
* **Función de Costo (Error Cuadrático Medio \- MSE):** $$MSE=\frac{1}{n}\sum\limits_{i=1}^{n}({y}_{i}-(w\cdot {x}_{i}+b){)}^{2}$$

### 2.3. Optimización mediante el Descenso del Gradiente (*Gradient Descent*)

* **Objetivo:** Encontrar los parámetros óptimos ($w$ y $b$) de manera iterativa simulando el descenso por una montaña para minimizar el error del modelo.  
* **Tasas de aprendizaje ($\alpha$):** Probamos diferentes valores en Google Colab comprobando que una tasa muy alta ($\alpha =0.1$) provoca divergencia (el error explota), mientras que una tasa adecuada ($\alpha =0.01$) converge suavemente hacia el mínimo error global.

---

## 3\. Estructura de Ficheros del Repositorio (`sprint-05/`)

Para cumplir estrictamente con la *Definition of Done* (DoD) en GitHub, la estructura generada y validada por el equipo es la siguiente:

* `README.md`: Documentación técnica y guía de uso del sprint.  
* `notebook_sprint05.py`: Script ejecutable en Google Colab con el modelado matemático y gráficos de convergencia del gradiente.  
* `autoevaluacion_sprint_05.md`: Tabla individual de autoevaluación de los 5 integrantes.  
* `coevaluacion_sprint_05.md`: Tabla de coevaluación cruzada del equipo.

---

## 4\. Tablas de Autoevaluación y Coevaluación del Sprint 05

### A. Autoevaluación del Sprint 05

| Criterio de Autoevaluación | Anzhela | Cristina | Miguel | Fran | Andrii |
| :---- | :---: | :---: | :---: | :---: | :---: |
| 1\. ¿Se comprende y ejecuta correctamente la correlación de Pearson en Colab? | Sí | Sí | Sí | Sí | Sí |
| 2\. ¿Se ha implementado el Descenso del Gradiente desde cero sin errores? | Sí | Sí | Sí | Sí | Sí |
| 3\. ¿La documentación del repositorio en `sprint-05/` está completa? | Sí | Sí | Sí | Sí | Sí |
| 4\. ¿Se han documentado las conclusiones de negocio para TurisData? | Sí | Sí | Sí | Sí | Sí |
| 5\. ¿Se ha completado la coevaluación cruzada del equipo 5Green? | Sí | Sí | Sí | Sí | Sí |

### B. Coevaluación (Evaluación entre Pares \- Rúbrica 1 a 4\)

| Criterio de Coevaluación | Anzhela | Cristina | Miguel | Fran | Andrii |
| :---- | :---: | :---: | :---: | :---: | :---: |
| **Fundamentación matemática y rigor analítico** | 4 | 4 | 4 | 4 | 4 |
| **Reproducibilidad y código en Google Colab** | 4 | 4 | 4 | 4 | 4 |
| **Enfoque al negocio hotelero (TurisData)** | 4 | 4 | 4 | 4 | 4 |
| **Trabajo en equipo y gestión Scrum (5Green)** | 4 | 4 | 4 | 4 | 4 |

---

&nbsp;

### A. Autoevaluación del Sprint 05

| Criterio de Autoevaluación | Anzhela | Cristina | Miguel | Fran | Andrii |
| :---- | :---: | :---: | :---: | :---: | :---: |
| 1\. ¿Se comprende y ejecuta correctamente la correlación de Pearson en Colab? | Sí | Sí | Sí | Sí | Sí |
| 2\. ¿Se ha implementado el Descenso del Gradiente desde cero sin errores? | Sí | Sí | Sí | Sí | Sí |
| 3\. ¿La documentación del repositorio en sprint-05/ está completa? | Sí | Sí | Sí | Sí | Sí |
| 4\. ¿Se han documentado las conclusiones de negocio para TurisData? | Sí | Sí | Sí | Sí | Sí |
| 5\. ¿Se ha completado la coevaluación cruzada del equipo 5Green? | Sí | Sí | Sí | Sí | Sí |

### B. Coevaluación (Evaluación entre Pares \- Rúbrica 1 a 4\)

| Criterio de Coevaluación | Anzhela | Cristina | Miguel | Fran | Andrii |
| :---- | :---: | :---: | :---: | :---: | :---: |
| Fundamentación matemática y rigor analítico | 4 | 4 | 4 | 4 | 4 |
| Reproducibilidad y código en Google Colab | 4 | 4 | 4 | 4 | 4 |
| Enfoque al negocio hotelero (TurisData) | 4 | 4 | 4 | 4 | 4 |
| Trabajo en equipo y gestión Scrum (5Green) | 4 | 4 | 4 | 4 | 4 |

---

&nbsp;

## 5\. IA Responsable y Transparencia

Los cálculos estadísticos y modelos de regresión se han ejecutado sobre datos anonimizados sin variables sensibles (*PII*). Todas las explicaciones matemáticas han sido validadas por el equipo 5Green.

&nbsp;

*Informe final consolidado para el proyecto TurisData Canarias \- Consultora 5Green.*

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;