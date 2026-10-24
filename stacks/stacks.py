class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """Appends an element on top."""
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        """Removes and returns the element on top."""
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The stack is empty"

    def peek(self):  # Returns the element on top without removing it.
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"

    def clear(self):
        while self.top:
            self.pop()

    def return_elements(self):
        """Returns a list of all elements in the stack."""
        elements = []
        current = self.top

        while current:
            elements.append(current.data)
            current = current.next

        return elements

    def search(self, data):
        """Searches for an element in the stack."""
        current = self.top

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def read(self):
        """Returns a list of all elements in the stack without modifying it."""
        return self.return_elements()

    def empty(self):
        """Checks if the stack is empty."""
        return self.size == 0

    def empty_stack(self):
        """Empties the stack."""
        self.clear()
