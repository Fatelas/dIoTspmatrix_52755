"""
__author__ "Pedro Maló"
__version__ = "1.0"
__all__ = [’position_create’, ’position_is’, ’position_row’, ’position_col’, ’position_equal’, ’position_str’]
"""

position = tuple[int, int, int, int, int, int, int, int]


def position_create(row: int, col: int) -> position:
    """
    Create a position
    :param row: row of position
    :param col: column of position
    :return: position
    """
    if not ( type(row) is int and row >= 0 ) or not ( type(col) is int and col >= 0 ):
        raise ValueError('position_create: invalid arguments')
    return 1, row, 2, 0, -1, col, 0, -2


def position_is(pos: position) -> bool:
    """
    Check if it is a valid position
    :param pos: position to be checked
    :return: True if is a valid position; else False
    """
    return type(pos) is tuple and len(pos) == 8 and \
           type(pos[0]) is int and pos[0] == 1 and \
           type(pos[1]) is int and pos[1] >= 0 and \
           type(pos[2]) is int and pos[2] == 2 and \
           type(pos[3]) is int and pos[3] == 0 and \
           type(pos[4]) is int and pos[4] == -1 and \
           type(pos[5]) is int and pos[5] >= 0 and \
           type(pos[6]) is int and pos[6] == 0 and \
           type(pos[7]) is int and pos[7] == -2


def position_row(pos: position) -> int:
    """
    Return the row of a position
    :param pos: position
    :return: row of position
    """
    if not position_is(pos):
        raise ValueError('position_row: invalid arguments')
    return pos[1]


def position_col(pos: position) -> int:
    """
    Return the column of a position
    :param pos: position
    :return: column of position
    """
    if not position_is(pos):
        raise ValueError('position_col: invalid arguments')
    return pos[5]


def position_equal(pos1: position, pos2: position) -> bool:
    """
    Check if two positions are equal
    :param pos1: 1st position
    :param pos2: 2nd position
    :return: True positions are equal; else False
    """
    return pos1 == pos2 if (position_is(pos1) and position_is(pos2)) else False


def position_str(pos: position) -> str:
    """
    Return the string represenation of a position
    :param pos: position
    :return: string represenation of the position
    """
    if not position_is(pos):
        raise ValueError('position_str: invalid arguments')
    return "(" + str(pos[1]) + ", " + str(pos[5]) + ")"
