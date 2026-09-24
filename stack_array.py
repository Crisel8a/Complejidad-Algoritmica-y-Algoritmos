class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Array:
    def __init__(self):
        self.elements = []

    def append(self, data):
        self.elements.append(data)

    def remove_last(self):
        if self.elements:
            return self.elements.pop()

    def __len__(self):
        return len(self.elements)


class Stack(Array):
    def __init__(self):
        super().__init__()

    @property
    def size(self):
        return len(self.elements)

    def push(self, data):
        """Agrega un elemento al tope."""
        self.append(data)

    def pop(self):
        """Elimina y retorna el elemento del tope."""
        if self.empty():
            return "The stack is empty"

        return self.remove_last()

    def peek(self):
        """Retorna el elemento del tope sin eliminarlo."""
        if self.empty():
            return "The stack is empty"

        return self.elements[-1]

    def clear(self):
        """Elimina todos los elementos."""
        self.elements.clear()

    def return_elements(self):
        """Retorna los elementos desde el tope hasta el fondo."""
        return self.elements[::-1]

    def search(self, data):
        """Comprueba si un elemento está en la pila."""
        return data in self.elements

    def read(self):
        """Retorna los elementos sin modificar la pila."""
        return self.return_elements()

    def empty(self):
        """Comprueba si la pila está vacía."""
        return self.size == 0

    def empty_stack(self):
        """Vacía la pila."""
        self.clear()
