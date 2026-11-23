# Sprint 10 · Entregable

Fecha : 17-18.11.2026&nbsp;

Scrum master Cristina, Tecnico Francis&nbsp;

- **Equipo:** 5 Green (Cristina, Miguel, Fran, Andri y Anzhela)  
- **Reto:** ¿Vale la pena la red?  
- **Problema elegido:** cancelaciones (`cancelada`), con extra de precio por noche  
- **Qué se entrega:** el cuaderno `reto_vale_la_pena.ipynb` (ejecutado), el informe `informe_comparativo.md`, este `README.md`, una autoevaluación y coevaluación por persona (`autoevaluacion_nombre.md`) y, opcionales, `curvas_aprendizaje.png` y `mlp_final.keras`  
- **Quién hizo qué:**  
  - Cristina (@cristina): cuaderno, ejercicios 1 y 2  
  - Miguel (@miguel): variantes del MLP, diagnóstico y ejercicio 3  
  - Fran (@fran): comparación, bootstrap y ejercicio 4  
  - Andri (@andri): informe comparativo  
  - Anzhela (@anzhela): README, extras (país/canal, umbral, modelo guardado) y subida de ficheros  
- **Cómo reproducirlo:** abrir `reto_vale_la_pena.ipynb` en Google Colab (CPU, sin GPU) y ejecutar de arriba abajo (*Entorno de ejecución → Reiniciar y ejecutar todo*). La primera celda descarga los datos sola.

## Datos

`reservas_turisdata.csv` (6000 reservas sintéticas). El cuaderno lo descarga de `https://raw.githubusercontent.com/cCoolBoox/IFCD107-alumnado/main/datos/reservas_turisdata.csv`. Una copia sin cambios está en `data/` del repositorio del equipo.

## Versiones y semillas

- Con las que se ejecutó: Python 3.12.3 · Keras 3.15.1 · TensorFlow 2.21.0 · scikit-learn 1.9.1 · pandas 3.0.6 · numpy 2.5.4. En Colab las versiones pueden ser otras y las cifras pueden cambiar un poco en la tercera cifra decimal; en el informe se usan las de la ejecución final.  
- Semillas: partición y boosting \= 42; MLP \= 1, 2 y 3; bootstrap \= 42\.  
- Partición única: 64 % entrenamiento, 16 % validación, 20 % prueba, con el escalador ajustado solo con el entrenamiento.

## Resultado en una línea

Recomendamos mantener el boosting: el MLP no lo mejora de forma clara (diferencia de AUC \+0,007, intervalo del 95 % \[−0,005, \+0,020\]) y tarda unas 37 veces más en entrenar.