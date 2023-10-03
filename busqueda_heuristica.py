import heapq

# Definir la función de costo real entre dos ubicaciones vecinas (en este caso, todas las transiciones tienen el mismo costo)
def costo_transicion(ubicacion_actual, ubicacion_vecina):
    return 1

# Definir la función de heurística (distancia Manhattan) para estimar el costo restante desde una ubicación a la ubicación objetivo
def heuristica(ubicacion_actual, ubicacion_objetivo):
    return abs(ubicacion_actual[0] - ubicacion_objetivo[0]) + abs(ubicacion_actual[1] - ubicacion_objetivo[1])

# Función para encontrar el camino utilizando A*
def buscar_camino(ubicacion_inicial, ubicacion_objetivo):
    # Inicializar la lista de nodos abiertos con la ubicación inicial
    nodos_abiertos = [(0, ubicacion_inicial)]  # (costo_total, ubicacion)
    # Inicializar la lista de nodos cerrados
    nodos_cerrados = set()
    # Diccionario para realizar un seguimiento de los padres de cada ubicación
    padres = {}
    
    while nodos_abiertos:
        # Obtener el nodo con el costo total mínimo
        costo_actual, ubicacion_actual = heapq.heappop(nodos_abiertos)
        
        # Verificar si llegamos a la ubicación objetivo
        if ubicacion_actual == ubicacion_objetivo:
            # Reconstruir el camino desde la ubicación objetivo hasta la inicial
            camino = [ubicacion_actual]
            while ubicacion_actual in padres:
                ubicacion_actual = padres[ubicacion_actual]
                camino.insert(0, ubicacion_actual)
            return camino
        
        # Marcar la ubicación actual como visitada
        nodos_cerrados.add(ubicacion_actual)
        
        # Generar vecinos y calcular sus costos
        for vecino in generar_vecinos(ubicacion_actual):
            if vecino in nodos_cerrados:
                continue
            
            costo_vecino = costo_actual + costo_transicion(ubicacion_actual, vecino)
            
            # Verificar si el vecino ya está en la lista de nodos abiertos y si tiene un costo menor
            encontrado = False
            for i, (costo, ubic) in enumerate(nodos_abiertos):
                if ubic == vecino and costo > costo_vecino:
                    nodos_abiertos[i] = (costo_vecino, vecino)
                    padres[vecino] = ubicacion_actual
                    encontrado = True
                    break
            
            if not encontrado:
                heapq.heappush(nodos_abiertos, (costo_vecino + heuristica(vecino, ubicacion_objetivo), vecino))
                padres[vecino] = ubicacion_actual
    
    return None  # No se encontró un camino

# Función para generar vecinos dentro de los límites del cuadrado de 8x8
def generar_vecinos(ubicacion_actual):
    vecinos = []
    fila, columna = ubicacion_actual
    for fila_vecina in range(fila - 1, fila + 2):
        for columna_vecina in range(columna - 1, columna + 2):
            if 0 <= fila_vecina <= 7 and 0 <= columna_vecina <= 7:
                vecinos.append((fila_vecina, columna_vecina))
    return vecinos

# Definir ubicación inicial y ubicación objetivo
ubicacion_inicial = (0, 0)  # Por ejemplo, ubicación inicial en (0, 0)
ubicacion_objetivo = (7, 7)  # Por ejemplo, ubicación objetivo en (7, 7)

# Encontrar el camino utilizando A*
camino = buscar_camino(ubicacion_inicial, ubicacion_objetivo)

# Imprimir el camino encontrado
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")