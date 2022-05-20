class StackArray:
    def __init__(self, max_size):
        self.items = [None]*max_size
        self.topo = 0  # posicao da proxima insercao

    def push(self, x):
        ''' Insere o x na Pilha '''
        self.items[self.topo] = x
        self.topo += 1

    def isEmpty(self):
        return self.topo == 0

    def pop(self):
        ''' Remove o x da Pilha '''
        if self.isEmpty():
            raise Exception("A Pilha esta vazia")
        self.topo -= 1
        x = self.items[self.topo]
        self.items[self.topo] = None
        return x

    def topo(self):
        ''' Retorna o topo da Pilha, sem remover '''
        return self.items[self.topo - 1]


P = StackArray(10)
P.push(1)
P.push(7)
P.pop()
P.pop()
P.pop()
