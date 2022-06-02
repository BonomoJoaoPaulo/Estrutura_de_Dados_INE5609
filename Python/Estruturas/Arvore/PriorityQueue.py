class PriorityQueue:
    """Min-Priority Queue with Heap"""
    def __init__(self):
        self.queue = []

    def insert(self, x):
        self.queue.append(x)
        last_idx = len(self.queue) -1
        self._upheap(last_idx)

    def update(self, pos, new_x):
        prev_x = self.queue[pos]
        self.queue[pos] = new_x
        if new_x < prev_x:
            self._upheap(pos)
        else:
            self._downheap(pos)

    def remove(self):
        first_idx, last_idx = 0, -1
        self._swap(first_idx, last_idx)
        result = self.queue.pop(last_idx)
        self._downheap(first_idx)
        return result

    def _upheap(self, p):
        parent = self._get_parent(p)
        if (not self._is_root(p)) and (self._get_priority(p) < self._get_priority(parent)):
            self._swap(p, parent)
            self._upheap(parent)

    def _downheap(self, p):
        if self._has_left(p):
            small_child = self.left(p)
            small_child_pos = self._left_pos(p)
            if self._has_right(p):
                r_child = self.right(p)
                r_child_pos = self._right_pos(p)
                if r_child < small_child:
                    small_child = r_child
                    small_child_pos = r_child_pos
            if small_child < self._get_priority(p):
                self._swap(p, small_child_pos)
                self._downheap(small_child_pos)

    def _get_parent(self, pos):
        return (pos - 1)//2

    def _is_root(self, pos):
        return pos == 0

    def _get_priority(self, pos):
        return self.queue[pos]

    def left(self, pos):
        return self.queue[pos * 2 + 1]

    def right(self, pos):
        return self.queue[pos * 2 + 2]

    def _left_pos(self, pos):
        return pos * 2 + 1

    def _right_pos(self, pos):
        return pos * 2 + 2

    def _has_left(self, pos):
        return pos * 2 + 1 < len(self.queue)

    def _has_right(self, pos):
        return pos * 2 + 2 < len(self.queue)

    def _swap(self, pos_a, pos_b):
        self.queue[pos_a], self.queue[pos_b] = self.queue[pos_b], self.queue[pos_a]

    def __str__(self):
        return str(self.queue)


# Testes

q = PriorityQueue()

for i in range(5, 0, -1):
    q.insert(i)

q.update(1, 0)

print(q)

q.update(1, 6)

print(q)
