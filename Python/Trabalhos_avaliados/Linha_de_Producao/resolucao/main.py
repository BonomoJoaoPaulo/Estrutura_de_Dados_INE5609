from Graph import Graph

Grafo = Graph()

number = int(input())

for n in range(1, number+1):
    Grafo._insert_vertice(n)

while True:
    x, y = [int(n) for n in input().split(",")]
    if x != -1 and y != -1:
        Grafo._insert_aresta(x, y)
    else:
        break

print(Grafo._calculate_stations())
print(Grafo._E)
