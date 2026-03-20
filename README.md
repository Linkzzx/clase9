# Tarea: Aplicación de Arreglos Multidimensionales en Ingeniería

Este repositorio contiene el código fuente con mis soluciones para los 5 problemas prácticos de la tarea. Para resolverlos, decidí utilizar **Python**, apoyándome principalmente en la librería `numpy` para manejar las matrices y `matplotlib` para hacer las gráficas como explicaba el video de esta clase.

## Descripción de las Soluciones

Aquí explico brevemente cómo abordé cada problema:

- **Problema 1 (Fuerzas en una Estructura):** Representé la estructura de 3x3 como una matriz bidimensional. En lugar de sumar celda por celda a mano, usé una función de NumPy para sumar todas las fuerzas de golpe y así obtener la fuerza resultante. Luego, dividí ese valor para calcular la reacción necesaria en los soportes y mantener el equilibrio.
- **Problema 2 (Simulación de Fluido 3D):** Creé un "cubo" de datos de 3x3x3 para representar el espacio. Puse una presión alta en el centro y, para simular cómo se expande la onda, usé un filtro que calcula el promedio de las celdas vecinas. Esto actualiza el estado del fluido en un solo paso.
- **Problema 3 (Imágenes Médicas 3D):** Simulé un volumen de imágenes médicas con un poco de "ruido" aleatorio. Para limpiarlo, hice un ciclo que recorre el volumen capa por capa (como si fueran hojas ojeadas) y le apliqué un filtro de promedio a cada capa 2D para suavizar la imagen.
- **Problema 4 (Tabla de Sensores):** Usé una matriz de 5x5 donde las filas son el tiempo y las columnas son los sensores. Usando las funciones matemáticas de la librería, calculé el promedio y la desviación estándar indicándole que lo haga por columnas (por sensor). Al final, lo mostré todo en un mapa de calor para que sea más fácil de entender visualmente.

* **Problema 5 (Transformación de Coordenadas):** Guardé las coordenadas (x, y) de un rectángulo en una matriz. Para girarlo 45 grados, creé una matriz de rotación usando senos y cosenos:

  R = | cos(45°) -sin(45°) |
  | sin(45°) cos(45°) |

  Luego, multipliqué la matriz de los puntos por esta matriz de rotación, lo que me dio las nuevas coordenadas exactas del rectángulo ya inclinado.

## Enfoque Utilizado y Eficiencia

**Mi enfoque principal fue evitar el uso excesivo de ciclos `for`.** Cuando trabajamos con matrices o arreglos de varias dimensiones, la primera solución que se me venía a la mente era usar algunos ciclos for anidados, pero claro, con lo revisado en las últimas clases esto termina siendo poco eficiente y hace que el programa se vuelva más lento.

**¿Cómo influye esto en la eficiencia?**
Al utilizar `numpy`, pude aplicar lo que se conoce como "operaciones vectorizadas". Esto significa que le digo a Python que haga sumas, promedios o multiplicaciones sobre toda la matriz al mismo tiempo y de esa forma se aprovecha algo ya creado y propio de python.

Esto mejora la eficiencia de dos maneras:

1.  **Código más limpio:** Son menos líneas de código, lo que hace que sea más fácil de leer, entender y encontrar errores.
2.  **Mayor velocidad:** Al hacer las operaciones matemáticas de golpe sobre los arreglos completos, el programa se ejecuta muchísimo más rápido que si la computadora tuviera que procesar número por número.

## Instrucciones para ejecutar el código

Al margen de tener lo básico instalado, utilicé algunas librerías adicionales y para que el código funcione habría que instalarlas de la siguiente forma: `pip install numpy matplotlib scipy`
