# Model card · Predicción de cancelaciones de TurisData

Fecha : 12 \- 13.11.2026

**Equipo 5 Green** (Cristina, Miguel, Fran, Andri, Anzhela) ·&nbsp;

Scrum master: Fran, Técnico :  Anzhela

Sprint 8 · «Duelo de modelos» · `SEMILLA = 42` Cuaderno: `reto_S08.ipynb` · Leaderboard: `leaderboard_S08.csv`

> Todas las cifras salen de `reto_S08.ipynb` (la celda final las guarda en `cifras_reto_S08.json`). Los datos son **sintéticos**.

---

## 1 · Resumen para el gerente

Hemos enfrentado **8 modelos de 6 familias** para avisar de qué reservas probablemente se cancelarán, midiéndolos todos con las mismas reglas. **El modelo recomendado es la regresión logística.** Acierta a ordenar las reservas por riesgo de cancelar el **76 %** de las veces (AUC en test \= **0,762**; 50 % sería tirar una moneda), se puede explicar con unas pocas frases, tarda unas centésimas de segundo en entrenarse y ocupa unos 4 KB. **No fue el más complejo**: *boosting*, bosques y SVM no superaron a un modelo sencillo, así que no compensaba pagar su complejidad.

Una cosa importante: el **árbol podado** quedó muy cerca (casi empate). Si lo que más os importa es poder leer el modelo como reglas «si pasa esto, entonces…», es una alternativa igual de válida (apartado 3).

## 2 · Modelo

|  |  |
| :---- | :---- |
| **Campeón** | Regresión logística (familia `lineal`) con preprocesado estándar (imputar nulos, escalar numéricas, *one-hot* de categóricas) |
| **Para qué sirve** | Dar a cada reserva una probabilidad de cancelación, para decidir cuánto sobrevender (*overbooking*) — ver Sprint 7 |
| **Entrada** | 15 variables conocidas **al reservar** (antelación, noches, adultos, niños, precio, peticiones, cliente repetidor, cancelaciones previas, temporada alta, tipo de habitación, régimen, canal, país, tarifa, depósito) |
| **Salida** | Probabilidad entre 0 y 1 de que la reserva se cancele |
| **Hiperparámetros** | `LogisticRegression(max_iter=1000)`; sin búsqueda (no la necesita) |

## 3 · Por qué este modelo y no otro

**Pesos de los criterios** *(propuesta del cuaderno: el equipo debe acordarlos con la «voz del cliente» y firmarlos)*:

| Criterio | Peso | Justificación |
| :---- | :---- | :---- |
| Rendimiento (AUC en validación cruzada) | **50 %** | Cada cancelación no detectada o falsa alarma cuesta dinero (Sprint 7: ≈ 150 € y ≈ 75 €); pero los mejores modelos difieren en pocas centésimas de AUC. |
| Explicabilidad (1 \= caja negra, 5 \= se lee directamente) | **30 %** | El gerente no es técnico y necesita explicar al personal por qué se avisa de una cancelación. |
| Coste (tiempo de ajuste y de predicción \+ tamaño) | **20 %** | Hotel pequeño sin equipo de datos: un modelo barato de reentrenar es una ventaja, pero no lo principal. |

**Leaderboard** (validación cruzada de 5 folds sobre *train*; puntuación global de 0 a 1 con los pesos anteriores):

| Modelo | Familia | AUC (media ± desv.) | Explicabilidad (1–5) | Coste (1 \= barato) | Puntuación global |
| :---- | :---- | :---- | :---- | :---- | :---- |
| logistica **(campeón)** | lineal | 0,755 ± 0,014 | 4 | 0,95 | **0,915** |
| arbol\_podado | arbol | 0,719 ± 0,009 | 5 | 0,90 | **0,911** |
| lightgbm\_ajustado | ensemble\_boosting | 0,747 ± 0,015 | 2 | 0,62 | **0,684** |
| lightgbm | ensemble\_boosting | 0,745 ± 0,014 | 2 | 0,62 | **0,681** |
| random\_forest\_ajustado | ensemble\_bagging | 0,744 ± 0,013 | 2 | 0,18 | **0,591** |
| random\_forest | ensemble\_bagging | 0,737 ± 0,012 | 2 | 0,00 | **0,541** |
| baseline | referencia | 0,500 ± 0,000 | 5 | 1,00 | **0,500** |
| svm\_rbf | svm | 0,735 ± 0,012 | 1 | 0,05 | **0,471** |

**Por qué ganó la logística:** el **AUC más alto** de todos (0,755), una explicabilidad alta (4 de 5: se leen coeficientes) y uno de los **costes más bajos** (solo el baseline, que no predice nada, y a la par del árbol): tarda 0,032 s en ajustarse y pesa 4,1 KB.

**Por qué no ganaron los demás:**

- **Árbol podado** (explicabilidad 5): segundo, a solo 0,004 puntos. Es el más fácil de leer, pero su AUC es menor (0,719 frente a 0,755).  
- ***Boosting*** **(LightGBM) y bosque aleatorio:** AUC algo menor (0,747 el mejor *boosting* ajustado), **cajas negras** (explicabilidad 2\) y mucho más pesados. Con ajuste de hiperparámetros en dos familias (bosque con `GridSearchCV`: 0,744; LightGBM con `RandomizedSearchCV`: 0,747, ambos solo con *train*) **tampoco alcanzaron** a la logística.  
- **SVM:** AUC 0,735, la más lenta (2,4 s de ajuste frente a 0,032 s) y caja negra (explicabilidad 1).  
- **Baseline:** es el suelo (AUC 0,50); no puede ser campeón.

**¿Y si cambian los pesos? (análisis de sensibilidad)**

| Escenario de pesos (rendimiento / explicabilidad / coste) | Campeón |
| :---- | :---- |
| Solo rendimiento (0,8 / 0,1 / 0,1) | logistica |
| Equilibrado (0,4 / 0,4 / 0,2) | **arbol\_podado** |
| Explicabilidad primero (0,2 / 0,6 / 0,2) | **arbol\_podado** |
| **Nuestros pesos** (0,5 / 0,3 / 0,2) | logistica |

**El campeón cambia:** probando las 66 combinaciones de pesos con paso 0,1, gana el árbol podado en 35 y la logística en 31\. **La recomendación depende de lo que valore el cliente:** si prioriza el rendimiento o un equilibrio con algo más de peso en rendimiento, la logística; si prioriza leer el modelo como reglas, el árbol podado. **En ninguna combinación ganan el *boosting*, el bosque ni la SVM.** Además, el ranking depende un poco de los tiempos medidos en cada máquina: simulando ruido del ±30 % en los tiempos, la logística sigue ganando en el **75 %** de los casos (el resto, el árbol podado).

## 4 · Datos y límites

- **Datos:** `reservas_turisdata.csv`, 6 000 reservas **sintéticas** de un solo hotel (llegadas de enero de 2024 a diciembre de 2026), 18 columnas; se predice `cancelada` (tasa del 46 %).  
- **Partición del reto:** 80 % *train* (4 800\) y 20 % *test* (1 200), estratificada, con `SEMILLA_TEST = 7` (distinta de las prácticas, para que el test no se haya visto).  
- **Preprocesado:** `pais_origen` tiene ≈ 2 % de nulos (se imputan con el valor más frecuente); numéricas escaladas; categóricas en *one-hot*.  
- **Variables:** solo las conocidas **al reservar** (sin `cancelada` ni información posterior). `peticiones_especiales` podría registrarse después: en el Sprint 7 se comprobó que quitarla casi no cambia el modelo.  
- **Límites:** datos sintéticos y de un único hotel; no hay precios de la competencia, eventos ni clima; el modelo **no explica causas** (que un canal cancele más no significa que el canal «cause» la cancelación).

## 5 · Métricas (con incertidumbre y test)

| Métrica de la logística | Valor |
| :---- | :---- |
| AUC en validación cruzada (5 folds, *train*) | **0,755 ± 0,014** |
| AP (precisión media) en validación cruzada | 0,718 |
| AUC con 5 semillas distintas de validación cruzada | 0,753 (entre 0,752 y 0,755) |
| **AUC en test (una sola vez, solo el campeón)** | **0,762** |

- **Cómo leer la incertidumbre:** la desviación entre folds es ≈ 0,014. La ventaja de la logística sobre el mejor *boosting* ajustado (0,008 de AUC) es **menor que esa desviación**: son técnicamente parecidos. Por eso se prefiere el más simple y explicable.  
- El AUC de test (0,762) es coherente con el de validación (0,755): no hay señales de sobreajuste ni de que el test se haya usado para elegir.  
- El AUC de test se calculó **una sola vez y solo para el campeón**: en `leaderboard_S08.csv` la columna `auc_test` tiene valor en una única fila.

## 6 · Usos previstos

- Ordenar las reservas futuras por **riesgo de cancelación** para decidir **cuántas habitaciones sobrevender** por fecha (combinado con los costes del Sprint 7).  
- Apoyar la **previsión de ocupación** de la temporada.  
- Priorizar **recordatorios o confirmaciones** a las reservas de más riesgo (sin penalizar a nadie).

## 7 · Usos NO previstos

- **No** usar la probabilidad para **negar reservas**, **cobrar depósitos o recargos** o dar peor trato a un cliente concreto, ni a un país o canal.  
- **No** usar el **país de origen** (ni nada parecido a nacionalidad) como criterio para decidir sobre una persona.  
- **No** usarlo como **previsión financiera** firme: los datos son sintéticos y de un solo hotel.  
- **No** aplicarlo a **otro hotel o destino** sin reentrenar y volver a medir.  
- **No** interpretar los coeficientes como **causas**.  
- Ninguna decisión que afecte a un cliente debe tomarse **sin que una persona la revise**.

## 8 · Explicabilidad (para el gerente)

La regresión logística se explica con **cuánto empuja cada dato hacia «cancela»**. Con las cifras de este modelo (los números son *odds ratio*: 1 \= sin efecto, \>1 más riesgo, \<1 menos):

- **Más riesgo de cancelar:** reservar con mucha **antelación** (×2.14 por cada desviación típica; la variable que más pesa), **sin depósito** (×1.87), por **web intermediaria** (×1.62), con **tarifa flexible** (×1.34) y en **temporada alta** (×1.30).  
- **Menos riesgo:** **depósito total** (×0.43), **canal directo** (×0.54), **tarifa no reembolsable** (×0.60), precio por noche más alto (×0.71) y habitación estándar (×0.78).  
- **Variables que más pesan** (importancia por permutación en validación, sin tocar el test): `antelacion_dias` (0.102), `deposito` (0.056), `canal` (0.041), `tarifa` (0.029) y `precio_noche` (0.016); es decir, **la antelación, el depósito y el canal** explican casi todo.  
- **En una frase:** «una reserva hecha con mucha antelación, sin depósito, por una web intermediaria y con tarifa flexible es la más propensa a cancelarse; una con depósito total, directa y no reembolsable, la que menos».

## 9 · Riesgos e IA responsable

- **País de origen \= variable sensible.** El modelo lo usa como entrada. Medido en validación cruzada sobre *train* (marcando como «riesgo» la mitad de reservas con más probabilidad): el AUC va de **0,693** (desconocido) a **0,810** (FR), una brecha de **0,117**; la tasa de falsas alarmas va de 30 % (NL) a 42 % (desconocido). Los grupos pequeños (p. ej. país no informado: ≈ 108 reservas) dan cifras poco estables.  
- **Canal.** El AUC varía de 0,695 (empresa) a 0,755 (agencia); la web intermediaria recibe muchas más falsas alarmas que el canal directo (≈ 47 % frente a ≈ 17 % de los clientes que sí vienen), en parte porque cancela más de verdad.  
- **Falsas alarmas \= clientes reubicados.** Un falso positivo es un cliente que va a venir pero se marca como «probable cancelación»; con *overbooking* puede quedarse sin habitación. **Quién lo sufre:** más los de web intermediaria y, algo, los de ciertos países.  
- **Medidas:** (1) acordar una **compensación** para clientes reubicados; (2) **no** usar el país como criterio de decisión sobre personas y valorar **quitar `pais_origen`** del modelo y comprobar cuánto se pierde; (3) **revisión humana** de toda decisión individual; (4) **medir cada trimestre** el AUC y las falsas alarmas por canal y país.  
- **Datos sintéticos:** todo se midió sobre datos de prueba; con clientes reales hay que repetirlo antes de decidir nada.  
- **Uso de IA en este trabajo:** declarado en el `README.md` (qué se pidió, qué se revisó).

## 10 · Mantenimiento (deriva)

- **Qué puede cambiar (deriva):** la tasa de cancelación, el peso de cada canal, nuevas políticas de tarifas/depósitos, cambios en la antelación típica, temporadas atípicas.  
- **Qué se medirá:** cada **trimestre**, con las reservas ya resueltas: (a) AUC del modelo, (b) tasa real de cancelación frente a la de entrenamiento (45,9 %), (c) falsas alarmas por canal y país.  
- **Umbral para reentrenar** *(propuesta, a confirmar)*: reentrenar si el **AUC en el último trimestre baja de 0,70** (≈ 5 puntos bajo el actual) o si la **tasa de cancelación se desvía más de 5 puntos** de la de entrenamiento.  
- **Cómo:** reejecutar `reto_S08.ipynb` con los datos nuevos (≈ 2–5 minutos) y comparar con el modelo vigente antes de sustituirlo.  
- **Persona responsable:** *(a confirmar por el equipo: p. ej., la persona de revenue management del hotel, con apoyo del equipo de datos)*.