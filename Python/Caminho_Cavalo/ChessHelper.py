from Position import Position


class ChessHelper:
    def __init__(self):
        pass

    def get_column_number(self, column):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return columns.index(column)

    def calculate_positions(self, position):
        possible_positions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        positions_list = []
        for x, y in possible_positions:
            positions_list.append(Position(int(position.column) + y, int(position.row) + x, 0))

        return positions_list
