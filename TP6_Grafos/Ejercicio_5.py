"""5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
sarios para resolver las tareas, listadas a continuación:

a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
dor, router, switch, impresora;
b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
Red Hat, Debian, Arch;
c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
Red Hat, Fedora hasta la impresora;
d. encontrar el árbol de expansión mínima;
e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
f. indicar desde que computadora del switch 01 es el camino más corto
al servidor “MongoDB”;
g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
h. debe utilizar un grafo no dirigido."""

from collections import deque
import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}      
        self.aristas = {}       
 
    def agregar_vertice(self, nombre, tipo):
        if nombre not in self.vertices:
            self.vertices[nombre] = tipo
            self.aristas[nombre] = []

    #h. debe utilizar un grafo no dirigido.
    def agregar_arista(self, origen, destino, peso):
        self.aristas[origen].append((destino, peso))
        self.aristas[destino].append((origen, peso))

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()

        print(inicio)
        visitados.add(inicio)

        for vecino, _ in self.aristas[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)

        while cola:
            nodo = cola.popleft()
            print(nodo)

            for vecino, _ in self.aristas[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0

        heap = [(0, inicio)]

        while heap:
            dist_actual, nodo = heapq.heappop(heap)

            for vecino, peso in self.aristas[nodo]:
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    heapq.heappush(heap, (nueva_dist, vecino))

        return distancias

    def prim(self, inicio):
        visitados = set([inicio])
        aristas_mst = []
        heap = []

        for vecino, peso in self.aristas[inicio]:
            heapq.heappush(heap, (peso, inicio, vecino))

        while heap:
            peso, origen, destino = heapq.heappop(heap)

            if destino not in visitados:
                visitados.add(destino)
                aristas_mst.append((origen, destino, peso))

                for vecino, p in self.aristas[destino]:
                    if vecino not in visitados:
                        heapq.heappush(heap, (p, destino, vecino))

        return aristas_mst


g = Grafo()

nodos = [
    ("Red Hat", "notebook"),
    ("Debian", "notebook"),
    ("Arch", "notebook"),
    ("Ubuntu", "pc"),
    ("Mint", "pc"),
    ("Manjaro", "pc"),
    ("Fedora", "pc"),
    ("Parrot", "pc"),
    ("Guarani", "servidor"),
    ("MongoDB", "servidor"),
    ("Impresora", "impresora"),
    ("Switch 1", "switch"),
    ("Switch 2", "switch"),
    ("Router 1", "router"),
    ("Router 2", "router"),
    ("Router 3", "router"),
]

#a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
#dor, router, switch, impresora;
for nombre, tipo in nodos:
    g.agregar_vertice(nombre, tipo)

aristas = [
    ("Red Hat", "Router 2", 25),
    ("Guarani", "Router 2", 9),
    ("Router 2", "Router 3", 50),
    ("Router 2", "Router 1", 37),
    ("Router 1", "Router 3", 43),
    ("Router 3", "Switch 2", 61),
    ("Switch 2", "Manjaro", 40),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "MongoDB", 5),
    ("Switch 2", "Arch", 56),
    ("Switch 2", "Fedora", 3),
    ("Switch 1", "Router 1", 29),
    ("Switch 1", "Debian", 17),
    ("Switch 1", "Ubuntu", 18),
    ("Switch 1", "Impresora", 22),
    ("Switch 1", "Mint", 80),
]

for origen, destino, peso in aristas:
    g.agregar_arista(origen, destino, peso)

#b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
#Red Hat, Debian, Arch;
print("\n--- BARRIDO DFS ---")

for notebook in ["Red Hat", "Debian", "Arch"]:
    print(f"\nDFS desde {notebook}:")
    g.dfs(notebook)

print("\n--- BARRIDO BFS ---")

for notebook in ["Red Hat", "Debian", "Arch"]:
    print(f"\nBFS desde {notebook}:")
    g.bfs(notebook)


#c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
#Red Hat, Fedora hasta la impresora;
print("\n--- CAMINO MÁS CORTO A IMPRESORA ---")
for pc in ["Manjaro", "Red Hat", "Fedora"]:
    dist = g.dijkstra(pc)
    print(pc, "-> Impresora:", dist["Impresora"])

#d. encontrar el árbol de expansión mínima;
print("\n--- ÁRBOL DE EXPANSIÓN MÍNIMA ---")
mst = g.prim("Router 1")
for arista in mst:
    print(arista)

#e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
print("\n--- PC MÁS CERCANA A GUARANI ---")
menor = float('inf')
mejor_pc = None

for nodo, tipo in g.vertices.items():
    if tipo == "pc":
        dist = g.dijkstra(nodo)
        if dist["Guarani"] < menor:
            menor = dist["Guarani"]
            mejor_pc = nodo

print("La PC más cercana a Guarani es:", mejor_pc)

#f. indicar desde que computadora del switch 01 es el camino más corto
#al servidor “MongoDB”;
print("\n--- DESDE SWITCH 1 A MongoDB ---")

mejor = float('inf')
mejor_equipo = None

for vecino, _ in g.aristas["Switch 1"]:
    if g.vertices[vecino] in ["pc", "notebook"]:
        dist = g.dijkstra(vecino)
        if dist["MongoDB"] < mejor:
            mejor = dist["MongoDB"]
            mejor_equipo = vecino

print("Equipo más cercano a MongoDB:", mejor_equipo)

#g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
print("\n--- CAMBIO DE CONEXIÓN IMPRESORA ---")

# eliminamos conexión con Switch 1
g.aristas["Switch 1"] = [x for x in g.aristas["Switch 1"] if x[0] != "Impresora"]
g.aristas["Impresora"] = [x for x in g.aristas["Impresora"] if x[0] != "Switch 1"]

# nueva conexión
g.agregar_arista("Impresora", "Router 2", 22)

print("\n--- BARRIDO DFS ---")

for notebook in ["Red Hat", "Debian", "Arch"]:
    print(f"\nDFS desde {notebook}:")
    g.dfs(notebook)

print("\n--- BARRIDO BFS ---")

for notebook in ["Red Hat", "Debian", "Arch"]:
    print(f"\nBFS desde {notebook}:")
    g.bfs(notebook)
