from collections import deque

# Función para verificar si una ubicación es la ubicación "A" objetivo
def es_ubicacion_objetivo(ubicacion):
    return ubicacion == 1

# Definir una función para generar los vecinos de una ubicación
    
def generar_vecinos(ubicacion_actual):
    # Definir los límites del cuadrado de 8x8
    limite_superior = 0
    limite_inferior = 7
    limite_izquierdo = 0
    limite_derecho = 7

    # Generar vecinos moviéndose en todas las direcciones posibles
    vecinos = []

    # Movimiento hacia arriba
    if ubicacion_actual[0] > limite_superior:
        vecino_arriba = (ubicacion_actual[0] - 1, ubicacion_actual[1])
        vecinos.append(vecino_arriba)

    # Movimiento hacia abajo
    if ubicacion_actual[0] < limite_inferior:
        vecino_abajo = (ubicacion_actual[0] + 1, ubicacion_actual[1])
        vecinos.append(vecino_abajo)

    # Movimiento hacia la izquierda
    if ubicacion_actual[1] > limite_izquierdo:
        vecino_izquierda = (ubicacion_actual[0], ubicacion_actual[1] - 1)
        vecinos.append(vecino_izquierda)

    # Movimiento hacia la derecha
    if ubicacion_actual[1] < limite_derecho:
        vecino_derecha = (ubicacion_actual[0], ubicacion_actual[1] + 1)
        vecinos.append(vecino_derecha)

    return vecinos

# Se define la ubicación inicial y la ubicación objetivo
ubicacion_inicial = 12  
ubicacion_objetivo = 1  

# Inicializar una cola para la búsqueda en anchura
cola = deque()
cola.append(ubicacion_inicial)

# Realizar la búsqueda en anchura
while cola:
    ubicacion_actual = cola.popleft()  # Obtener la ubicación actual desde la cola
    if es_ubicacion_objetivo(ubicacion_actual):
        print("Ubicación objetivo encontrada:", ubicacion_actual)
        break  # Terminar la búsqueda si se encuentra la ubicación objetivo
    
    # Generar vecinos y agregarlos a la cola
    vecinos = generar_vecinos(ubicacion_actual)
    for vecino in vecinos:
        cola.append(vecino)