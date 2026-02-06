"""24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;

c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G."""

class nodoPila:
    info, sig = None, None

class Pila:
    def __init__(self):
        self.tope = None
        self.tamanio =0
    
    def apilar(pila,dato):
        nodo= nodoPila()
        nodo.info = dato 
        nodo.sig = pila.tope
        pila.tope = nodo
        pila.tamanio += 1

    def desapilar(pila):
        if pila.tope is None:
            return None
        x = pila.tope.info
        pila.tope = pila.tope.sig
        pila.tamanio -= 1
        return x
    
    def esta_vacia(pila):
        return pila.tope is None
    
    #a. Determina en qué posición se encuentran Rocket Raccoon y Groot.
    def posicion_rocket_groot(pila):
        aux = Pila()
        posicion = 1
        pos_rocket = -1
        pos_groot = -1

        while not pila.esta_vacia():
            personaje = pila.desapilar()
            personaje_nombre, peliculas = personaje
            if personaje_nombre.lower() == "rocket raccoon":
                pos_rocket = posicion

            if personaje_nombre.lower() == "groot":
                pos_groot = posicion

            aux.apilar(personaje)
            posicion += 1

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
        return pos_rocket, pos_groot
    
    #b. Determina los personajes que participaron en más de 5 películas.
    def personajes_mas_5_peliculas(pila):
        aux = Pila()
        personajes =[]
        while not pila.esta_vacia():
            personaje = pila.desapilar()
            personaje_nombre, peliculas = personaje
            if peliculas > 5:
                personajes.append((personaje_nombre, peliculas))
            aux.apilar(personaje)
        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
        return personajes
    
    #c. Determina en cuantas películas participo la Viuda Negra (Black Widow);
    def peliculas_black_widow(pila):
        aux = Pila()
        peliculas_black_widow = 0

        while not pila.esta_vacia():
            personaje = pila.desapilar()
            personaje_nombre, peliculas = personaje
            if personaje_nombre.lower() == "black widow":
                peliculas_black_widow = peliculas
            aux.apilar(personaje)

        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
        return peliculas_black_widow

    #d. Muestra todos los personajes cuyos nombre empiezan con C, D y G.
    def personajes_c_d_g(pila):
        aux= Pila()
        personajes = []
        while not pila.esta_vacia():
            personaje = pila.desapilar()
            personaje_nombre, peliculas = personaje
            if personaje_nombre.lower().startswith(("c", "d", "g")):
                personajes.append(personaje_nombre)
            aux.apilar(personaje)
        while not aux.esta_vacia():
            pila.apilar(aux.desapilar())
        return personajes
    
#Ejemplos de uso:
pila = Pila()

Pila.apilar(pila, ("Iron Man", 10))
Pila.apilar(pila, ("Rocket Raccoon", 6))        
Pila.apilar(pila, ("Groot", 5))
Pila.apilar(pila, ("Black Widow", 8))

print("\n--- Punto A ---")
pos_rocket, pos_groot = pila.posicion_rocket_groot()
print(f"Rocket Raccoon está en la posición: {pos_rocket}")
print(f"Groot está en la posición: {pos_groot}")
print("\n--- Punto B ---")
personajes_mas_5 = pila.personajes_mas_5_peliculas()
for personaje, peliculas in personajes_mas_5:
    print(f"{personaje} participó en {peliculas} películas.")   
print("\n--- Punto C ---")
peliculas_bw = pila.peliculas_black_widow()
print(f"La Viuda Negra participó en {peliculas_bw} películas.") 
print("\n--- Punto D ---")
personajes_c_d_g = pila.personajes_c_d_g()
print("Personajes cuyos nombres empiezan con C, D y G:")
for personaje in personajes_c_d_g:
    print(personaje)    
    