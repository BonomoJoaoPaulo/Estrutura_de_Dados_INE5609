class Node:
    def __init__(self):
        self.value = None
        self.next = self


class LinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, x):
        novo = Node()
        novo.value = x
        if self.tail is None:
            self.tail = novo
            novo.next = self.tail
        else:
            novo.next = self.tail.next
            self.tail.next = novo

        self.size += 1

    def insert(self, x, pos):
        novo = Node()
        novo.value = x
        q = self.head
        q.pos = 0
        while q.pos != pos - 1:
            q = q.next
        novo.next = q.next
        q.next = novo

    def remove(self, x):
        q = None
        while True:
            if q == None:
                q = self.tail

            elif q == self.tail:
                break

            if q.next.value == x:
                if q.next == self.tail:
                    self.tail = q.next.next
                q.next = q.next.next
                self.size -= 1
                break

            else:
                q = q.next

    def find_prox(self, m, current):
        count = 1
        to_kill = current
        while count <= m:
            to_kill = to_kill.next
            count += 1
        return to_kill

    def printa(self):
        q = None
        while True:
            if q == None:
                q = self.tail
            elif q == self.tail:
                break
            print(q.value)
            q = q.next


j = int(input())

for count in range(j):
    n = int(input())
    m = int(input())
    teste = LinkedList()

    teste.append(1)
    for i in range(n, 1, -1):
        teste.append(i)

    q = teste.tail

    while teste.size != 1:
        morto = teste.find_prox(m, q)
        if morto == q:
            morto = q.next

        teste.remove(morto.value)
        q = morto.next

    print(f"Usando n={n}, m={m}, resultado={teste.tail.value}")
