class Node:
    def __init__(self, data, next=None):
        self.data = data  # Almacena el valor del nodo
        self.next = next  # Apunta al siguiente nodo en la lista

    def __str__(self):
        return str(self.data)  # Representación en cadena del nodo (su dato)


def hascycle(head):
    slow = head  # Inicializa el puntero lento al inicio de la lista
    fast = head  # Inicializa el puntero rápido al inicio de la lista

    while fast and fast.next:  # Mientras el puntero rápido y su siguiente no sean None
        slow = slow.next  # Mueve el puntero lento un paso
        fast = fast.next.next  # Mueve el puntero rápido dos pasos

        if slow == fast:  # Si los punteros se encuentran, hay un ciclo
            return True

    return False  # Si se sale del bucle, no hay ciclo


def hascycle(head):
    slow = head  # Inicializa el puntero lento al inicio de la lista
    fast = head  # Inicializa el puntero rápido al inicio de la lista

    while fast and fast.next:  # Mientras el puntero rápido y su siguiente no sean None
        slow = slow.next  # Mueve el puntero lento un paso
        fast = fast.next.next  # Mueve el puntero rápido dos pasos

        if slow == fast:  # Si los punteros se encuentran, hay un ciclo
            return True

    return False  # Si se sale del bucle, no hay ciclo
