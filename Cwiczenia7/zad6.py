class Node():
    def __init__(self, val = None):
        self.val = val
        self.next = None

first = Node(3)

def add_el_to_list(el):
    if first.next == None:
        first.next = Node(el)
    else:
        prev = None
        current = first
        while current:
            prev = current
            current = current.next
        prev.next = Node(el)
        prev.next.next = current

def print_list():
    current = first
    while current:
        print(current.val)
        current = current.next

add_el_to_list(4)
add_el_to_list(4)
add_el_to_list(6)
add_el_to_list(8)
add_el_to_list(9)
print_list()