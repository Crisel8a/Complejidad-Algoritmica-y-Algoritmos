class Node:
    def __init__(self, data, next=None):
        self.data = data  # Almacena el valor del nodo
        self.next = next  # Apunta al siguiente nodo en la lista
        self.prev = None  # Apunta al nodo anterior (para listas doblemente enlazadas)

    def __str__(self):
        return str(self.data)  # Representación en cadena del nodo (su dato)

    def addNode(self, newNode):
        newNode.prev = (
            self  # Establece el nodo actual como el nodo anterior del nuevo nodo
        )
        newNode.next = (
            self.next
        )  # El siguiente del nuevo nodo apunta al siguiente del nodo actual
        if self.next is not None:  # Si hay un siguiente nodo
            self.next.prev = (
                newNode  # El siguiente nodo apunta al nuevo nodo como su anterior
            )
        self.next = newNode  # El siguiente del nodo actual apunta al nuevo nodo
