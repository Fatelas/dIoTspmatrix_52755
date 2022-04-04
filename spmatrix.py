from position import *

spmatrix = list[float, dict()]


def spmatrix_create(zero: float = 0.0) -> spmatrix:
    if type(zero) is float:
        return [zero, dict()]
    else:
        raise ValueError('spmatrix_create: invalid arguments')


def spmatrix_is(mat: spmatrix) -> bool:
    if type(mat) is list and type(mat[1]) is dict and type(mat[0]) is float:
        return True
    else:
        return False


def spmatrix_zero_get(mat: spmatrix) -> float:
    if spmatrix_is(mat):
        return mat[0]
    else:
        raise ValueError('spmatrix_zero_get: invalid arguments')


def spmatrix_zero_set(mat: spmatrix, zero: float):
    if spmatrix_is(mat) and type(zero) is float:
        mat[0] = zero
        aux_dict = mat[1]
        for item in list(aux_dict.items()):
            if item[1] == zero:
                del aux_dict[item[0]]
    else:
        raise ValueError('spmatrix_zero_set: invalid arguments')

# meu isto n e suposto verificar se a posicao sequer existe yo? retorna o que se tiver dentro da range meu?
def spmatrix_value_get(mat: spmatrix, pos: position) -> float:
    if spmatrix_is(mat) and position_is(pos):
        return mat[1].get(pos)
    else:
        raise ValueError('spmatrix_value_get: invalid arguments')


def spmatrix_value_set(mat: spmatrix, pos: position, val: float):
    if spmatrix_is(mat) and position_is(pos) and type(val) is float:
        mat[1][pos] = val
    else:
        raise ValueError('spmatrix_value_set: invalid arguments')


def spmatrix_copy(mat: spmatrix) -> spmatrix:
    if spmatrix_is(mat):
        return [spmatrix_zero_get(mat), mat[1].copy()]
    else:
        raise ValueError('spmatrix_copy: invalid arguments')


def spmatrix_dim(mat: spmatrix) -> [tuple[position, position], ()]:
    if spmatrix_is(mat):
        max_x = -1
        max_y = -1
        min_x = float('inf')
        min_y = float('inf')
        if len(mat[1]) != 0:
            for pos in mat[1]:
                if position_row(pos) > max_x:
                    max_x = position_row(pos)
                if position_col(pos) > max_y:
                    max_y = position_col(pos)
                if position_row(pos) < min_x:
                    min_x = position_row(pos)
                if position_col(pos) < min_y:
                    min_y = position_col(pos)
            return position_create(min_x, min_y), position_create(max_x, max_y)
        else:
            return ()
    else:
        raise ValueError('spmatrix_dim: invalid arguments')

# perguntar se a sparsity é 1 quando a dimensao é 0 e o numero de elementos é 0
def spmatrix_sparsity(mat: spmatrix) -> float:
    if spmatrix_is(mat):
        dim = spmatrix_dim(mat)
        if dim != ():
            dim_min = dim[0]
            dim_max = dim[1]
            area = (position_row(dim_max) - position_row(dim_min) + 1) * (position_col(dim_max) - position_col(dim_min) + 1)
            return len(mat[1]) / float(area)
        else:
            return 0  # perguntar se a sparsity é 1 quando a dimensao é 0 e o numero de elementos é 0
    else:
        raise ValueError('spmatrix_sparsity: invalid arguments')


def spmatrix_str(mat: spmatrix, format: str) -> str:
    if spmatrix_is(mat) and type(format) is str:
        ret = ''
        dim = spmatrix_dim(mat)
        dim_min = dim[0]
        dim_max = dim[1]
        zero = spmatrix_zero_get(mat)

        for x in range(position_row(dim_min), position_row(dim_max) + 1):
            for y in range(position_col(dim_min), position_col(dim_max) + 1):
                value = spmatrix_value_get(mat, position_create(x, y))
                if value is not None:
                    ret += format % value
                else:
                    ret += format % zero
                if y != position_col(dim_max):
                    ret += ' '
            if x != position_row(dim_max):
                ret += '\n'

        return ret
    else:
        raise ValueError('spmatrix_str: invalid arguments')


def spmatrix_row(mat: spmatrix, row: int) -> spmatrix:
    if spmatrix_is(mat) and type(row) is int:
        new_mat = [spmatrix_zero_get(mat), {}]
        aux_dict = mat[1]
        for item in list(aux_dict.items()):
            if position_row(item[0]) == row:
                new_mat[1][item[0]] = item[1]
        return new_mat
    else:
        raise ValueError('spmatrix_row: invalid arguments')


def spmatrix_col(mat: spmatrix, col: int) -> spmatrix:
    if spmatrix_is(mat) and type(col) is int:
        new_mat = [spmatrix_zero_get(mat), {}]
        aux_dict = mat[1]
        for item in list(aux_dict.items()):
            if position_col(item[0]) == col:
                new_mat[1][item[0]] = item[1]
        return new_mat
    else:
        raise ValueError('spmatrix_column: invalid arguments')


def spmatrix_diagonal(mat: spmatrix) -> [spmatrix, ...]:
    if spmatrix_is(mat):
        dim = spmatrix_dim(mat)
        if dim != ():
            dim_min = dim[0]
            dim_max = dim[1]
            width = position_row(dim_max) - position_row(dim_min)
            height = position_col(dim_max) - position_col(dim_min)
            if width == height:
                new_mat = [spmatrix_zero_get(mat), {}]
                for x in range(position_row(dim_min), position_row(dim_max) + 1):
                    for y in range(position_col(dim_min), position_col(dim_max) + 1):
                        if x == y:
                            value = spmatrix_value_get(mat, position_create(x, y))
                            if value is not None:
                                new_mat[1][position_create(x, y)] = value
                return new_mat
            else:
                raise ValueError('spmatrix_diagonal: matrix not square')
        else:
            new_mat = [spmatrix_zero_get(mat), {}]
            return new_mat
    else:
        raise ValueError('spmatrix_diagonal: invalid arguments')
