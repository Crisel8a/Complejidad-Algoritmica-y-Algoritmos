class Node:
    def __init__(self, data, next=None):
        self.data = data  # Almacena el valor del nodo
        self.next = next  # Apunta al siguiente nodo en la lista

    def __str__(self):
        return str(self.data)  # Representación en cadena del nodo (su dato)


def OddEvenLinkedList(head):
    if head is None:
        return None

    odd_head = None
    odd_tail = None
    even_head = None
    even_tail = None

    current = head
    index = 1  # Comenzamos con el índice 1 para el primer nodo

    while current:
        if index % 2 == 1:  # Nodo impar
            if odd_head is None:
                odd_head = current
                odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        else:  # Nodo par
            if even_head is None:
                even_head = current
                even_tail = current
            else:
                even_tail.next = current
                even_tail = current

        current = current.next
        index += 1

    # Conectar la lista de nodos impares con la lista de nodos pares
    if odd_tail:
        odd_tail.next = even_head

    # Asegurarse de que el último nodo de la lista par apunte a None
    if even_tail:
        even_tail.next = None

    return odd_head if odd_head else even_head


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# ejemplo de uso
if __name__ == "__main__":
    # Crear una lista enlazada: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Lista original:")
    print_linked_list(head)

    # Reorganizar la lista en nodos impares y pares
    new_head = OddEvenLinkedList(head)

    print("Lista reorganizada (impares primero):")
    print_linked_list(new_head)
