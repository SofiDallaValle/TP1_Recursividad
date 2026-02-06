"""Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
las siguientes actividades:

a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
además mostrar el nombre de dichas películas;
b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
c. eliminar los modelos de los trajes destruidos mostrando su nombre;
d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
más de un modelo de traje, estos deben cargarse por separado;
e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
repetidos en una misma película;
f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
“Capitan America: Civil War”."""
class nodoPila:
    info, sig = None, None

class Pila:
     
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.tope
        pila.tope = nodo 
        pila.tamanio += 1

    def desapilar(pila):
        if pila.tope is None:
            return None
        x= pila.tope.info
        pila.tope = pila.tope.sig
        pila.tamanio -= 1
        return x
    
    def esta_vacia(pila):
    #Devuelve true si la pila esta vacia
        return pila.tope is None
    
    #a. Busca si el modelo fue utilizado en alguna de las película y muestra el nombre de esta.
    def buscar_modelo(pila):
        aux = Pila()
        encontrado = False

        while not pila.esta_vacia(): 
            traje = pila.desapilar()
            modelo, pelicula, estado = traje
            if modelo.lower() == "mark xliv":
                print(f"Modelo usado en: {pelicula}")
                encontrado = True

            aux.apilar(traje)
        

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
        if not encontrado:
            print("El modelo no fue utilizado")

        return encontrado
    
    #b. Busca si un modelo esta dañado y lo muestra, sin perder información.
    def daniados(pila):
        aux = Pila()

        while not pila.esta_vacia():
            traje = pila.desapilar()
            modelo, pelicula, estado= traje

            if estado.lower() == "dañado":
                print(f"Dañado: {modelo}")

            aux.apilar(traje)

        while not aux.esta_vacia(): 
            pila.apilar(aux.desapilar())

    #c. Busca si un modelo esta destruido y lo eliminar mostrando su modelo.
    def eliminar(pila):
        aux = Pila()

        while not pila.esta_vacia():
            traje = pila.desapilar()
            modelo, pelicula, estado = traje

            if estado.lower() == "destruido":
                print(f"Eliminado: {modelo}")
            else:
                aux.apilar(traje)

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())

    #e. Agrega el modelo Mark LXXXV a la pila, sin cargar modelos repetidos en una misma película.
    def agregar_sin_repetir(pila, pelicula, estado):
        aux = Pila()
        repetido = False

        while not pila.esta_vacia():
            traje = pila.desapilar()
            modelo, peli, est = traje

            if modelo.lower() == "mark lxxxv" and peli.lower() == pelicula.lower():
                repetido = True

            aux.apilar(traje)

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())

        if repetido:
            print(f"El modelo Mark LXXXV ya fue cargado en la película {pelicula}")
        else:
            pila.apilar(("Mark LXXXV", pelicula, estado))
            print(f"Modelo Mark LXXXV agregado para la película {pelicula}")

    #f. Muestra los nombres de los trajes utilizados en las películas indicadas.
    def mostrar_trajes(pila, peliculas_buscadas):
        aux = Pila()

        while not pila.esta_vacia():
            traje = pila.desapilar()
            modelo, pelicula, estado = traje

            if pelicula in peliculas_buscadas:
                print(f"Modelo: {modelo}, Película: {pelicula}")

            aux.apilar(traje)

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
            
# Para probar los puntos a-f
#d.Cada modelo, película y estado se apila como un elemento independiente.  
pila = Pila()
pila.apilar(("Mark XLIV", "Avengers: Age of Ultron", "dañado"))
pila.apilar(("Mark XLIV", "Avengers: Infinity War", "impecable"))
pila.apilar(("Mark III", "Iron Man", "impecable"))
pila.apilar(("Mark XLVI", "Capitan America: Civil War", "dañado"))
pila.apilar(("Mark XLVI", "Spider-Man: Homecoming", "impecable"))
pila.apilar(("Mark I", "Iron Man", "destruido"))


print("\n--- Punto A ---")
pila.buscar_modelo()
print("\n--- Punto B ---")
pila.daniados() 
print("\n--- Punto C ---")
pila.eliminar()
print("\n--- Punto E ---")
pila.agregar_sin_repetir("Avengers: Endgame", "impecable")
print("\n--- Punto F ---")  
peliculas = [
    "Spider-Man: Homecoming",
    "Capitan America: Civil War"
]

pila.mostrar_trajes(peliculas)
