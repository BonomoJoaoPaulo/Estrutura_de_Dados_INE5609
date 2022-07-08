from re import U
from Graph import Graph

def redefine_workstations(u, v, workstations):
    for i in range(len(workstations)):
            for j in range(len(workstations[i])):
                if workstations[i][j] == u:
                    if len(workstations) < i + 2:
                        workstations.append([v])
                    workstations[i+1].append(v)
                    return
    workstations.append([u])
    workstations.append([v])
    return


Grafo = Graph()

number = int(input())

for n in range(1, number+1):
    Grafo._insert_vertice(n)

workstations = []

while True:
    u, v = [int(n) for n in input().split(",")]
    if u != -1 and v != -1:
        Grafo._insert_aresta(u, v)
        redefine_workstations(u, v, workstations)
    else:
        break

workstations_size = len(workstations)

print(workstations_size)
