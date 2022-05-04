class Node:
    def __init__(self):
        self.value = None
        self.next = self


class LinkedList:
    def __init__(self):
        self.tail = None

    def append(self, x):
        novo = Node()
        novo.value = x
        if self.tail is None:
            self.tail = novo
            novo.next = self.tail
        else:
            novo.next = self.tail.next
            self.tail.next = novo


    def insert(self, x, pos):
        novo = Node()
        novo.value = x
        q = self.head
        q.pos = 0
        while q.pos != pos-1:
            q = q.next
        novo.next = q.next
        q.next = novo

    def remove(self, x):
        q = self.tail
        while q.next != self.tail:
            if q == self.tail:
                print('oi')
                q.next = q.next.next
                self.tail = self.tail.next
                break
            q = q.next

    def printa(self):
        q = self.tail
        print(q.value)
        while q.next is not self.tail:
            print(q.next.value)
            q = q.next


teste = LinkedList()
teste.append("José")
teste.append("Matheus")
teste.append("João")
teste.printa()
teste.remove("José")
teste.printa()
