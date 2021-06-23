class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def whereitstarts(first):
    p = q = first
    while True:
        p = p.next
        q = q.next.next
        if p == q:
            break
    cnt = 0
    p = first
    while p != q:
        p = p.next
        q = q.next
        cnt += 1
    return cnt

z1 = Node(2)
z1.next = Node(3)
z1.next.next = Node(5)
z1.next.next.next = Node(5)
z1.next.next.next.next = Node(8)
z1.next.next.next.next.next = Node(9)
z1.next.next.next.next.next.next = Node(9)
z1.next.next.next.next.next = z1.next.next.next.next
print(whereitstarts(z1))