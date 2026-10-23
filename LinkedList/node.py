class Node:
    def __init__(self, data, next=None):
        # hacemos referencia None, porque el ultimo nodo te va a llevar a None
        self.data = data
        self.next = next


if __name__ == "__main__":
    from node import Node

    node_1 = None
    node_2 = Node("A", None)
    node_3 = Node("B", node_2)

    print(node_2)
    print(node_2.data)
    print(node_2.next)
    print(node_3.next)

    # para ver el dato del siguiente nodo
    print(node_3.next.data)

    # para que el nodo_1 sin valor, lo apuntaramos a otro lado o quisieramos saber a donde apunta
    node_1 = Node("C", node_3)
    print(node_1.next.data)
    # B
    print(node_1.data)
    # C

    # asi podemos ver como utilizamos esos nodos

    # vamos a crear una serie de nodos

    head = None

    print("Esta es la nueva linked list")
    for count in range(1, 5):
        head = Node(count, head)
        print(head.data)
        print(head)

    """
    Esta es la nueva linked list
    1
    <node.Node object at 0x7f850db67be0>
    2
    <node.Node object at 0x7f850db67b50>
    3
    <node.Node object at 0x7f850db67af0>
    4
    <node.Node object at 0x7f850db67a60>
    """
    """
    print('aqui empieza una iteracion')
    while head != None:
        print(head.data)
        head = head.next
    """

    """
    4
    3
    2
    1
    """
