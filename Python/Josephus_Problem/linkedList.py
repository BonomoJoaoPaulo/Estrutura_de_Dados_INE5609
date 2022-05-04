class Node:
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x):
        novo = Node()
        novo.value = x
        q = self.head
        if self.head is None:
            self.head = novo
        else:
            while q.next is not None:
                q = q.next

            q.next = novo

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
        q = self.head
        while q.next.value != x:
            q = q.next
        q.next = q.next.next

    def printa(self):
        q = self.head
        print(q.value)
        while q.next is not None:
            print(q.next.value)
            q = q.next


divisoria = "------------"
teste = LinkedList()
teste.append(3)
teste.append(12)
teste.printa()
print(divisoria)
teste.append(4)
teste.printa()
print(divisoria)
teste.remove(12)
teste.append(50)
teste.printa()
teste.insert(24, 1)
print(divisoria)
teste.printa()
