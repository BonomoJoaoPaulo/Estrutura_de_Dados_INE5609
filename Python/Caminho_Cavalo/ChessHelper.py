from Position import Position


class ChessHelper:

    def get_column_number(column):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return columns.index(column)

    def calculate_positions(position):
        possible_positions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        positions_list = []

        for x, y in possible_positions:
            positions_list.append(Position(int(position.column) + y, int(position.row) + x, 0))

        return positions_list
