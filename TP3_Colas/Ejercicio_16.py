"""16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

class QueuePriority:
    def __init__(self):
        self._elements = []

    def arrive(self, value, priority):
        self._elements.append((value,priority))
    
    def attention(self):
        if self._elements:
            highest_priority = min(self._elements, key=lambda x: x[1])[1]
            for i, (value, priority) in enumerate(self._elements):
                if priority == highest_priority:
                    return self._elements.pop(i)
        return None

    def size(self) -> int:
        return len(self._elements)

    def on_front(self):
        if self._elements:
            highest_priority = min(self._elements, key=lambda x: x[1])[1]
            for value, priority in self._elements:
                if priority == highest_priority:
                    return value
        return None
    
    def show(self):
        for value, priority in self._elements:
            print(value)

    def move_to_end (self):
        if self._elements:
            value, priority = self.attention()
            self.arrive(value, priority)    
            return value
        return None
    
    #a. Cargar tres documentos de empleados (cada documento se representa solamente con un nombre).
    def cargar_empleados(self):
        for i in range(3):
            nombre = input("Ingrese el nombre del documento del empleado: ")
            self.arrive(nombre, 1)

    #b. Imprimir el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
    def imprimir_primer_doc(self):
        doc = self.on_front()
        if doc:
            print(f"Primer documento a imprimir: {doc}")
        else:
            print("La cola de impresión está vacía.")

    #c. Cargar dos documentos del staff de TI.
    def cargar_staff_TI(self):
        for i in range(2):
            nombre = input("Ingrese el nombre del documento del staff de TI: ")
            self.arrive(nombre, 2)

    #d. Cargar un documento del gerente.
    def cargar_gerente(self):
        nombre = input("Ingrese el nombre del documento del gerente:")
        self.arrive(nombre, 3)

    #e. Imprimir los dos primeros documentos de la cola.
    def imprimir_dos_primeros(self):  
        aux = QueuePriority()
        mostrados = 0

        while self.size() > 0:
            doc = self.attention()
            if mostrados < 2:
                print(f"Documento: {doc[0]}")
                mostrados += 1
            aux.arrive(doc[0], doc[1])

        while aux.size() > 0:
            doc = aux.attention()
            self.arrive(doc[0], doc[1])

    #f. Cargar dos documentos de empleados y uno de gerente.
    def cargar_empleados_gerente(self):
        for i in range(2):
            nombre = input("Ingrese el nombre del documento del empleado: ")
            self.arrive(nombre, 1)
        nombre_gerente = input("Ingrese el nombre del documento del gerente: ")
        self.arrive(nombre_gerente, 3)

    #g. Imprimir todos los documentos de la cola de impresión.
    def imprimir_documentos(self):
        while self.size() > 0:
            doc = self.attention()
            print(f"Documento impreso: {doc[0]}")
    
#Ejemplo de uso 
if __name__ == "__main__":
    cola = QueuePriority()
    cola.cargar_empleados()
    cola.imprimir_primer_doc()
    cola.cargar_staff_TI()
    cola.cargar_gerente()
    cola.imprimir_dos_primeros()
    cola.cargar_empleados_gerente()
    cola.imprimir_documentos()
