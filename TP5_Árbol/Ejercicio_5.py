"""5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""


class nodoArbol(object):

    def __init__(self, info):
        """Crea un nodo con la información cargada."""
        self.izq = None
        self.der = None
        self.info = info

    def eliminar_nodo(raiz,clave):
        """Elimina un elemento del arbol y lo devuelve si lo encuentra"""
        x = None
        if (raiz is not None):
            if (clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif (clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if (raiz.izq is None):
                    raiz = raiz.der
                elif (raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x
    
    def insertar_nodo(raiz,dato):
        """Inserta un dato al arbol"""
        if (raiz is None):
            raiz = nodoArbol(dato)
        elif (dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        return raiz
    
    def arbol_vacio(raiz):
        """Devuelve True si el arbol esta vacio"""
        return raiz is None

    def remplazar(raiz):
        """Determina el nodo que remplazará al que se elimina"""
        aux = None
        if (raiz.der is None):
            aux = raiz
            raiz = raiz.izq 
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux
    
    def buscar(raiz, clave):
        """Devuelve la direccion del elemento buscado"""
        pos = None
        if (raiz is not None):
            if (raiz.info == clave):
                pos = raiz
            elif (clave < raiz.info):
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        """Realiza un barrido inorden del arbol"""
        if (raiz is not None):
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        """Realiza un barrido preorden del arbol"""
        if (raiz is not None):
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        """Realiza un barrido postorden del arbol"""
        if (raiz is not None):
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

    def por_nivel(raiz):
        """Realiza un barrido por nivel del arbol"""
        if (raiz is not None):
            cola = []
            cola.arribo(raiz)
            while (not cola.cola_vacia()):
                nodo = cola.atencion()
                print(nodo.info)
                if (nodo.izq is not None):
                    cola.arribo(nodo.izq)
                if (nodo.der is not None):
                    cola.arribo(nodo.der)

    #a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo 
    # booleano que indica si es un héroe o un villano, True y False respectivamente;
    def insertar_superheroe(raiz, nombre, es_heroe):
        """Inserta un superhéroe o villano al árbol."""
        dato = (nombre, es_heroe)
        return nodoArbol.insertar_nodo(raiz, dato)

    #b. listar los villanos ordenados alfabéticamente;
    def listar_villanos(raiz):
        """Lista los villanos ordenados alfabéticamente."""
        if raiz is not None:
            nodoArbol.listar_villanos(raiz.izq)
            nombre, es_heroe = raiz.info
            if not es_heroe:
                print(nombre)
            nodoArbol.listar_villanos(raiz.der)

    #c. mostrar todos los superhéroes que empiezan con C;
    def listar_superheroes_con_c(raiz):
        """Muestra todos los superhéroes que empiezan con C."""
        if raiz is not None:
            nodoArbol.listar_superheroes_con_c(raiz.izq)
            nombre, es_heroe = raiz.info
            if es_heroe and nombre.startswith('C'):
                print(nombre)
            nodoArbol.listar_superheroes_con_c(raiz.der)

    #d. determinar cuántos superhéroes hay el árbol;
    def contar_superheroes(raiz):
        """Determina cuántos superhéroes hay en el árbol."""
        if raiz is None:
            return 0
        nombre, es_heroe = raiz.info
        count = 1 if es_heroe else 0
        count += nodoArbol.contar_superheroes(raiz.izq)
        count += nodoArbol.contar_superheroes(raiz.der)
        return count
    
    #e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
    # encontrarlo en el árbol y modificar su nombre;
    def modificar_doctor_strange(raiz, nuevo_nombre):
        """Busca por proximidad a Doctor Strange y modifica su nombre."""
        if raiz is not None:
            nombre, es_heroe = raiz.info
            if nombre == "Doctor Strange":
                raiz.info = (nuevo_nombre, es_heroe)
            nodoArbol.modificar_doctor_strange(raiz.izq, nuevo_nombre)
            nodoArbol.modificar_doctor_strange(raiz.der, nuevo_nombre)

    #f. listar los superhéroes ordenados de manera descendente;
    def listar_superheroes_descendente(raiz):
        """Lista los superhéroes ordenados de manera descendente."""
        if raiz is not None:
            nodoArbol.listar_superheroes_descendente(raiz.der)
            nombre, es_heroe = raiz.info
            if es_heroe:
                print(nombre)
            nodoArbol.listar_superheroes_descendente(raiz.izq)

    #g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
    # los villanos, luego resolver las siguiente tareas:    
    def generar_bosque(raiz):
        arbol_heroes = None
        arbol_villanos = None

        def recorrer(nodo):
            nonlocal arbol_heroes, arbol_villanos
            if nodo is not None:
                nombre, es_heroe = nodo.info
                if es_heroe:
                    arbol_heroes = nodoArbol.insertar_nodo(arbol_heroes, nodo.info)
                else:
                    arbol_villanos = nodoArbol.insertar_nodo(arbol_villanos, nodo.info)
                recorrer(nodo.izq)
                recorrer(nodo.der)

        recorrer(raiz)
        return arbol_heroes, arbol_villanos
    
    #gI. determinar cuántos nodos tiene cada árbol;
    def contar_nodos(raiz):
        """Determina cuántos nodos tiene el árbol."""
        if raiz is None:
            return 0
        return 1 + nodoArbol.contar_nodos(raiz.izq) + nodoArbol.contar_nodos(raiz.der)
    
    #gII. realizar un barrido ordenado alfabéticamente de cada árbol.
    def barrido_alfabetico(raiz):
        """Realiza un barrido ordenado alfabéticamente del árbol."""
        if raiz is not None:
            nodoArbol.barrido_alfabetico(raiz.izq)
            print(raiz.info[0])  # Imprime solo el nombre
            nodoArbol.barrido_alfabetico(raiz.der)

    #Ejemplo de uso:
raiz = None
raiz = nodoArbol.insertar_superheroe(raiz, "Iron Man", True)
raiz = nodoArbol.insertar_superheroe(raiz, "Thanos", False)
raiz = nodoArbol.insertar_superheroe(raiz, "Captain America", True)
raiz = nodoArbol.insertar_superheroe(raiz, "Loki", False)
raiz = nodoArbol.insertar_superheroe(raiz, "Doctor Strange", True)
print("Villanos ordenados alfabéticamente:")
nodoArbol.listar_villanos(raiz) 
print("\nSuperhéroes que empiezan con C:")
nodoArbol.listar_superheroes_con_c(raiz)    
print("\nCantidad de superhéroes en el árbol:")
print(nodoArbol.contar_superheroes(raiz))
print("\nModificando Doctor Strange a Stephen Strange...")
nodoArbol.modificar_doctor_strange(raiz, "Stephen Strange")
print("\nSuperhéroes ordenados de manera descendente:")
nodoArbol.listar_superheroes_descendente(raiz)
print("\nGenerando bosque...")
arbol_heroes, arbol_villanos = nodoArbol.generar_bosque(raiz)
print("\nCantidad de nodos en el árbol de héroes:")
print(nodoArbol.contar_nodos(arbol_heroes))
print("\nCantidad de nodos en el árbol de villanos:")
print(nodoArbol.contar_nodos(arbol_villanos))
