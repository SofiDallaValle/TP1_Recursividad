"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra 'Python', si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from datetime import datetime

class nodoCola(object):
    info, sig = None, None

class Cola(object):

    def __init__(self):
        self.frente, self.final = None, None
        self._tamanio = 0

    def arribo(self, dato):
        """Arriba el dato al final de la cola"""
        nodo = nodoCola()
        nodo.info = dato
        if self.frente is None:
            self.frente = nodo
        else: 
            self.final.sig = nodo 
        self.final = nodo
        self._tamanio += 1

    def atencion (self):
        """Atiende el elemento en el frente de la cola y lo devuelve"""
        dato = self.frente.info
        self.frente = self.frente.sig
        if self.frente is None: 
            self.final = None
        self._tamanio -= 1
        return dato
    
    def cola_vacia (self):
        """Devuelve True si la cola esta vacia"""
        return self.frente is None
    
    def en_frente (self):
        """Devuelve el valor almacenado en el frente de la cola"""
        return self.frente.info 
        
    def tamanio (self):
        """Devuelve el numero de elementos en la cola"""
        return self._tamanio
    
    def mover_al_final (self):
        """Mueve el elemento del frente de la cola al final"""
        dato = self.atencion()
        self.arribo(dato)
        return dato
    
    def barrido (self):
        """Muestra el contenido de la cola sin perder datos"""
        i = 0 
        while (i < self._tamanio):
            dato = self.mover_al_final()
            print(dato)
            i += 1

    #a. Función que elimina de la cola todas las notificaciones de Facebook.
    def eliminar_facebook(self):
        i = 0
        while (i < self._tamanio):
            dato = self.atencion()
            if dato["app"] != "Facebook":
                self.arribo(dato)
            i += 1

    #b. Función que muestra todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', si perder datos en la cola.
    def mostrar_twitter_python(self):
        i = 0 
        while (i < self._tamanio):
            dato = self.atencion()
            if dato["app"] == "Twitter" and "Python" in dato["message"].lower():
                print(dato)
            i += 1
            self.arribo(dato)

    #c. Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
    def almacenar_horarios(self):
        pila = []
        i = 0
        inicio = datetime.strptime("11:43", "%H:%M")
        fin = datetime.strptime("15:57", "%H:%M")
        while (i < self._tamanio):
            dato = self.atencion()
            notification_time = datetime.strptime(dato["time"], "%H:%M")
            if inicio <= notification_time <= fin:
                pila.append(dato)
            self.arribo(dato)
            i += 1
        return len(pila)
    
    # Ejemplo de uso

cola = Cola()
cola.arribo({"time": "10:30", "app": "Facebook", "message": "New friend request"})
cola.arribo({"time": "12:00", "app": "Twitter", "message": "Python is great!"})
cola.arribo({"time": "14:00", "app": "Twitter", "message": "Learning Python"})
cola.arribo({"time": "16:00", "app": "Facebook", "message": "You have a new message"})

print("Notificaciones de Twitter con 'Python':")
cola.mostrar_twitter_python()

print("\nNúmero de notificaciones entre las 11:43 y las 15:57:")
print(cola.almacenar_horarios())

print("\nEliminando notificaciones de Facebook...")
cola.eliminar_facebook()

print("\nNotificaciones restantes en la cola:")
cola.barrido()
