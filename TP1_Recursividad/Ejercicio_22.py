"""
22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila.
"""
def usar_la_fuerza(mochila, objetos_sacados=0):
# Si no hay objetos en la mochila
    if len(mochila) == 0:
        return False, objetos_sacados
    
# Si el primer objeto es el sable
    if mochila[0] == "sable de luz":
        return True, objetos_sacados + 1
# Si no es el primer objeto, vuelve a llamar a la función con los siguientes objetos de la mochila
# y suma 1 a los objetos sacados
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)


# Para probarlo 

# Creo un vector y pido al usuario que ingrese los objetos que iran dentro 
mochila = []
print("Ingresá objetos en la mochila (escribí 'fin' para terminar):")

while True:
# Espera que el usuario escriba algo y lo convierte a minúscula
    objeto = input("> ").lower()
#Si el usuario escribe "fin" utilizo break y paro el while
    if objeto == "fin":
        break
# Si no escribio "fin" se agrega el objeto a la lista mochila
    mochila.append(objeto)

encontrado, cantidad = usar_la_fuerza(mochila)
# Si el valor de encontro es true entonces imprime que se encontro y cuantos objetos saco
if encontrado:
    print("El Jedi encontró el sable de luz")
    print("Objetos sacados:", cantidad)
# Si el valor de encontrado es false entonces imprime que no estaba y cuantos objetos saco
else:
    print("El Jedi no encontró el sable de luz")
    print("Objetos sacados:", cantidad)