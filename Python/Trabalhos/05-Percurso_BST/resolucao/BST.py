class BST:
    class _Node:
        def __init__(self, element=None):
            self._element = element
            self._left_child = None
            self._right_child = None

    def __init__(self):
        self.size = 0
#        self.hight = self.return_node_hight(0)
        self.root = None
        self.ordem_array = []
        self.pre_ordem_array = []
        self.pos_ordem_array = []

# Insere um elemento x em um node
    def insert(self, x, root=None):
        if root is None:
            root = self.root

        if root is None:
            self.root = self._Node(x)
        else:
            if x <= root._element:
                if root._left_child is None:
                    root._left_child = self._Node(x)
                else:
                    self.insert(x, root._left_child)
            if x > root._element:
                if root._right_child is None:
                    root._right_child = self._Node(x)
                else:
                    self.insert(x, root._right_child)

        self.size += 1
        return self.size

    def append_in_pre_ordem_array(self, root):
        if root is not None:
            print(root._element, end = " ")
            self.append_in_pre_ordem_array(root._left_child)
            self.append_in_pre_ordem_array(root._right_child)

    def append_em_ordem_array(self, root):
        if root is not None:
            left_child = root._left_child
            right_child = root._right_child

            self.append_em_ordem_array(left_child)
            print(root._element, end=" ")
            self.append_em_ordem_array(right_child)

    def append_pos_ordem_array(self, root):
        if root is not None:
            left_child = root._left_child
            right_child = root._right_child

            self.append_pos_ordem_array(left_child)
            self.append_pos_ordem_array(right_child)
            print(root._element, end=" ")






    def __str__(self):
        return f"{self.append_em_ordem_array(self.root)}"

"""
    def left_child(self, x):
        print(x._left_child._element)
        return self.left_child(x._left_child._element)

    def right_child(self, x):
        print(x._right_child._element)
        return self.left_child(x._right_child._element)

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
"""

# Criacao de uma Arvore
arvore_teste = BST()

# Input do número de nós
nodes_number = int(input())

# Criacao dos nodes
for i in range(0, nodes_number):
    new_node = int(input())
    arvore_teste.insert(new_node)

# Testes
arvore_teste.append_in_pre_ordem_array(arvore_teste.root)
print("")
arvore_teste.append_em_ordem_array(arvore_teste.root)
print("")
arvore_teste.append_pos_ordem_array(arvore_teste.root)
