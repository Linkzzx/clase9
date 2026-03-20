import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter

def problema_1_fuerzas():
    print("--- Problema 1: Análisis de Fuerzas ---")
    # Representamos una cuadrícula 3x3 de fuerzas en el eje Y (en Newtons)
    # Valores negativos indican fuerzas hacia abajo.
    fuerzas = np.array([
        [0, -500, 0],
        [-200, -1000, -200],
        [0, -500, 0]
    ])
    
    # Cálculo de la fuerza resultante (Sumatoria de fuerzas)
    fuerza_resultante = np.sum(fuerzas)
    print(f"Matriz de fuerzas (N):\n{fuerzas}")
    print(f"Fuerza resultante en la estructura: {fuerza_resultante} N")
    
    # Asumiendo soportes en los extremos (columna 0 y columna 2)
    # Calculamos la reacción asumiendo simetría para mantener el equilibrio estático (Sumatoria F = 0)
    reaccion_por_soporte = abs(fuerza_resultante) / 2
    print(f"Reacción necesaria en cada soporte extremo para equilibrio: {reaccion_por_soporte} N\n")

def problema_2_simulacion_fluido():
    print("--- Problema 2: Simulación de Fluido 3D ---")
    # Arreglo 3x3x3 representando la presión inicial del fluido
    # Inicializamos todo en 1.0 atm, excepto el centro que tiene una perturbación (onda de presión de 5.0 atm)
    presion = np.ones((3, 3, 3))
    presion[1, 1, 1] = 5.0 
    
    print("Presión inicial (capa central Z=1):\n", presion[:, :, 1])
    
    # Simulación de propagación (1 paso de tiempo): Cada celda es el promedio de sus vecinas
    # Usamos un filtro uniforme tridimensional que hace exactamente esto
    presion_actualizada = uniform_filter(presion, size=3, mode='constant', cval=1.0)
    
    print("Presión tras propagación (capa central Z=1):\n", np.round(presion_actualizada[:, :, 1], 2), "\n")

def problema_3_imagenes_medicas():
    print("--- Problema 3: Análisis de Imágenes Médicas 3D ---")
    # Simulamos un volumen de 5x5x5 con "tejido" (valor 100) y ruido aleatorio
    volumen_original = np.random.normal(100, 20, (5, 5, 5))
    
    # Aplicamos un filtro de promedio (suavizado) capa por capa (2D)
    volumen_suavizado = np.zeros_like(volumen_original)
    for i in range(volumen_original.shape[0]):
        # Se suaviza cada "rebanada" o capa usando un kernel de 3x3
        volumen_suavizado[i] = uniform_filter(volumen_original[i], size=3)
    
    print("Capa 2 ORIGINAL (con ruido):\n", np.round(volumen_original[2], 1))
    print("Capa 2 SUAVIZADA (ruido reducido):\n", np.round(volumen_suavizado[2], 1), "\n")

def problema_4_sensores():
    print("--- Problema 4: Manejo de Datos de Sensores ---")
    # Matriz 5x5: 5 momentos en el tiempo (filas) x 5 sensores (columnas)
    # Temperaturas simuladas entre 20 y 30 grados
    datos_sensores = np.random.uniform(20, 30, (5, 5))
    
    # Promedios y Desviaciones por Sensor (Columnas, axis=0)
    promedios_sensores = np.mean(datos_sensores, axis=0)
    std_sensores = np.std(datos_sensores, axis=0)
    
    print(f"Promedio por sensor: {np.round(promedios_sensores, 2)}")
    print(f"Desviación estándar por sensor: {np.round(std_sensores, 2)}\n")
    
    # Visualización
    plt.figure(figsize=(8, 4))
    plt.imshow(datos_sensores, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Temperatura (°C)')
    plt.title('Mapa de Calor - Sensores de Temperatura')
    plt.xlabel('Sensor ID')
    plt.ylabel('Momento (Tiempo)')
    plt.show()

def problema_5_transformacion():
    print("--- Problema 5: Transformación de Coordenadas (Rectángulo) ---")
    # Definimos un conjunto de puntos formando un RECTÁNGULO (base=2, altura=1)
    # Las coordenadas (x, y) de las esquinas son:
    puntos = np.array([
        [0, 0], # Origen / Esquina inferior izquierda
        [2, 0], # Esquina inferior derecha (estiramos la base a 2)
        [2, 1], # Esquina superior derecha
        [0, 1], # Esquina superior izquierda
        [0, 0]  # Volvemos al origen para cerrar la línea de la figura
    ])
    
    # Ángulo de rotación: mantenemos 45 grados (convertidos a radianes)
    theta = np.radians(45)
    
    # Matriz de transformación lineal (Rotación 2D estándar)
    # Esta matriz no cambia, es la "operación" matemática de girar.
    matriz_rotacion = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    # Aplicar transformación (Multiplicación matricial: Puntos * Matriz Transpuesta)
    puntos_transformados = puntos.dot(matriz_rotacion.T)
    
    # Visualización
    plt.figure(figsize=(7, 7)) # Un poco más grande para apreciar el detalle
    
    # Dibujamos la figura original (Rectángulo azul)
    plt.plot(puntos[:, 0], puntos[:, 1], label='Original (Rectángulo $2\\times1$)', marker='o', linewidth=2)
    
    # Dibujamos la figura transformada (Rectángulo naranja rotado)
    plt.plot(puntos_transformados[:, 0], puntos_transformados[:, 1], label='Rotado 45°', marker='x', linestyle='--')
    
    # Configuración de los ejes cartesianos
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    
    # AJUSTE DE LÍMITES: Importante ampliar el rango para que quepa el rectángulo estirado y rotado
    plt.xlim(-1, 3)     # Ampliamos en X para la base de 2
    plt.ylim(-0.5, 2.5) # Ampliamos un poco en Y
    
    plt.legend()
    plt.title('Transformación Cartesiana: Rotación de un Rectángulo')
    plt.axis('equal') # Fundamental para que las proporciones visuales sean correctas (1:1)
    plt.show()

if __name__ == "__main__":
    problema_1_fuerzas()
    problema_2_simulacion_fluido()
    problema_3_imagenes_medicas()
    problema_4_sensores()
    problema_5_transformacion()