# Herramientas internas · TurisData Canarias

> **README corto** para la entrega en nivel mínimo con explicación. Cópialo como `README.md`, sustituye lo que está entre `<...>` y borra este aviso. Si tu equipo llega más lejos, usa `README_PLANTILLA.md`.

**Equipo:** 5Green· **Fecha:** 04-11-2026

## **Qué hace**

Lee el archivo CSV de reservas y procesa los datos para calcular los principales indicadores clave de rendimiento (KPIs). Finalmente, exporta los resultados en un archivo JSON estructurado para facilitar su consulta e integración con otros sistemas.

## **Cómo se ejecuta y se prueba**

El programa se ejecuta desde la terminal indicando el CSV de reservas, el archivo JSON de salida y la capacidad máxima mediante \--capacidad. Para comprobar su correcto funcionamiento, se ejecutan las pruebas automatizadas.

**python kpis.py reservas\_turisdata.csv salida.json \--capacidad 40**

**python test\_kpis.py**

**Descripción de los comandos:**

* kpis.py: procesa las reservas y calcula los KPIs.  
* reservas\_turisdata.csv: archivo de entrada con los datos.  
* salida.json: archivo generado con los resultados.  
* \--capacidad 40: establece una capacidad máxima de 40\.  
* test\_kpis.py: ejecuta las pruebas para validar el funcionamiento.

Resultado de las pruebas: \<12 de 12  superadas\>

## **Quién hizo qué**

| Parte | La escribí yo | La copié y la expliqué |
| :---- | :---- | :---- |
| `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva` | Miguel, Cristina, Andrii, Anzhela, Francis | Miguel, Cristina, Andrii, Anzhela, Francis |
| `_convertir_fila` y `leer_reservas` | Miguel, Cristina, Andrii, Anzhela, Francis | Miguel, Cristina, Andrii, Anzhela, Francis |
| `exportar_json` y `main` | Miguel, Cristina, Andrii, Anzhela, Francis | Miguel, Cristina, Andrii, Anzhela, Francis |

&nbsp;

## **Explicación de una función**

Esta función calcula cuánto dinero ingresa de media el hotel por cada reserva. Primero, descarta las reservas que fueron canceladas para que los cálculos no fallen. Después, multiplica las noches de cada estancia válida por su precio para saber el total, suma esas cantidades y las divide entre el número de reservas. Por último, redondea el resultado a dos decimales, o devuelve 0.0 si la lista está vacía para evitar que el programa se rompa.

## **Errores que controla**

El programa está preparado para que, si el archivo CSV no existe o está mal colocado, aparezca un mensaje de aviso claro en la pantalla en lugar de un código de error largo y confuso. También detecta si faltan columnas o si hay datos extraños (como precios negativos o estancias de cero noches), los elimina y anota cuántos fallos se han encontrado.

## **Uso de IA**

Hemos utilizado la inteligencia artificial como una ayuda..

## **Qué mejoraríamos**

Nos gustaría añadir en el futuro un comando extra para poder filtrar las reservas por meses directamente desde la terminal, sin tener que cambiar el código fuente.

&nbsp;