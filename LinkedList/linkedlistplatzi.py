class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def Insert(self, value):
        new_node = LinkedList(value)
        new_node.next = self.next
        self.next = new_node

    def InsertNodeAtTheEnd(self, value):
        new_node = LinkedList(value)
        current = self
        while current.next is not None:
            current = current.next
        current.next = new_node

    def InsertNodeAtTheBeginning(self, value):
        new_node = LinkedList(value)
        new_node.next = self
        return new_node  # Return the new head of the list

    def DeleteNode(self, value):
        current = self
        if current.value == value:
            return current.next  # Return the new head of the list
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return self  # Return the head of the list
            current = current.next
        return self  # Return the head of the list if value not found

    def SearchNode(self, value):
        current = self
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
