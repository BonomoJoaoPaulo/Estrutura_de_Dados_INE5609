
class AVL:
    def __init__(self, element = None):
        self.element = element
        self.setaFilhos(None, None)

    def setaFilhos(self, left, right):
        self.left = left
        self.right = right

    def balanco(self):
        prof_left = 0
        if self.left:
            prof_left = self.left.profundidade()
        prof_right = 0
        if self.right:
            prof_right = self.right.profundidade()
        return prof_left - prof_right

    def profundidade(self):
        prof_left = 0
        if self.left:
            prof_left = self.left.profundidade()
        prof_dir = 0
        if self.right:
            prof_dir = self.right.profundidade()
        return 1 + max(prof_left, prof_dir)

    def rotacaoleft(self):
        self.element, self.right.element = self.right.element, self.element
        old_left = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_left, self.left.left)

    def rotacaoright(self):
        self.element, self.left.element = self.left.element, self.element
        old_right = self.right
        self.setaFilhos(self.left.left, self.left)
        self.right.setaFilhos(self.right.right, old_right)

    def rotacaoleftright(self):
        self.left.rotacaoleft()
        self.rotacaoright()

    def rotacaorightleft(self):
        self.right.rotacaoright()
        self.rotacaoleft()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.left.balanco() > 0:
                self.rotacaoright()
            else:
                self.rotacaoleftright()
        elif bal < -1:
            if self.right.balanco() < 0:
                self.rotacaoleft()
            else:
                self.rotacaorightleft()

    def insere(self, element):
        if self.element is None or element <= self.element:
            if not self.left:
                self.left = AVL(element)
            else:
                self.left.insere(element)
        else:
            if not self.right:
                self.right = AVL(element)
            else:
                self.right.insere(element)
        self.executaBalanco()

    def imprime_pre_ordem(self, root):
        if root is not None:
            if root.element is not None:
                print(root.element, end=" ")
            self.imprime_pre_ordem(root.left)
            self.imprime_pre_ordem(root.right)
        
    def imprime_em_ordem(self, root):
        if root is not None:
            self.imprime_em_ordem(root.left)
            if root.element is not None:
                print(root.element, end=" ")
            self.imprime_em_ordem(root.right)

    def imprime_pos_ordem(self, root):
        if root is not None:
            self.imprime_pos_ordem(root.left)
            self.imprime_pos_ordem(root.right)
            if root.element is not None:
                print(root.element, end=" ")
