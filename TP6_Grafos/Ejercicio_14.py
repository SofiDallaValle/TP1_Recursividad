"""14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""

from collections import deque
import heapq

class Grafo:
    def __init__(self):
        self.aristas = {}

    def agregar_vertice(self, nombre):
        if nombre not in self.aristas:
            self.aristas[nombre] = []

    def agregar_arista(self, origen, destino, peso):
        self.aristas[origen].append((destino, peso))
        self.aristas[destino].append((origen, peso))

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.aristas}
        distancias[inicio] = 0

        heap = [(0, inicio)]

        while heap:
            dist_actual, nodo = heapq.heappop(heap)

            for vecino, peso in self.aristas[nodo]:
                nueva = dist_actual + peso
                if nueva < distancias[vecino]:
                    distancias[vecino] = nueva
                    heapq.heappush(heap, (nueva, vecino))

        return distancias

    def prim(self, inicio):
        visitados = set([inicio])
        mst = []
        heap = []

        for vecino, peso in self.aristas[inicio]:
            heapq.heappush(heap, (peso, inicio, vecino))

        while heap:
            peso, origen, destino = heapq.heappop(heap)

            if destino not in visitados:
                visitados.add(destino)
                mst.append((origen, destino, peso))

                for vecino, p in self.aristas[destino]:
                    if vecino not in visitados:
                        heapq.heappush(heap, (p, destino, vecino))

        return mst


g = Grafo()

#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho",
    "Baño 1", "Baño 2",
    "Habitación 1", "Habitación 2",
    "Sala de estar", "Terraza", "Patio"
]

for amb in ambientes:
    g.agregar_vertice(amb)

#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
#ta es la distancia entre los ambientes, se debe cargar en metros;
aristas = [
    # Cocina (5 conexiones)
    ("Cocina", "Comedor", 5),
    ("Cocina", "Baño 1", 4),
    ("Cocina", "Patio", 6),
    ("Cocina", "Sala de estar", 7),
    ("Cocina", "Cochera", 8),

    # Sala de estar (5 conexiones)
    ("Sala de estar", "Habitación 1", 4),
    ("Sala de estar", "Habitación 2", 6),
    ("Sala de estar", "Terraza", 5),
    ("Sala de estar", "Comedor", 3),

    # Otras conexiones
    ("Comedor", "Quincho", 7),
    ("Quincho", "Patio", 4),
    ("Cochera", "Patio", 5),
    ("Baño 1", "Baño 2", 3),
    ("Habitación 1", "Baño 2", 4),
    ("Habitación 2", "Terraza", 3),
]

for origen, destino, peso in aristas:
    g.agregar_arista(origen, destino, peso)


#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;
print("\n--- ÁRBOL DE EXPANSIÓN MÍNIMA ---")

mst = g.prim("Cocina")
total_metros = 0

for origen, destino, peso in mst:
    print(origen, "-", destino, ":", peso, "m")
    total_metros += peso

print("\nTotal de metros de cable necesarios:", total_metros, "m")


#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el
#Smart Tv.
print("\n--- CAMINO MÁS CORTO ---")

distancias = g.dijkstra("Habitación 1")
print("Metros desde Habitación 1 hasta Sala de estar:",
      distancias["Sala de estar"], "m")