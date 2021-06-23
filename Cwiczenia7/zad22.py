class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def check(start):
    p = start
    q = start
    while q is not None and q.next is not None:
        p, q = p.next, q.next.next
        if p == q:
            return True
    return False


z1 = Node(2)
z1.next = Node(3)
z1.next.next = Node(5)
z1.next.next.next = Node(5)
z1.next.next.next.next = z1.next
print(check(z1))