class Position:
    def __init__(self, column, row, step):
        self.column = column
        self.row = row
        self.step = step

    def is_valid(self):
        return (0 <= self.row < 8) and (0 <= self.column < 8)
