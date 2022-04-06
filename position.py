position = tuple[int, int] 


def position_create(row: int, col: int) -> position:
    if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col


def position_is(pos: position) -> bool:
    if type(pos) is tuple and len(pos) == 2:
        if type(pos[0]) is int and type(pos[1]) is int:
            if pos[0] >= 0 and pos[1] >= 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def position_row(pos: position) -> int:
    if position_is(pos):
        return pos[0]
    else:
        raise ValueError('position_row: invalid arguments')


def position_col(pos: position) -> int:
    if position_is(pos):
        return pos[1]
    else:
        raise ValueError('position_col: invalid arguments')


def position_equal(pos1: position, pos2: position) -> bool:
    if position_is(pos1) and position_is(pos2):
        if pos1 == pos2:
            return True
        else:
            return False
    else:
        raise ValueError('position_equal: invalid arguments')


def position_str(pos: position) -> str:
    if position_is(pos):
        return '(' + str(position_row(pos)) + ', ' + str(position_col(pos)) + ')'
    else:
        raise ValueError('position_str: invalid arguments')


#project made by fatelas