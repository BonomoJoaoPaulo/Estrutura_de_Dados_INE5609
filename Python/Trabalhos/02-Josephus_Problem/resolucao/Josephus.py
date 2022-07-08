class Node():
    def __init__(self, x=0):
        self.value = x
        self.next = self


class CircularLinkedList():
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.size += 1

    def remove_next_node(self, previous_node):
        if previous_node.next == self.tail:
            self.tail = previous_node.next.next

        previous_node.next = previous_node.next.next
        self.size -= 1


def solveJosephus(n, m):
    list = createCircularLinkedList(n)
    soldier = list.tail

    while list.size != 1:
        previous_soldier = find_previous_soldier(soldier, m)
        if previous_soldier.next != soldier:
            list.remove_next_node(previous_soldier)
            soldier = previous_soldier.next

        else:
            list.remove_next_node(soldier)
            soldier = soldier.next

    return list.tail.value


def readData():
    data = []
    test_cases = int(input())
    data.append(test_cases)

    for i in range(test_cases):
        n = int(input())
        m = int(input())
        data.append(n)
        data.append(m)

    return data


def createCircularLinkedList(n):
    list = CircularLinkedList()
    list.append(1)
    for number in range(n, 1, -1):
        list.append(number)

    return list


def find_previous_soldier(current_soldier, m):
    counter = 1
    soldier_to_kill = current_soldier
    while counter < m:
        soldier_to_kill = soldier_to_kill.next
        counter += 1

    return soldier_to_kill


data = readData()
for test_number in range(data[0]):
    n = data[(test_number * 2) + 1]
    m = data[(test_number * 2) + 2]

    result = solveJosephus(n, m)

    print(f'Usando n={n}, m={m}, resultado={result}')
