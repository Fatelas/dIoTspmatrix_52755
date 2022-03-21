position = tuple[int,int]

def position_create(row:int, col:int) -> position :
    if not ( type(row) is int and row >= 0 ) or not ( type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col

def position_is(pos: position) -> bool :
    if type(pos) is position :
        return True
    else :
        return False

def position_row(pos: position) -> int :
    if type(pos) is position :
        return pos[0]
    else : raise ValueError('position_row: invalid arguments')

def position_col(pos: position) -> int :
    if type(pos) is position :
        return pos[1]
    else : raise ValueError('position_col: invalid arguments')

def  position_equal(pos1: position, pos2: position) -> bool :
    if type(pos1) is position and type(pos2) is position :
        if pos1 == pos2 :
            return True
        else:
            return False
    else:
        raise ValueError('position_equal: invalid arguments')

def position_str(pos: position) -> str :
    if type(pos) is position :
        return '(' + pos[0] + ',' + pos[1] + ')'
    else :
        raise ValueError('position_str: invalid arguments')




