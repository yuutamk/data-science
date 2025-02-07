¡Hola a todos los futuros científicos de datos! 👋

Soy un ingeniero de ciencia de datos, y hoy vamos a embarcarnos en un viaje fascinante al mundo de la **visualización de datos**.  ¿Alguna vez te has topado con montones de números y te has sentido un poco perdido? ¡No te preocupes! La visualización de datos es como tener un superpoder que te permite transformar esos números confusos en imágenes claras y fáciles de entender.

Imagínate que eres un detective, pero en lugar de buscar pistas en la escena de un crimen, buscas patrones y secretos escondidos en los datos. La visualización de datos es tu lupa y linterna, ¡todo en uno! 🔍

En este blog, vamos a explorar cómo crear gráficos increíbles usando herramientas que están a tu alcance. No necesitas ser un artista experto, solo necesitas entender algunos conceptos básicos y tener ganas de experimentar.  Así que, ¡prepárense para convertir datos en obras de arte que cuenten historias!

**1. Visualización de Datos Básica: ¡Construyendo los Cimientos!** 🏗️

Antes de construir rascacielos de visualizaciones avanzadas, necesitamos empezar con los bloques de construcción fundamentales: los **gráficos básicos**.  Estos gráficos son como el alfabeto de la visualización de datos: una vez que los dominas, ¡puedes escribir cualquier historia con datos!

**2.1 Creación de gráficos básicos: líneas, barras, dispersión**

*   **Gráficos de Líneas: Siguiendo la Corriente de los Datos** 📈

    Imagina que estás siguiendo la temperatura a lo largo del día.  Cada hora tomas una medida y quieres ver cómo cambia la temperatura con el tiempo. ¡Un **gráfico de líneas** es perfecto para esto!  Los gráficos de líneas son geniales para mostrar **tendencias** y **cambios continuos** a lo largo del tiempo o de otra variable continua.

    **Ejemplo Didáctico:**

    Pensemos en el crecimiento de una planta de frijol que sembraste en clase.  Cada día mides la altura de la planta.  Con un gráfico de líneas, puedes ver fácilmente cómo ha ido creciendo la planta día tras día.

    ```python
    import matplotlib.pyplot as plt

    dias = [1, 2, 3, 4, 5, 6, 7] # Días desde la siembra
    altura_planta = [1, 2.5, 4, 5.5, 7, 8.5, 10] # Altura en centímetros

    plt.plot(dias, altura_planta) # Creamos el gráfico de líneas
    plt.xlabel('Días desde la siembra') # Etiqueta del eje x
    plt.ylabel('Altura de la planta (cm)') # Etiqueta del eje y
    plt.title('Crecimiento de la Planta de Frijol') # Título del gráfico
    plt.grid(True) # Añadimos una cuadrícula para facilitar la lectura
    plt.show() # Mostramos el gráfico
    ```

    [Image of Gráfico de líneas mostrando el crecimiento de la planta de frijol]

    En este gráfico, el eje horizontal (x) representa los días, y el eje vertical (y) representa la altura de la planta. La línea conecta los puntos de datos y nos muestra la tendencia del crecimiento. ¡Vemos claramente que la planta crece cada día!

*   **Gráficos de Barras: Comparando Categorías Lado a Lado** 📊

    Ahora, imagina que quieres saber cuál es tu materia favorita entre tus compañeros de clase.  Puedes preguntar a cada uno y contar cuántos prefieren matemáticas, ciencias, historia, etc.  Un **gráfico de barras** es ideal para **comparar diferentes categorías**. Cada barra representa una categoría y la altura de la barra muestra la cantidad o el valor asociado a esa categoría.

    **Ejemplo Didáctico:**

    Supongamos que encuestas a 20 compañeros de clase sobre su materia favorita y obtienes los siguientes resultados:

    *   Matemáticas: 5
    *   Ciencias: 7
    *   Historia: 3
    *   Literatura: 5

    ```python
    import matplotlib.pyplot as plt

    materias = ['Matemáticas', 'Ciencias', 'Historia', 'Literatura'] # Categorías
    cantidad_favoritos = [5, 7, 3, 5] # Cantidad de estudiantes que prefieren cada materia

    plt.bar(materias, cantidad_favoritos) # Creamos el gráfico de barras
    plt.xlabel('Materias Favoritas') # Etiqueta del eje x
    plt.ylabel('Cantidad de Estudiantes') # Etiqueta del eje y
    plt.title('Materias Favoritas de los Estudiantes') # Título del gráfico
    plt.show() # Mostramos el gráfico
    ```

    [Image of Gráfico de barras mostrando las materias favoritas de los estudiantes]

    Aquí, cada barra representa una materia, y la altura de la barra nos dice cuántos estudiantes la prefieren.  ¡Vemos rápidamente que Ciencias es la materia más popular en este grupo!

*   **Gráficos de Dispersión: Buscando Relaciones entre Puntos** 散点图

    Finalmente, piensa en si existe alguna relación entre las horas que estudias para un examen y la nota que obtienes.  Si recopilas datos de tus compañeros sobre sus horas de estudio y sus notas, puedes usar un **gráfico de dispersión** para investigar si hay una **relación** entre estas dos variables.  En un gráfico de dispersión, cada punto representa un dato individual, y la posición del punto en el gráfico nos muestra los valores de dos variables para ese dato.

    **Ejemplo Didáctico:**

    Recopilemos datos de 10 estudiantes sobre las horas que estudiaron para un examen y la nota que obtuvieron (en una escala de 0 a 10):

    *   Estudiante 1: 2 horas, Nota 5
    *   Estudiante 2: 3 horas, Nota 6
    *   Estudiante 3: 4 horas, Nota 7
    *   Estudiante 4: 5 horas, Nota 8
    *   Estudiante 5: 6 horas, Nota 9
    *   Estudiante 6: 2.5 horas, Nota 6
    *   Estudiante 7: 3.5 horas, Nota 7
    *   Estudiante 8: 4.5 horas, Nota 8
    *   Estudiante 9: 5.5 horas, Nota 9
    *   Estudiante 10: 1 hora, Nota 4

    ```python
    import matplotlib.pyplot as plt

    horas_estudio = [2, 3, 4, 5, 6, 2.5, 3.5, 4.5, 5.5, 1] # Horas de estudio
    notas_examen = [5, 6, 7, 8, 9, 6, 7, 8, 9, 4] # Notas en el examen

    plt.scatter(horas_estudio, notas_examen) # Creamos el gráfico de dispersión
    plt.xlabel('Horas de Estudio') # Etiqueta del eje x
    plt.ylabel('Nota en el Examen') # Etiqueta del eje y
    plt.title('Relación entre Horas de Estudio y Notas en el Examen') # Título del gráfico
    plt.grid(True) # Añadimos una cuadrícula para facilitar la lectura
    plt.show() # Mostramos el gráfico
    ```

    [Image of Gráfico de dispersión mostrando la relación entre horas de estudio y notas en el examen]

    Cada punto en este gráfico representa a un estudiante.  La posición horizontal del punto muestra las horas de estudio, y la posición vertical muestra la nota.  Al observar el gráfico, podemos ver que **a medida que aumentan las horas de estudio, generalmente las notas también tienden a aumentar**. ¡Parece haber una relación positiva!

**2.2 Personalización de gráficos: ¡Añadiendo Estilo y Claridad!** 🎨

Crear gráficos básicos es genial, pero personalizarlos los hace aún mejores. La **personalización** te permite hacer que tus gráficos sean más informativos, atractivos y fáciles de entender.  ¡Es como ponerle accesorios a tu gráfico para que brille! ✨

Podemos personalizar nuestros gráficos de muchas maneras, pero vamos a enfocarnos en tres aspectos clave: **colores**, **etiquetas** y **estilos**.

*   **Colores: ¡Dando Vida a tus Datos!** 🌈

    Los colores pueden hacer que tus gráficos sean más atractivos y también pueden ayudarte a resaltar información importante.  Puedes usar diferentes colores para distinguir entre categorías en un gráfico de barras, para enfatizar diferentes líneas en un gráfico de líneas o para mostrar diferentes grupos de puntos en un gráfico de dispersión.

    **Ejemplo:**

    Volvamos al gráfico de barras de materias favoritas.  Podríamos usar diferentes colores para cada barra para hacer el gráfico más visualmente atractivo.

    ```python
    import matplotlib.pyplot as plt

    materias = ['Matemáticas', 'Ciencias', 'Historia', 'Literatura']
    cantidad_favoritos = [5, 7, 3, 5]
    colores = ['skyblue', 'lightcoral', 'lightgreen', 'lightsalmon'] # Lista de colores

    plt.bar(materias, cantidad_favoritos, color=colores) # Añadimos el argumento 'color'
    plt.xlabel('Materias Favoritas')
    plt.ylabel('Cantidad de Estudiantes')
    plt.title('Materias Favoritas de los Estudiantes (con colores)')
    plt.show()
    ```

    [Image of Gráfico de barras de materias favoritas con diferentes colores para cada barra]

    ¡Ahora cada barra tiene su propio color!  Puedes elegir los colores que más te gusten o que mejor se adapten a tus datos.

*   **Etiquetas: ¡Guiando al Lector!** 🏷️

    Las etiquetas son como letreros en un mapa.  Le dicen al lector qué representa cada parte del gráfico.  Necesitas etiquetas para:

    *   **Título del gráfico:**  Describe de qué trata el gráfico en general.
    *   **Etiquetas de los ejes (x e y):**  Indican qué variable se representa en cada eje.
    *   **Leyenda (si es necesario):**  Explica qué representa cada color o símbolo en el gráfico.

    Ya hemos usado etiquetas en los ejemplos anteriores, ¡pero siempre es bueno recordarlo!  **Un gráfico sin etiquetas es como un mapa sin nombres de calles**.

*   **Estilos: ¡Afinando los Detalles!** ✨

    Los estilos te permiten ajustar la apariencia general de tu gráfico.  Puedes cambiar:

    *   **El estilo de línea:**  Sólida, punteada, discontinua, etc.
    *   **El tipo de marcador (para gráficos de líneas y dispersión):**  Círculos, cuadrados, triángulos, etc.
    *   **El grosor de las líneas.**
    *   **El fondo del gráfico.**
    *   **¡Y mucho más!**

    **Ejemplo:**

    Vamos a personalizar el gráfico de líneas del crecimiento de la planta de frijol.  Podríamos cambiar el estilo de línea, añadir marcadores en los puntos de datos y hacer la línea más gruesa.

    ```python
    import matplotlib.pyplot as plt

    dias = [1, 2, 3, 4, 5, 6, 7]
    altura_planta = [1, 2.5, 4, 5.5, 7, 8.5, 10]

    plt.plot(dias, altura_planta, linestyle='--', marker='o', linewidth=2, color='purple') # Personalizamos la línea
    plt.xlabel('Días desde la siembra')
    plt.ylabel('Altura de la planta (cm)')
    plt.title('Crecimiento de la Planta de Frijol (Personalizado)')
    plt.grid(True)
    plt.show()
    ```

    [Image of Gráfico de líneas del crecimiento de la planta de frijol personalizado con estilo de línea, marcadores y grosor]

    ¡Ahora la línea es discontinua, tiene marcadores circulares en cada punto y es de color púrpura y más gruesa!  ¡Experimenta con diferentes estilos para encontrar los que más te gusten!

**¡Felicidades!**  Has aprendido los conceptos básicos de la visualización de datos y cómo crear y personalizar gráficos básicos.  ¡Ahora estás listo para explorar visualizaciones más avanzadas!

**3. Visualización Avanzada: ¡Elevando el Nivel!** 🚀

Ahora que dominamos los gráficos básicos, vamos a subir de nivel y explorar algunas visualizaciones más sofisticadas que nos permiten entender los datos desde diferentes perspectivas.

**3.1 Gráficos de distribuciones y relaciones (histogramas, boxplots, pairplots)**

*   **Histogramas: Revelando la Forma de los Datos** 📊

    Imagina que tienes las notas de todos los estudiantes de tu clase en un examen.  Quieres saber **cómo se distribuyen las notas**: ¿muchos estudiantes obtuvieron notas altas, bajas o la mayoría se concentró en el medio?  Un **histograma** es perfecto para visualizar la **distribución de una sola variable numérica**.  Divide los datos en "bins" (intervalos) y muestra la frecuencia (cantidad) de datos que caen en cada bin.  La forma del histograma nos revela la distribución de los datos.

    **Ejemplo Didáctico:**

    Supongamos que tienes las notas de 30 estudiantes en un examen (de 0 a 10):

    ```python
    import matplotlib.pyplot as plt
    import numpy as np # Importamos numpy para generar datos aleatorios

    notas_examen = np.random.normal(loc=7, scale=1.5, size=30) # Generamos notas aleatorias con media 7 y desviación estándar 1.5
    notas_examen = np.clip(notas_examen, 0, 10) # Aseguramos que las notas estén entre 0 y 10 (recortamos los valores fuera de rango)

    plt.hist(notas_examen, bins=10, edgecolor='black', color='skyblue') # Creamos el histograma, 10 bins, borde negro, color celeste
    plt.xlabel('Notas del Examen')
    plt.ylabel('Frecuencia (Cantidad de Estudiantes)')
    plt.title('Distribución de Notas del Examen (Histograma)')
    plt.show()
    ```

    [Image of Histograma mostrando la distribución de notas del examen]

    En este histograma, el eje horizontal representa las notas del examen, divididas en intervalos (bins). El eje vertical representa la frecuencia, es decir, cuántos estudiantes obtuvieron notas en cada intervalo.  La forma del histograma nos muestra cómo se distribuyen las notas.  Podemos ver si la distribución es simétrica, sesgada a la izquierda o a la derecha, etc.

*   **Boxplots (Diagramas de Caja y Bigotes): Comparando Distribuciones entre Grupos** 📦

    Ahora, imagina que quieres comparar las notas del examen entre dos clases diferentes, por ejemplo, la Clase A y la Clase B.  Un **boxplot** (o diagrama de caja y bigotes) es ideal para **comparar la distribución de una variable numérica entre diferentes grupos o categorías**.  Muestra la mediana, los cuartiles (percentiles 25% y 75%) y los valores atípicos (outliers) de cada grupo.  ¡Es como un resumen visual rápido de la distribución de cada grupo!

    **Ejemplo Didáctico:**

    Supongamos que tienes las notas del examen para la Clase A y la Clase B:

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    notas_clase_A = np.random.normal(loc=7, scale=1.2, size=25) # Notas aleatorias para Clase A
    notas_clase_A = np.clip(notas_clase_A, 0, 10)
    notas_clase_B = np.random.normal(loc=6.5, scale=1.8, size=25) # Notas aleatorias para Clase B
    notas_clase_B = np.clip(notas_clase_B, 0, 10)

    plt.boxplot([notas_clase_A, notas_clase_B], labels=['Clase A', 'Clase B']) # Creamos el boxplot, etiquetas para cada caja
    plt.ylabel('Notas del Examen')
    plt.title('Comparación de Notas entre Clases (Boxplot)')
    plt.show()
    ```

    [Image of Boxplot comparando las notas del examen entre la Clase A y la Clase B]

    Cada caja en el boxplot representa una clase (Clase A y Clase B).  La línea dentro de la caja es la mediana (el valor central).  La caja representa el rango intercuartílico (IQR), que contiene el 50% central de los datos.  Los "bigotes" se extienden desde la caja y muestran la dispersión de los datos.  Los puntos fuera de los bigotes podrían ser valores atípicos.  Con un boxplot, podemos comparar rápidamente las distribuciones de notas entre las dos clases y ver si hay diferencias significativas.

*   **Pairplots (Gráficos de Pares): Explorando Relaciones Múltiples a la Vez** 🧩

    Cuando tienes un conjunto de datos con muchas variables, puede ser interesante explorar las **relaciones entre todas las posibles parejas de variables**.  Un **pairplot** (o gráfico de pares) es una herramienta poderosa para visualizar estas relaciones **de forma conjunta**.  Para cada pareja de variables en tu conjunto de datos, un pairplot muestra un gráfico de dispersión (si ambas variables son numéricas) o un histograma (si es la relación de una variable consigo misma en la diagonal).  ¡Es como tener una visión general de todas las posibles relaciones entre tus variables!

    **Ejemplo Didáctico:**

    Imagina que tienes datos de estudiantes con información sobre sus horas de estudio, horas de sueño y notas en un examen.  Quieres explorar si existen relaciones entre estas tres variables.

    ```python
    import seaborn as sns # Importamos la librería seaborn para pairplots
    import pandas as pd # Importamos pandas para crear un DataFrame

    # Datos de ejemplo (simulados)
    data = {'Horas de Estudio': np.random.uniform(1, 6, 50), # 50 valores aleatorios entre 1 y 6
            'Horas de Sueño': np.random.uniform(6, 9, 50), # 50 valores aleatorios entre 6 y 9
            'Notas': np.random.normal(loc=7, scale=1.5, size=50)} # 50 notas aleatorias

    df = pd.DataFrame(data) # Creamos un DataFrame de pandas

    sns.pairplot(df) # Creamos el pairplot a partir del DataFrame
    plt.suptitle('Pairplot de Horas de Estudio, Sueño y Notas', y=1.02) # Título general del pairplot
    plt.show()
    ```

    [Image of Pairplot mostrando las relaciones entre horas de estudio, horas de sueño y notas]

    En este pairplot, cada gráfico fuera de la diagonal es un gráfico de dispersión que muestra la relación entre un par de variables.  Por ejemplo, el gráfico en la primera fila y segunda columna muestra la relación entre 'Horas de Estudio' (eje y) y 'Horas de Sueño' (eje x).  Los gráficos en la diagonal son histogramas que muestran la distribución de cada variable individual.  Con un pairplot, podemos explorar rápidamente todas las relaciones entre las variables en nuestro conjunto de datos y buscar patrones interesantes.

**3.2 Gráficos categóricos y de tiempo**

*   **Gráficos Categóricos: Explorando Categorías en Detalle** 📊

    Ya vimos los gráficos de barras para comparar categorías.  Pero hay otros tipos de gráficos categóricos que pueden ser útiles para explorar categorías de diferentes maneras.  Algunos ejemplos incluyen:

    *   **Countplots (Gráficos de Conteo):**  Similar a un histograma, pero para variables categóricas.  Muestra la frecuencia de cada categoría.
    *   **Pie Charts (Gráficos de Torta o Pastel):**  Muestra las proporciones de diferentes categorías como "rebanadas" de un círculo.  **¡Ojo!** Los pie charts pueden ser engañosos si hay muchas categorías o si las proporciones son muy similares.  A menudo, los gráficos de barras son una mejor opción para comparar categorías.

    **Ejemplo Didáctico (Countplot):**

    Supongamos que tienes datos sobre el color de ojos de un grupo de personas.  Quieres ver cuántas personas tienen ojos azules, marrones, verdes, etc.  Un countplot es perfecto para esto.

    ```python
    import seaborn as sns
    import matplotlib.pyplot as plt

    colores_ojos = ['Marrones', 'Azules', 'Verdes', 'Marrones', 'Marrones', 'Azules', 'Marrones', 'Verdes', 'Marrones', 'Marrones'] # Lista de colores de ojos

    sns.countplot(x=colores_ojos) # Creamos el countplot, eje x = colores de ojos
    plt.xlabel('Color de Ojos')
    plt.ylabel('Cantidad de Personas')
    plt.title('Distribución de Color de Ojos (Countplot)')
    plt.show()
    ```

    [Image of Countplot mostrando la distribución de color de ojos]

    El countplot muestra la cantidad de personas para cada color de ojos.  Es una forma rápida de visualizar la frecuencia de cada categoría.

*   **Gráficos de Tiempo: El Tiempo como Eje Central** ⏳

    Ya hablamos de gráficos de líneas para mostrar tendencias a lo largo del tiempo.  Cuando los datos tienen una **componente temporal** (fechas, horas, etc.), los gráficos de tiempo son esenciales.  Los gráficos de líneas son el tipo más común de gráfico de tiempo, pero también puedes usar otros tipos, dependiendo de lo que quieras visualizar.

    **Ejemplo Didáctico (Gráfico de Líneas de Tiempo):**

    Imagina que estás registrando la temperatura cada día durante un mes.  Quieres ver cómo cambia la temperatura a lo largo del tiempo y si hay alguna tendencia estacional.

    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    fechas = pd.date_range(start='2024-01-01', end='2024-01-31') # Creamos un rango de fechas para enero de 2024
    temperaturas = np.random.uniform(10, 25, len(fechas)) # Generamos temperaturas aleatorias entre 10 y 25 grados

    plt.plot(fechas, temperaturas) # Creamos el gráfico de líneas de tiempo, eje x = fechas
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperaturas Diarias en Enero de 2024 (Gráfico de Tiempo)')
    plt.gcf().autofmt_xdate() # Formateamos las fechas en el eje x para que se lean mejor
    plt.show()
    ```

    [Image of Gráfico de líneas de tiempo mostrando las temperaturas diarias en enero de 2024]

    En este gráfico de tiempo, el eje horizontal es el tiempo (fechas), y el eje vertical es la temperatura.  La línea muestra cómo cambia la temperatura a lo largo del tiempo.  Los gráficos de tiempo son fundamentales para analizar datos que evolucionan con el tiempo, como series temporales, tendencias, estacionalidad, etc.

**3.3 Mapas de calor y gráficos de correlación**

*   **Mapas de Calor: Visualizando la Intensidad en Dos Dimensiones** 🔥

    Imagina que tienes una tabla con datos en filas y columnas, y quieres visualizar la **intensidad** de los valores en cada celda de la tabla.  Un **mapa de calor** es perfecto para esto.  Representa los valores numéricos como colores en una cuadrícula bidimensional.  Los colores más intensos suelen representar valores más altos, y los colores menos intensos representan valores más bajos.  Los mapas de calor son útiles para visualizar patrones, concentraciones y relaciones en datos tabulares.

    **Ejemplo Didáctico (Mapa de Calor de Correlación):**

    Un uso común de los mapas de calor es visualizar **matrices de correlación**.  La correlación mide qué tan relacionadas están dos variables entre sí.  Una correlación positiva alta significa que cuando una variable aumenta, la otra también tiende a aumentar.  Una correlación negativa alta significa que cuando una variable aumenta, la otra tiende a disminuir.  Una correlación cercana a cero significa que no hay mucha relación lineal.

    ```python
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt

    # Datos de ejemplo (simulados, como en el pairplot)
    data = {'Horas de Estudio': np.random.uniform(1, 6, 50),
            'Horas de Sueño': np.random.uniform(6, 9, 50),
            'Notas': np.random.normal(loc=7, scale=1.5, size=50)}
    df = pd.DataFrame(data)

    correlacion_matriz = df.corr() # Calculamos la matriz de correlación del DataFrame

    sns.heatmap(correlacion_matriz, annot=True, cmap='coolwarm', center=0) # Creamos el mapa de calor
    plt.title('Mapa de Calor de Correlación entre Variables')
    plt.show()
    ```

    [Image of Mapa de calor de correlación entre horas de estudio, horas de sueño y notas]

    En este mapa de calor, cada celda representa la correlación entre dos variables.  El color de la celda y el valor numérico dentro de la celda indican la fuerza y dirección de la correlación.  Colores más cálidos (rojos) indican correlaciones positivas, colores más fríos (azules) indican correlaciones negativas, y colores cercanos al blanco indican correlaciones cercanas a cero.  El argumento `annot=True` muestra los valores numéricos de correlación en cada celda. `cmap='coolwarm'` elige una paleta de colores "frío-cálido", y `center=0` centra la paleta en el valor 0 (correlación nula).

**¡Enhorabuena!** Has llegado al final de este viaje por la visualización de datos.  Hemos cubierto desde gráficos básicos hasta técnicas más avanzadas como histogramas, boxplots, pairplots, gráficos de tiempo, gráficos categóricos y mapas de calor.  ¡Ahora tienes un conjunto de herramientas poderosas para explorar y comunicar tus datos de manera visual!

**Conclusión: ¡Visualiza, Explora y Descubre!** 🌟

La visualización de datos es una habilidad esencial en el mundo actual, donde estamos rodeados de datos por todas partes.  Desde entender las tendencias en redes sociales hasta analizar resultados de experimentos científicos, la visualización de datos nos permite **descubrir patrones, obtener insights y comunicar nuestras ideas de forma clara y efectiva**.

¡Te animo a seguir explorando y experimentando con diferentes tipos de gráficos y técnicas de visualización!  Hay muchas más herramientas y opciones disponibles, y la mejor manera de aprender es **practicar y aplicar estos conceptos a tus propios datos y proyectos**.

Recuerda: **¡Un buen gráfico vale más que mil números!** 😉

¡Hasta la próxima aventura de datos!  📊🚀