class BinaryTree:
    def __init__(self, array_size):
        self.size = array_size
        self.vetor = [None] * array_size
        self.hight = self.return_node_hight(0)

# Insere um elemento x em um node
    def insert(self, x, node):
        if not self.vetor[node]:
            self.vetor[node] = x
        else:
            return "Nao eh possivel inserir esse valor nessa posicao"
        return self.vetor

# Remove um determinado node
    def remove(self, node):
        if not self.vetor[node]:
            return "Nao ha nada nesse nó"
        else:
            self.vetor[node] = [None]
        return self.vetor

# Retorna o node de um elemento x
    def return_node(self, x):
        if x in self.vetor:
            x_node = self.vetor[self.vetor.index(x)]
            return x_node
        else:
            return "Esse elemento nao esta na Arvore"

# Retorna a altura de um determinado node
    def return_node_hight(self, node, count=0):
        if (node * 2 + 1) >= self.size:
            return count
        else:
            count += 1
            return self.return_node_hight(node*2 + 1, count)


# Criacao de uma Arvore
arvore_teste = BinaryTree(9)

# Criacao dos nodes
arvore_teste.insert(1, 0)
arvore_teste.insert(20, 1)
arvore_teste.insert(64, 2)
arvore_teste.insert(-15, 3)
arvore_teste.insert(12, 4)
arvore_teste.insert(3, 5)
arvore_teste.insert(98, 6)
arvore_teste.insert(10, 7)
arvore_teste.insert(33, 8)

# Testes
print(arvore_teste.vetor)
print(arvore_teste.return_node_hight(1))
print(arvore_teste.hight)
