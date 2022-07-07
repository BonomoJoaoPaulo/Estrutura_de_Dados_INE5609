class Graph:
    def __init__(self) -> None:
        self.V = []
        self.number_V = 0
        self.E = []
        self.matrix = []

    class _Vertice:
        def __init__(self, element) -> None:
            self.element = element
        

    class _Aresta:
        def __init__(self, u, v) -> None:
            self.aresta = {u : v}


    def insert_vertice(self, x):
        new_vertice = self._Vertice(x)
        self.V.append(new_vertice)
        self.number_V += 1
        return new_vertice

    def insert_aresta(self, u, v):
        new_aresta = self._Aresta(u, v)
        self.E.append(new_aresta)
        self.redefine_matrix(u, v)
        return new_aresta
    
    def redefine_matrix(self, u, v):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == u:
                    if len(self.matrix) < i + 2:
                        self.matrix.append([v])
                    self.matrix[i+1].append(v)
                    return
        self.matrix.append([u])
        self.matrix.append([v])

    def insert_aresta_in_matrix(self, u, v):
        self.matrix[u - 1][v - 1] = 1
        return self.matrix[u-1]
    
    def calculate_stations(self):
        return len(self.matrix)



    def __str__(self) -> str:
        return f"{self.matrix}"
        #return f"Vertices: {self.V} | Arestas: {self.E}"

Grafo = Graph()

number = int(input())

for n in range(1, number+1):
    Grafo.insert_vertice(n)

while True:
    x, y = [int(n) for n in input().split(",")]
    if x != -1 and y != -1:
        Grafo.insert_aresta(x, y)
    else:
        break

print(Grafo.calculate_stations())
