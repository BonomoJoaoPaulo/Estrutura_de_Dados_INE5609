class LinkedList:
    class Node:
        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, x):
        pivot = self.head
        while pivot is not None and pivot.element != x:
            pivot = pivot.next
        return pivot

    def insert(self, elem, pos):
        # This method assumes pos is a position in [0, self._size-1]
        new_node = self.Node(elem, None)  # Creating new node
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            insert_here = self.head
            idx = 1
            while idx < pos:
                insert_here = insert_here.next
                idx += 1
            new_node.next = insert_here.next
            insert_here.next = new_node
        self.size += 1

    def remove(self, pos):
        if pos == 0:
            value = self.head.element
            self.head = self.head.next
        else:
            remove_next = self.head
            idx = 1
            while idx < pos:
                remove_next = remove_next.next
                idx += 1
            value = remove_next.next.element
            remove_next.next = remove_next.next.next
        self.size -= 1
        return value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        to_print = []
        pivot = self.head
        while pivot is not None:
            to_print.append(pivot.element)
            pivot = pivot.next
        return str(to_print)


# Testing:
my_list = LinkedList()
print("Initial size: ", len(my_list))
my_list.insert(1, 0)
my_list.insert(2, 0)
my_list.insert(3, 0)
my_list.insert(4, 0)
my_list.insert(10, 4)
print("size: ", len(my_list))
print(my_list)
print("Removing: ", my_list.remove(3))
print(my_list)
my_list.insert(7, 2)
print(my_list)
