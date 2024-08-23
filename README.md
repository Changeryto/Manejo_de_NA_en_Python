# Como descargar y ejecutar esta notebook

En un directorio vacío, ejecuta

```sh
git clone https://github.com/Changeryto/Manejo_de_NA_en_Python.git
```

Para crear el entorno virtual, ejecuta

```sh
python -m venv env
```

Activa el entorno virtual con

```sh
source env/bin/activate
```

Finalmente instala las dependencias con

```sh
pip install requirements.txt
```

Listo!

# Manejo De NAs

By/Por: Rubén Téllez Gerardo

Curso de manejo de valores faltantes en Platzi.

## Extendiendo la API de Pandas

Al rededor de pandas hay un ecosistema de paquetes diseñado para la manipulación de pandas desde una base común.

## Tabulación de valores faltantes

### Es preferible empezar con resúmenes simples. Por ejemplo: 

- ¿Cuántos valores deberían existir en el conjunto de datos?
- ¿Cuántos valores existen en el conjuntos de datos?
- ¿Cuántos valores completos existen en el conjunto de datos?

### Construir resúmenes por variables y por observaciones

- ¿Cuáles valores faltantes existen por cada variable?
- ¿Cuántos valores faltantes existen por cada observación?
- ¿Cuantas variables tiene X numero de valores faltantes?
- ¿Cuántas observaciones tienen X número de valores faltantes?

De esta forma resulta más sencillo saber dónde se están acumulando los valores faltantes. Así se va a continuar la exploración.

En algún momento va a hacer falta realizar preguntas por negocio u objetivos, por ejemplo: ¿Qué está pasando semana a semana? ¿Mes a mes? ¿Paso a paso? ¿Cuál es la racha?
A travez de la racha puede intuirse que algo ha sucedido en ese momento.


## Tipos de valores faltantes.

Debe entenderse la diferencia para conocer el por qué de su falta.

Por lo general hay 3.

### Missing Completely at Random (MCAR)

Debido a fallos de la medición sin responsabilidad otorgable.
La localización de los valores faltantes en el conjunto de datos ocurre completamente al azar, sin dependencia de otrodato.

### Missing at random (MAR)

Debido a periodos de paro en la toma de mediciones en periodos conocidos.
La localización de los valores faltantes en el conjunto de datos depende de otros valores observados.

### Missing not at Random (MNAR)

Difíciles de identificar.
Debido a los límites de detección de las herramientas.
La localización de los valores faltantes en el conjunto de datos dependen de los valores faltantes en sí mismos.

__No se puede tener seguridad sobre qué mecanismo de valores faltantes es correcto para los datos.__

Sin embargo, atravez del anális, exploración y el conocimiento dirigido, se pueden hacer suposiciones razonables.
