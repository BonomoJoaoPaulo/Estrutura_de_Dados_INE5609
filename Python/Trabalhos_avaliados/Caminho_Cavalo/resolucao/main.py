from ChessHelper import ChessHelper
from Position import Position
from Queue import Queue


def verified(verificados, position):
    for verificado in verificados:
        if (verificado.column == position.column) and (verificado.row == position.column):
            return True

    return False


def acha_menor_caminho(origem, destino):
    verificados = []
    fila = Queue(64)
    fila.insert(origem)

    while not fila.empty():
        pos_popped = fila.pop()

        if pos_popped.column == destino.column and pos_popped.row == destino.row:
            return pos_popped.step

        possible_positions = ChessHelper.calculate_positions(pos_popped)

        for position in possible_positions:
            if not verified(verificados, position) and position.is_valid():
                fila.insert(Position(position.column, position.row, pos_popped.step + 1))
                verificados.append(pos_popped)

    return "Nao encontrado"


pos_inicial = input()
pos_destino = input()

inicio = Position(ChessHelper.get_column_number(pos_inicial[0]), int(pos_inicial[1]) - 1, 0)
fim = Position(ChessHelper.get_column_number(pos_destino[0]), int(pos_destino[1]) - 1, 0)

steps = acha_menor_caminho(inicio, fim)

print(f"Movimentos: {steps}")
