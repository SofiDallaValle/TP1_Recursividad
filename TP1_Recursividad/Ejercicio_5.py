#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_decimal(num):
    num = num.upper()
    # Diccionario con el valor de cada letra
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    invalidos = ["IIII", "XXXX", "CCCC", "MMMM", "VV", "LL", "DD"]
    # Valida repeticiones inválidas
    for patron in invalidos:
        if patron in num:
            raise ValueError("Número romano inválido")
        
    # Valida letras inválidas
    for letra in num:
        if letra not in valores:
            raise ValueError("Número romano inválido")
        
    # Cuando es una sola letra devuelve directamente el valor
    if len(num) == 1:
        return valores[num]
    # Si el valor de la primer letra es menor a la siguiente entonces resta el primer valor 
    # y vuelve a llamar a la funcion pero con el valor desde la posicion 1 en adelante     
    if valores[num[0]] < valores[num[1]]:
        return -valores[num[0]] + romano_decimal(num[1:])
    # Si no pasa esto se suma el primer valor y vuelve a llamar la funcion con el valor desde la posicion 1 en adelante
    else: 
        return valores[num[0]] + romano_decimal(num[1:])
   
    
num = input("Escriba un número romano que quiera pasar a decimal: ")
# Utilizo el try por los posibles errores
try:
    print(romano_decimal(num))
except ValueError as e:
    print(e)