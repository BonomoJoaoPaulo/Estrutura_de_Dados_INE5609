from ChessHelper import ChessHelper
from Position import Position
from Queue import Queue


def verified(already_verified, position):
    for verificado in already_verified:
        if (verificado.column == position.column) and (verificado.row == position.column):
            return True
    return False

