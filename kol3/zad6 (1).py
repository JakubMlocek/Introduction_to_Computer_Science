#Jakub Młocek
#Funkcja korzysta z uporzadkowanych rosnaca elementow przechodzac do dalszego wskaznika,
#gdy element w jej liscie jest mniejszy niz w pozostałych. Nastepnie gdy elementy są równe
#w trzech listach sa dodawane do listy wynikowej
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_to_list(first,val):
    if first == None:
        return Node(val)
    elif first.val == None:
        first.val = val
        return first
    else:
        prev = None
        current = first
        while current:
            prev = current
            current = current.next
        prev.next = Node(val)
        return first

def iloczyn(z1,z2,z3):
    cur1, cur2, cur3 = z1, z2, z3
    il = None
    while cur1.next and cur2.next and cur3.next:
        if cur1.val == cur2.val == cur3.val:
            il = add_to_list(il,cur1.val)
            cur1 = cur1.next
            cur2 = cur2.next
            cur3 = cur3.next
        else:
            if cur1.val < cur2.val or cur1.val < cur3.val:
                cur1 = cur1.next
            if cur2.val < cur3.val or cur2.val < cur1.val:
                cur2 = cur2.next
            if cur3.val < cur2.val or cur3.val < cur1.val:
                cur3 = cur3.next
    return il
