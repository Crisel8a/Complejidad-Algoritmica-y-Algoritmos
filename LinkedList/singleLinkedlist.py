from node import Node  # Importa la clase Node desde otro archivo llamado 'node'.

# Se asume que Node tiene atributos como 'data' y 'next'.


class SingleLinkedList:
    def __init__(self):
        self.tail = None  # Referencia al primer nodo de la lista (mal nombrado, debería llamarse 'head')
        self.size = 0  # Lleva el conteo del número de nodos en la lista

    def append(self, data):
        node = Node(data)  # Crea un nuevo nodo con el dato recibido

        if self.tail is None:  # Si la lista está vacía
            self.tail = node  # El nuevo nodo se convierte en el primero (head/tail)
        else:
            current = self.tail  # Comienza desde el primer nodo

            while current.next:  # Recorre hasta el último nodo
                current = current.next

            current.next = node  # Inserta el nuevo nodo al final de la lista

        self.size += 1  # Incrementa el tamaño de la lista

    def size(self):
        return str(
            self.size
        )  # Devuelve el tamaño como cadena (⚠️ Este método sobrescribe el atributo 'size')

    def iter(self):
        current = self.tail  # Comienza desde el primer nodo

        while current:  # Mientras haya nodos
            val = current.data  # Extrae el dato
            current = current.next  # Pasa al siguiente nodo
            yield val  # Retorna el dato usando un generador

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:  # Si encuentra el nodo con el dato buscado
                self.tail = current.next  # Cambia la cabeza al siguiente nodo (⚠️ Esto solo es válido si es el primero)
            else:
                previous.next = current.next  # Salta el nodo actual
                self.size -= 1
                return current.data  # Devuelve el dato borrado

        previous = (
            current  # ⚠️ Esto está fuera del bucle y nunca se ejecutará correctamente
        )
        current = current.next  # ⚠️ current es None aquí, error lógico

    def search(self, data):
        for node in self.iter():  # Recorre los nodos usando el generador
            if node == data:
                return f"Node {data} found"
            else:
                return f"Node {data} not found"  # ⚠️ Esto termina la búsqueda en la primera iteración

    def clear(self):
        self.tail = None
        self.head = None  # ⚠️ 'head' no está definido en ningún otro lugar
        self.size = 0
        return "List cleared"
