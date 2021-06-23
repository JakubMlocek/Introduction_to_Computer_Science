class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def custo_print(cos):
    if cos is not None:
        print(cos.val)


def del_prev(start):
    p = start
    prev = None
    rem = -1

    while p is not None:
        # custo_print(p)
        # custo_print(prev)
        # print()
        if prev is not None and rem > p.val:
            prev.next = p.next
            rem = p.val
            p = prev.next
        else:
            rem = p.val
            prev = p
            p = p.next

    return start


def print_all(p):
    while p is not None:
        print(p.val, end=" ")
        p = p.next
    print()


def create_list(tab):
    sentinel = Node()
    sen = sentinel
    for i in range(len(tab)):
        sen.next = Node(tab[i])
        sen = sen.next
    return sentinel.next


lst = create_list([5,4,3,4,1])
print_all(lst)
print_all(del_prev(lst))