class Graph:
    def __init__(self) -> None:
        self._V = []
        self._number_V = 0
        self._E = []
        self._matrix = []

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
        self._redefine_matrix(u, v)
        return new_aresta
    
    def _redefine_matrix(self, u, v):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if self._matrix[i][j] == u:
                    if len(self._matrix) < i + 2:
                        self._matrix.append([v])
                    self._matrix[i+1].append(v)
                    return
        self._matrix.append([u])
        self._matrix.append([v])

    def _insert_aresta_in_matrix(self, u, v):
        self._matrix[u - 1][v - 1] = 1
        return self._matrix[u-1]
    
    def _calculate_stations(self):
        return len(self._matrix)


    def __str__(self) -> str:
        return str(self._matrix)
        #return f"Vertices: {self.V} | Arestas: {self.E}"
