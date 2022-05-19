class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def empty_pos(self, i):
        if self.table[i] == -1 or self.table[i] == -2:
            return True

        return False

    def insert(self, s):
        m = self.size
        pos = len(s) % m
        pos_inicial = pos

        if self.empty_pos(pos):
            self.table[pos] = s

        else:
            while not self.empty_pos(pos):
                pos += 1
                if pos == self.size:
                    pos = 0
                if pos == pos_inicial:
                    return "Nao foi possivel fazer a insercao, a tabela esta cheia!"

            self.table[pos] = s

        return self.table[pos]

    def pop(self, s):
        if s in self.table:
            pos = self.table.index(s)
            self.table[pos] = -2
        else:
            return "Nao foi possivel fazer a remocao, a string nao esta na tabela!"

        return self.table[pos]
