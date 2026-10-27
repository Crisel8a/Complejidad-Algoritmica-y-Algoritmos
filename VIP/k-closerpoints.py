import heapq
from ast import List


def kClosest(self, puntos: List[List[int]], k: int) -> List[List[int]]:
    # Crear una lista de tuplas (distancia, punto)
    distancias = []
    for punto in puntos:
        distancia = punto[0] ** 2 + punto[1] ** 2  # Calcular la distancia al cuadrado
        distancias.append((distancia, punto))

    # Usar heapq para obtener los k puntos más cercanos
    k_cercanos = heapq.nsmallest(k, distancias)

    # Extraer solo los puntos de las tuplas
    return [punto for _, punto in k_cercanos]
