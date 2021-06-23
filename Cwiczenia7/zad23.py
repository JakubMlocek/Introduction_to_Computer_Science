class Node():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def dlugosc(start):
    p,q = start,start
    dl = 2
    while True:
        p = p.next
        q = q.next.next
        dl += 1
        if p == q:
            break
    return dl

a = Node(1)
first = a
for i in range(2,7):
    a = Node(i , a)

first.next = Node(5,None)
first.next.next = Node(6,None)
first.next.next.next = first

print(dlugosc(a))