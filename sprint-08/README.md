# Sprint 8 · Reto «Duelo de modelos» · Equipo 5 Green

**Fecha** : 12 \- 13.11.2026

**Equipo:** Cristina, Miguel, Fran, Andri y Anzhela  
**Curso:** Especialista en Inteligencia Artificial (IFCD107)  
**Repositorio del Sprint:** Carpeta `sprint-08/` del repositorio privado del equipo.

Scrum master: Fran, Tecnico :  Anzhela

---

## 1\. Qué se entrega

Para superar este sprint de «Duelo de modelos», los entregables obligatorios que contiene nuestra carpeta son los siguientes:

| Fichero | Contenido detallado |
| :---- | :---- |
| `reto_S08.ipynb` | Cuaderno principal basado en la plantilla oficial (`S08_06_leaderboard_plantilla`): incluye 8 modelos evaluados de 6 familias diferentes, búsquedas de hiperparámetros con validación cruzada en 2 familias, ponderación mediante pesos, análisis de sensibilidad, apartados extras y la prueba de test final ejecutada una única vez sobre el modelo campeón\[cite: 13\]. |
| `leaderboard_S08.csv` | Tabla comparativa completa de resultados generada automáticamente por la ejecución final del cuaderno\[cite: 13\]. |
| `model_card.md` | Ficha técnica completa del modelo campeón estructurada en sus 10 apartados obligatorios\[cite: 13\]. |
| `README.md` | Este documento descriptivo con las instrucciones de reproducción, autorías y uso de IA\[cite: 13\]. |
| `autoevaluacion_<nombre>.md` | Fichas individuales de autoevaluación y coevaluación de cada uno de los 5 integrantes del equipo (`anzhela`, `cristina`, `miguel`, `fran`, `andri`)\[cite: 13\]. |

*Nota sobre los datos:* Los datos no se almacenan estáticamente en el repositorio; el cuaderno se encarga de descargar de forma automatizada el archivo `reservas_turisdata.csv` directamente desde las fuentes oficiales del curso\[cite: 13\].

---

## 2\. Resumen de Resultados del Duelo

Tras la ejecución del proceso de validación cruzada y la aplicación de nuestra tabla de pesos personalizada (rendimiento, velocidad e interpretabilidad):

* **Modelo Campeón:** Regresión Logística (`logistica`), con una puntuación global ponderada de **0,915**\[cite: 13\].  
* **Métrica en Test:** El AUC obtenido en el conjunto de prueba final (evaluado estrictamente una sola vez) fue de **0,762**\[cite: 13\].  
* **Competencia:** Qio muy cerca el Árbol de Decisión Podado (puntuación global de **0,911**)\[cite: 13\]. Los detalles de los motivos de la elección se encuentran documentados en el fichero `model_card.md`\[cite: 13\].

---

## 3\. Cómo reproducirlo paso a paso

Para garantizar la total reproducibilidad de los resultados y evitar discrepancias en el entorno:

1. Abrir el archivo `reto_S08.ipynb` directamente en [Google Colab](https://colab.research.google.com)\[cite: 13\].  
2. En la barra superior de herramientas, ir a **Entorno de ejecución → Reiniciar y ejecutar todo** (*Restart and Run All*)\[cite: 13\].  
3. *Aclaración de dependencias:* No es necesario instalar librerías adicionales externas; Google Colab incorpora de serie `scikit-learn` y `lightgbm`\[cite: 13\].  
4. **Tiempo de ejecución estimado:** El proceso completo tarda entre **3 y 5 minutos**, ya que incluye las celdas de optimización e hiperparámetros\[cite: 13\].  
5. **Archivos generados al finalizar:** Al terminar de correr el cuaderno, asegúrate de descargar los archivos de salida generados en el entorno virtual: `leaderboard_S08.csv` y `cifras_reto_S08.json`\[cite: 13\].  
6. **Semillas fijadas:** El código opera de forma determinista utilizando `SEMILLA = 42` (para particiones de validación cruzada y entrenamiento de modelos) y `SEMILLA_TEST = 7` (para la partición final de test)\[cite: 13\].

### Versiones del entorno técnico empleadas:

* **Python:** 3.12.3\[cite: 13\]  
* **scikit-learn:** 1.9.1\[cite: 13\]  
* **pandas:** 3.0.6\[cite: 13\]  
* **numpy:** 2.5.4\[cite: 13\]  
* **lightgbm:** 4.7.0\[cite: 13\]

---

## 4\. Reparto de tareas (Quién hizo qué)

Para cumplir con los principios de desarrollo ágil y revisión por pares, el trabajo del sprint se distribuyó de la siguiente manera:

| Módulo / Apartado del Reto | Responsable de la Creación | Responsable de la Revisión (Peer Review) |
| :---- | :---- | :---- |
| Asignación de pesos, justificación de criterios y análisis de sensibilidad | Cristina\[cite: 13\] | Miguel\[cite: 13\] |
| Implementación del baseline, modelo de regresión logística y contendientes | Miguel\[cite: 13\] | Fran\[cite: 13\] |
| Búsquedas y optimización de hiperparámetros | Fran\[cite: 13\] | Andri\[cite: 13\] |
| Bloque de extras (incertidumbre, importancias de variables e IA responsable) | Andri\[cite: 13\] | Anzhela\[cite: 13\] |
| Ejecución del test final y redacción de la `model_card.md` | Anzhela\[cite: 13\] | Cristina\[cite: 13\] |
| Integración del README, gestión de commits y subida a GitHub | Todo el equipo\[cite: 13\] | — |

---

## 5\. Declaración sobre el uso de Asistentes de IA

* **Herramienta empleada:** Claude (Anthropic) y ChatGPT para la estructuración inicial de código basada en la plantilla `S08_06_leaderboard_plantilla` y la redacción formal de la documentación técnica.  
* **Verificaciones manuales realizadas por el equipo:**  
  1. Se ejecutó de principio a fin el cuaderno en un entorno limpio de Google Colab para validar que todas las métricas de rendimiento coincidían exactamente con los datos declarados\[cite: 13\].  
  2. Se auditó línea por línea el código para garantizar que el conjunto de prueba (`X_test`) no se filtrara de ninguna manera ni interviniera en las fases de validación cruzada o búsqueda de hiperparámetros\[cite: 13\].  
  3. Los pesos aplicados en la fórmula del leaderboard fueron consensuados y adaptados de forma autónoma por el equipo en función de los requerimientos de negocio de TurisData Canarias, y no obedecen a sugerencias automáticas de la IA\[cite: 13\].

---

## 6\. Autoevaluación y Coevaluación

Los registros individuales de autoevaluación y la matriz cruzada de coevaluación de cada miembro del equipo (`anzhela`, `cristina`, `miguel`, `fran`, `andri`) se encuentran debidamente cumplimentados y alojados de manera independiente dentro de esta misma carpeta `sprint-08/`\[cite: 13\].