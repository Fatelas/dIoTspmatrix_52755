from position import *

spmatrix = tuple(float, dict())

def spmatrix_create(zero: float = 0) -> spmatrix :
    if type(zero) is float:
        return zero, dict()
    else:
        raise ValueError('spmatrix_create: invalid arguments')

def spmatrix_is(mat: spmatrix) -> bool:
    if not (type(mat[1]) is dict) and type(mat[0] is float):
        return False
    else:
        return True

def spmatrix_zero_get(mat: spmatrix) -> float:
    if spmatrix_is(mat):
        return mat[0]
    else:
        raise ValueError('spmatrix_zero_get: invalid arguments')

#def spmatrix_zero_set(mat: spmatrix, zero: float) :
#    if spmatrix_is(mat) and zero is float:
#        for x in mat:
#            mat.pop()



