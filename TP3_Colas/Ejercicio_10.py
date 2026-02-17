"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra 'Python', si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from datetime import datetime


class Queue:
    def __init__(self):
        self._elements= []

    def arrive(self, value):
        self._elements.append(value)

    def attention(self):
        return (
            self._elements.pop(0)
            if self._elements
            else None
        )

    def size (self) -> int:
        return len(self._elements)
    
    def on_front(self):
        return (
            self._elements[0] 
            if self._elements 
            else None)
    
    def move_to_end(self):
        if self._elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for i in range(len(self._elements)):
            print(self.move_to_end())

    #a. Función que elimina de la cola todas las notificaciones de Facebook.   
    def eliminar_facebook(self):
        size= self.size()
        for i in range(size):
            notification = self.attention()
            if notification["app"] != "Facebook":
                self.arrive(notification)

    #b. Función que muestra todas las notificaciones de Twitter, cuyo mensaje incluya la palabra 'Python', si perder datos en la cola. 
    def mostrar_twitter_python(self):
        size = self.size()
        for i in range(size):
            notification = self.attention()

            if notification["app"] == "Twitter" and "Python" in notification["message"]:
                print(notification)

            self.arrive(notification)


    #c. Utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
    def almacenar_horarios(self):
        stack = []
        size = self.size()

        inicio = datetime.strptime("11:43", "%H:%M")
        fin = datetime.strptime("15:57", "%H:%M")

        for i in range(size):
            notification = self.attention()
            notification_time = datetime.strptime(notification["time"], "%H:%M")

            if inicio <= notification_time <= fin:
                stack.append(notification)

            self.arrive(notification) 

        return len(stack)

# Ejemplo de uso
if __name__ == "__main__":
    queue = Queue()
    queue.arrive({"time": "10:30", "app": "Facebook", "message": "New friend request"})
    queue.arrive({"time": "12:00", "app": "Twitter", "message": "Python is great!"})
    queue.arrive({"time": "14:00", "app": "Twitter", "message": "Learning Python"})
    queue.arrive({"time": "16:00", "app": "Facebook", "message": "You have a new message"})

    print("Notificaciones de Twitter con 'Python':")
    queue.mostrar_twitter_python()

    print("\nNúmero de notificaciones entre las 11:43 y las 15:57:")
    print(queue.almacenar_horarios())

    print("\nEliminando notificaciones de Facebook...")
    queue.eliminar_facebook()

    print("\nNotificaciones restantes en la cola:")
    queue.show()
