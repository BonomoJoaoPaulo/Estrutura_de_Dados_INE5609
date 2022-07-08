class Graph:
    def __init__(self) -> None:
        self._V = []
        self._number_V = 0
        self._E = []

    class _Vertice:
        def __init__(self, element) -> None:
            self._element = element
        
        def __str__(self) -> str:
            return str(self._element)
        

    class _Aresta:
        def __init__(self, u, v) -> None:
            self._aresta = {u : v}
        
        def __str__(self) -> str:
            return str(self._aresta)


    def _insert_vertice(self, x):
        new_vertice = self._Vertice(x)
        self._V.append(new_vertice)
        self._number_V += 1
        return new_vertice

    def _insert_aresta(self, u, v):
        new_aresta = self._Aresta(u, v)
        self._E.append(new_aresta)
        return new_aresta

    def __str__(self) -> str:
        return str(self._V)
