"""Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

class nodoLista(object):
    info, sig = None, None

class Lista(object):
    def __init__(lista):
        lista.inicio = None
        lista.tamanio = 0
    
    def insertar(lista, dato):
        """Inserta un nuevo nodo al final de la lista"""
        nodo = nodoLista()
        nodo.info = dato
        if lista.inicio is None:
            lista.inicio = nodo
        else:
            aux = lista.inicio
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
        lista.tamanio += 1

    def eliminar (lista, clave):
        """Elimina un elemento de la lista y lo devuele si lo encuentra"""
        if lista.inicio is None:
            return None

        if lista.inicio.info[0].lower() == clave.lower():
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
            return dato

        anterior = lista.inicio
        actual = lista.inicio.sig

        while actual is not None and actual.info[0].lower() != clave.lower():
            anterior = actual
            actual = actual.sig

        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
            return dato

        return None

    
    def buscar(lista, buscado):
        """Devuelve la direccion del elemento buscado"""
        aux = lista.inicio
        while (aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

    #a. eliminar el nodo que contiene la información de Linterna Verde;
    def eliminar_linterna_verde(lista):
        eliminado = lista.eliminar("Linterna Verde")
        if eliminado:
            return "Linterna Verde eliminado"
        else:
            return "Linterna Verde no encontrado"

    
    #b. mostrar el año de aparición de Wolverine;
    def mostrar_ano_wolverine(lista):
        nodo = lista.buscar("Wolverine")
        if nodo is not None:
            return nodo.info[1]
        else:
            return "Wolverine no encontrado"
        
    #c. cambiar la casa de Dr. Strange a Marvel;
    def cambiar_casa_dr_strange(lista):
        nodo = lista.buscar("Dr. Strange")
        if nodo is not None:
            nodo.info[2] = "Marvel"
            return "Casa de Dr. Strange cambiada a Marvel"
        else:
            return "Dr. Strange no encontrado"
        
    #d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
    def mostrar_superheroes_con_traje_o_armadura(lista):
        aux = lista.inicio
        superheroes = []
        while aux is not None:
            if "traje" in aux.info[3].lower() or "armadura" in aux.info[3].lower():
                superheroes.append(aux.info[0])
            aux = aux.sig
        return superheroes
    
    #e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
    def mostrar_superheroes_antes_de_1963(lista):
        aux = lista.inicio
        superheroes =[]
        while aux is not None:
            if aux.info[1] < 1963:
                superheroes.append((aux.info[0], aux.info[2]))
            aux = aux.sig
        return superheroes
    
    #f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
    def mostrar_casa_capitana_marvel_y_mujer_maravilla(lista):
        aux = lista.inicio
        casas = []
        while aux is not None:
            if aux.info[0] == "Capitana Marvel" or aux.info[0] == "Mujer Maravilla":
                casas.append((aux.info[0],aux.info[2]))
            aux = aux.sig
        return casas
    
    #g. mostrar toda la información de Flash y Star-Lord;
    def mostrar_info_flash_y_star_Lord(lista):
        aux = lista.inicio
        info = []
        while aux is not None:
            if aux.info[0] == "Flash" or aux.info[0] == "Star-Lord":
                info.append(aux.info)
            aux = aux.sig
        return info
    
    #h. listar los superhéroes que comienzan con la letra B, M y S;
    def listar_superheroes_con_letra_b_m_s(lista):
        aux = lista.inicio
        superheroes = []
        while aux is not None:
            if aux.info[0][0] in ["B", "M", "S"]:
                superheroes.append(aux.info[0])
            aux = aux.sig
        return superheroes
    
    #i. determinar cuántos superhéroes hay de cada casa de comic.
    def contar_superheroes_por_casa(lista):
        aux = lista.inicio
        conteo = {"Marvel": 0, "DC": 0}
        while aux is not None:
            if aux.info[2] in conteo:
                conteo[aux.info[2]] += 1
            aux = aux.sig
        return conteo
    
    #Ejemplo de uso
lista_superheroes = Lista()
lista_superheroes.insertar(("Linterna Verde", 1940, "DC", "Usa un anillo de poder para crear objetos de luz sólida"))
lista_superheroes.insertar(("Wolverine", 1974, "Marvel", "Tiene garras retráctiles y un factor de curación acelerado"))
lista_superheroes.insertar(("Dr. Strange", 1963, "Marvel", "Es un hechicero supremo que protege la Tierra de amenazas mágicas"))
lista_superheroes.insertar(("Flash", 1940, "DC", "Puede moverse a velocidades increíbles"))
lista_superheroes.insertar(("Star-Lord", 1976, "Marvel", "Es un aventurero espacial y líder de los Guardianes de la Galaxia"))
lista_superheroes.insertar(("Capitana Marvel", 1968, "Marvel", "Tiene super fuerza, vuelo y puede disparar energía"))
lista_superheroes.insertar(("Mujer Maravilla", 1941, "DC", "Es una princesa amazona con super fuerza y habilidades de combate"))

print(lista_superheroes.eliminar_linterna_verde())
print(lista_superheroes.mostrar_ano_wolverine())
print(lista_superheroes.cambiar_casa_dr_strange())
print(lista_superheroes.mostrar_superheroes_con_traje_o_armadura())
print(lista_superheroes.mostrar_superheroes_antes_de_1963())
print(lista_superheroes.mostrar_casa_capitana_marvel_y_mujer_maravilla())
print(lista_superheroes.mostrar_info_flash_y_star_Lord())
print(lista_superheroes.listar_superheroes_con_letra_b_m_s())
print(lista_superheroes.contar_superheroes_por_casa())