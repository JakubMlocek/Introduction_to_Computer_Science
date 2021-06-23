class Node:
    def __init__(self,id,val):
        self.id = id
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,first):
        self.first = None

    def assign(self, id, val):
        if (self.first == None):
            self.first = Node(id, val)
        elif (self.first.id == id):
            self.first.val = val
        else:
            if (id < self.first.id):
                p = self.first
                q = Node(id, val)
                q.next = p
                self.first = q
                return
            p = self.first.next
            r = self.first
            while (p != None):
                if (p.id == id):
                    p.val = val
                    return
                elif (id < p.id):
                    q = Node(id, val)
                    q.next = p
                    r.next = q
                    return
                r = p
                p = p.next
            r.next = Node(id, val)



    def print(self):
        p = self.first
        while p != None:
            print(f"{p.id}   {p.val}")
            p = p.next

lista = LinkedList()
lista.assign(10,1)
lista.assign(12,5)
lista.print()
lista.assign(33,5)
lista.print()
