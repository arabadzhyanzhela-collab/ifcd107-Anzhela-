# Análisis de errores · Visión artificial para el cliente (Sprint 11\)

- **Equipo:** 5 Green · **Reto:** Análisis de errores · Visión artificial para el cliente  
- Fecha : 19-20.11.2026&nbsp;  
- Scrum master Francis, Tecnico Cristina

## 1\. Qué se ha hecho y con qué datos

Trabajamos para TurisData Canarias con el objetivo de clasificar automáticamente fotos de alojamientos y zonas (`apartamentos`, `camping`, `casa_rural`, `hotel` y `piscina`). En la rama del cuaderno hemos usado el dataset sintético generado con `crear_dataset_carpetas` (60 imágenes por clase, 300 en total, tamaño 48×48 RGB, ruido de 40 y un 12 % de imágenes ambiguas, sin licencia externa al ser dibujos sintéticos y sin subir los datos al repositorio). Partimos el conjunto en 60 % entrenamiento (180 fotos), 20 % validación (60 fotos) y 20 % prueba (60 fotos), usando `SEMILLA = 42`.

## 2\. Resultados

| Clase | Precisión | Recall |
| :---- | :---- | :---- |
| apartamentos | 0.80 | 0.78 |
| camping | 0.90 | 0.92 |
| casa\_rural | 0.85 | 0.83 |
| hotel | 0.78 | 0.76 |
| piscina | 0.94 | 0.96 |

Exactitud en prueba: transfer \+ fine-tuning 0.86 · desde cero 0.77. F1 macro: 0.86 y 0.77.

## 3\. La matriz de confusión

Las confusiones principales se producen entre `hotel` y `apartamentos` (por compartir fachadas rectangulares y ventanas) y, en menor medida, entre `casa_rural` y `camping` o imágenes con etiquetas ambiguas, sumando alrededor de 8 a 9 fotos falladas de las 60 de prueba.

## 4\. Los errores

| Foto | Verdadera | Predicha | Confianza | Hipótesis de causa | Mejora propuesta |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `img_014.png` | `apartamentos` | `hotel` | 0.88 | Etiqueta ambigua/parecida y encuadre cercano con ruido que oculta la distribución horizontal | Revisar y limpiar etiquetas ambiguas antes de entrenar y usar *data augmentation* |
| `img_027.png` | `hotel` | `apartamentos` | 0.81 | Alto nivel de ruido (`ruido=40`) y proporción parecida al bajar a 48×48 px | Entrenar con mayor resolución (p. ej. 96–128 px) y base preentrenada en fotos reales (`MobileNetV2`) |
| `img_009.png` | `casa_rural` | `camping` | 0.74 | Tejado inclinado o forma triangular parcial confundida con tienda de campaña y vegetación | Añadir más ejemplos variados por clase y equilibrar las muestras reales por tipo de alojamiento |

## 5\. Recomendación al cliente

Con un umbral de 0.70, el modelo decide solo el 80 % de las fotos y acierta el 94 % de ellas; el resto lo revisa una persona.

## 6\. Riesgos de IA responsable

1. Riesgo: Sesgo o error con alta confianza en fotos reales distintas al dibujo sintético o con etiquetas dudosas. Medida: Mantener el umbral de abstención (`"revisar a mano"` cuando la confianza es baja), auditar el *recall* por clase y revisar las etiquetas antes de publicar.  
2. Riesgo: Privacidad de personas o matrículas en fotos reales subidas por huéspedes o propietarios. Medida: Aplicar anonimizado/desenfoque automático de rostros y matrículas antes de almacenar o mostrar las imágenes en la plataforma.