class Node():
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


def create_list(tab):
    first = Node()
    current = first
    for i in range(len(tab)):
        current.next = Node(tab[i])
        current = current.next
    current.next = first.next
    return first.next

def deleq(cur1,cur2):
    deleted = 0
    q1 = cur1
    q2 = cur2
    prev1 = cur1
    cur1 = cur1.next
    prev2 = cur2
    cur2 = cur2.next
    moved = True
    while cur1 != q1 and cur2 != q2 and moved:
        if cur1.val < cur2.val:
            #print("A")
            cur1 = cur1.next
        elif cur2.val < cur1.val:
            #print("B")
            cur2 = cur2.next
        elif cur2.val == cur1.val:
            #print("C")
            prev1.next = cur1.next
            prev2.next = cur2.next
            cur1 = cur1.next
            cur2 = cur2.next
            deleted += 2
        else:
            moved = False
    return deleted


def print_list(start):
    p = start
    q = start
    while q is not None and q.next is not None:
        print(p.val, end = ' ')
        p, q = p.next, q.next.next
        if p == q:
            print()
            return


lst1 = create_list([1,3,4,5,6,7,9])
lst2 = create_list([1,2,3,4,5,6,7,8,9,10])
print_list(lst1)
print_list(lst2)
print(deleq(lst1,lst2))
print_list(lst1)
print_list(lst2)