class Node:
    def __init__(self, data, next=None):
        self.data = data  # Almacena el valor del nodo
        self.next = next  # Apunta al siguiente nodo en la lista

    def __str__(self):
        return str(self.data)  # Representación en cadena del nodo (su dato)

    def is_palindrome(self):
        # Convert the linked list to a string
        s = ""
        current = self
        while current:
            s += str(current.data)
            current = current.next

        # Check if the string is a palindrome
        return s == s[::-1]


def is_palindrome(head):
    # Convert the linked list to a string
    s = ""
    current = head
    while current:
        s += str(current.data)
        current = current.next

    # Check if the string is a palindrome
    return s == s[::-1]


def findmiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev  # New head of the reversed list


def is_palindrome_optimized(head):
    if head is None or head.next is None:
        return True

    # Step 1: Find the middle of the linked list
    middle = findmiddle(head)

    # Step 2: Reverse the second half of the linked list
    second_half_reversed = reverse_linked_list(middle)

    # Step 3: Compare the first half and the reversed second half
    first_half = head
    second_half = second_half_reversed

    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def create_linked_list_from_string(s):
    if not s:
        return None

    head = Node(s[0])
    current = head

    for char in s[1:]:
        current.next = Node(char)
        current = current.next

    return head


def create_linked_list_from_list(lst):
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for item in lst[1:]:
        current.next = Node(item)
        current = current.next

    return head


def create_linked_list_from_array(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for item in arr[1:]:
        current.next = Node(item)
        current = current.next

    return head


# ejemplo de uso
if __name__ == "__main__":
    # Crear una lista enlazada a partir de una cadena
    s = "racecar"
    head = create_linked_list_from_string(s)
    print_linked_list(head)
    print("Is palindrome:", is_palindrome_optimized(head))

    # Crear una lista enlazada a partir de una lista
    lst = [1, 2, 3, 2, 1]
    head = create_linked_list_from_list(lst)
    print_linked_list(head)
    print("Is palindrome:", is_palindrome_optimized(head))

    # Crear una lista enlazada a partir de un arreglo
    arr = ["a", "b", "c", "b", "a"]
    head = create_linked_list_from_array(arr)
    print_linked_list(head)
    print("Is palindrome:", is_palindrome_optimized(head))
