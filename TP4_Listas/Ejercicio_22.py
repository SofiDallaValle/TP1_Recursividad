"""Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron."""

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
    
    def buscar(lista, clave):
        """Busca un elemento en la lista y lo devuelve si lo encuentra"""
        aux = lista.inicio
        while aux is not None:
            if aux.info[0].lower() == clave.lower():
                return aux
            aux = aux.sig
        return None
    
    def lista_vacia(lista):  
        """Devuelve True si la lista está vacía, False en caso contrario"""
        return lista.inicio is None
    
    #a. listado ordenado por nombre y por especie;
    def ordenar_por_nombre_y_especie(lista):
        """Ordena la lista por nombre y luego por especie"""
        if lista.lista_vacia():
            return []
        
        elementos = []
        aux = lista.inicio
        while aux is not None:
            elementos.append((aux.info[0], aux.info[3], aux.info))  # (nombre, especie, info)
            aux = aux.sig
        # Ordenar por nombre y luego por especie
        elementos.sort(key=lambda x: (x[0], x[1]))
        return [elemento[2] for elemento in elementos]
    
    #b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
    def mostrar_info_ahsoka_y_kit(lista):
        """Muestra toda la información de Ahsoka Tano y Kit Fisto"""
        ahsoka = lista.buscar("Ahsoka Tano")
        kit = lista.buscar("Kit Fisto")
        if ahsoka is not None:
            info_ahsoka = ahsoka.info
        else:
            info_ahsoka = "Ahsoka Tano no encontrado"
        if kit is not None:
            info_kit = kit.info
        else:
            info_kit = "Kit Fisto no encontrado"
        return info_ahsoka, info_kit
    
    #c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
    def mostrar_padawans_yoda_luke(lista):
        """Muestra todos los padawan de Yoda y Luke Skywalker"""
        padawans = []
        aux = lista.inicio
        while aux is not None:
            if "Yoda" in aux.info[1] or "Luke Skywalker" in aux.info[1]: 
                padawans.append(aux.info)
            aux = aux.sig
        return padawans
    
    #d. mostrar los Jedi de especie humana y twi'lek;
    def mostrar_jedi_humana_twilek(lista):
        """Muestra los Jedi de especie humana y twi'lek"""
        jedis = []
        aux = lista.inicio
        while aux is not None:
            if aux.info[3].lower() in ["humana", "twi'lek"]:
                jedis.append(aux.info)
            aux = aux.sig
        return jedis
    
    #e. listar todos los Jedi que comienzan con A;
    def listar_jedi_con_a(lista):
        """Lista todos los Jedi que comienzan con A"""
        jedis = []
        aux = lista.inicio
        while aux is not None:
            if aux.info[0].lower().startswith("a"):
                jedis.append(aux.info)
            aux = aux.sig
        return jedis
    
    #f. mostrar los Jedi que usaron sable de luz de más de un color;
    def mostrar_jedi_con_sable_multicolor(lista):
        """Muestra los Jedi que usaron sable de luz de más de un color"""
        jedis = []
        aux = lista.inicio
        while aux is not None:
            if len(aux.info[2]) > 1:
                jedis.append(aux.info)
            aux = aux.sig
        return jedis
    
    #g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
    def mostrar_jedi_con_sable_amarillo_violeta(lista):
        """Indica los Jedi que utilizaron sable de luz amarillo o violeta"""
        jedis = []
        aux = lista.inicio
        while aux is not None:
            colores = [c.lower() for c in aux.info[2]]
            if "amarillo" in colores or "violeta" in colores:
                jedis.append(aux.info)
            aux = aux.sig
        return jedis
    
    #h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
    def mostrar_padawans_qui_gon_mace(lista):
        """Indica los nombres de los padawans de Qui-Gon Jin y Mace Windu"""
        padawans = []
        aux = lista.inicio
        while aux is not None:
            if "Qui-Gon Jin" in aux.info[1] or "Mace Windu" in aux.info[1]:
                padawans.append(aux.info[0])  # Solo el nombre del padawan
            aux = aux.sig
        return padawans
    
#Ejermplo de uso:

lista_jedi = Lista()

lista_jedi.insertar(["Luke Skywalker",
                     ["Obi-Wan Kenobi", "Yoda"],
                     ["verde"],
                     "humana"])

lista_jedi.insertar(["Yoda",
                     [],
                     ["verde"],
                     "desconocida"])

lista_jedi.insertar(["Ahsoka Tano",
                     ["Anakin Skywalker"],
                     ["blanco", "verde"],
                     "togruta"])

lista_jedi.insertar(["Kit Fisto",
                     ["Yoda"],
                     ["verde"],
                     "nautolano"])

lista_jedi.insertar(["Qui-Gon Jin",
                     [],
                     ["verde"],
                     "humana"])

lista_jedi.insertar(["Mace Windu",
                     [],
                     ["violeta"],
                     "humana"])

print("Listado ordenado por nombre y especie:")
for jedi in lista_jedi.ordenar_por_nombre_y_especie():
    print(jedi)

print("\nInformación de Ahsoka Tano y Kit Fisto:")
info_ahsoka, info_kit = lista_jedi.mostrar_info_ahsoka_y_kit()
print(info_ahsoka)
print(info_kit)

print("\nPadawans de Yoda y Luke Skywalker:")
for padawan in lista_jedi.mostrar_padawans_yoda_luke():
    print(padawan)

print("\nJedi de especie humana y twi'lek:")
for jedi in lista_jedi.mostrar_jedi_humana_twilek():
    print(jedi)

print("\nJedi que comienzan con A:")
for jedi in lista_jedi.listar_jedi_con_a():
    print(jedi)

print("\nJedi que usaron sable de luz de más de un color:")
for jedi in lista_jedi.mostrar_jedi_con_sable_multicolor():
    print(jedi)

print("\nJedi que utilizaron sable de luz amarillo o violeta:")
for jedi in lista_jedi.mostrar_jedi_con_sable_amarillo_violeta():
    print(jedi)

print("\nPadawans de Qui-Gon Jin y Mace Windu:")
for padawan in lista_jedi.mostrar_padawans_qui_gon_mace():
    print(padawan)