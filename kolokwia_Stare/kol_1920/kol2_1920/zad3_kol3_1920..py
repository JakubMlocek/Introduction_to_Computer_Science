class Node():
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next

first = Node()
def add(val):
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

def print_list(first):
    current = first
    while current:
        print(current.val, end = ' ')
        current = current.next
    print()

def create_list(tab):
    first = Node()
    current = first
    for i in range(len(tab)):
        current.next = Node(tab[i])
        current = current.next
    return first.next

def del_eq_val(first):
    if not first.next:
        return
    prev = first
    current = first.next
    dl = 1
    maxdl = 0
    onemax = True
    while current:
        if current.val == prev.val:
            print(str(current.val) + " " + str(prev.val))
            dl += 1
            #if dl == maxdl:
            #    onemax = False
            #if dl > maxdl:
            #    maxdl = dl
            #    onemax = True
        else:
            if dl > maxdl:
                maxdl = dl
                onemax = True
            elif dl == maxdl:
                onemax = False
            dl = 1
        prev = current
        current = current.next
    if not onemax:
        return

    is_started = False
    start = None
    prev_prev = None
    prev = first
    current = first.next
    dl = 1
    while current:
        if current.val == prev.val:
            if not is_started:
                start = prev_prev
                is_started = True
            dl += 1
        else:
            if dl == maxdl:
                start.next = current
                return first
            is_started = False
            dl = 1
        prev_prev = prev
        prev = current
        current = current.next







lst = create_list([ 1, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2,3])
#lst = create_list([  1 ,3, 3, 3, 3, 5, 7, 11, 13, 13, 1, 2, 2, 2, 2, 3 ])
print_list(lst)

print_list(del_eq_val(lst))