from xml.dom.minidom import Element


class AVL:
    def __init__(self, element):
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
        self.eleelement, self.right.eleelement = self.right.eleelement, self.eleelement
        old_left = self.left
        self.setaFilhos(self.right, self.right.right)
        self.left.setaFilhos(old_left, self.left.left)

    def rotacaoright(self):
        self.eleelement, self.left.eleelement = self.left.eleelement, self.eleelement
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
        if element <= self.element:
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

    def imprimeArvore(self, indent = 0):
        print(" " * indent + str(self.element))
        if self.left:
            self.left.imprimeArvore(indent + 2)
        if self.right:
            self.right.imprimeArvore(indent + 2)
