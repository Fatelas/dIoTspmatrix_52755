import pytest
from spmatrix import *
from position import *


def test_position_create_valid_1_2():
    assert position_create(1, 2) is not None


def test_position_create_valid_1000_0():
    assert position_create(1000, 0) is not None


def test_position_create_invalid_args_minus1():
    try:
        position_create(-1, -1)
    except ValueError as error:
        assert str(error) == 'position_create: invalid arguments'


def test_position_create_invalid_args_emptytuple():
    try:
        position_create((), ())
    except ValueError as error:
        assert str(error) == 'position_create: invalid arguments'


def test_position_is_true():
    assert position_is(position_create(1, 2)) is True


def test_position_is_false():
    assert position_is(1.2) is False


def test_position_row():
    assert position_row(position_create(1, 2)) == 1


def test_position_col():
    assert position_col(position_create(1, 2)) == 2


def test_position_equal_same():
    assert position_equal(position_create(1, 2), position_create(1, 2)) is True


def test_position_equal_different():
    assert position_equal(position_create(1, 2), position_create(2, 1)) is False


def test_position_str():
    assert position_str(position_create(1, 2)) == '(1, 2)'


def test_spmatrix_create_with_zero_as_default():
    assert spmatrix_create() is not None


def test_spmatrix_create_with_zero_as_1_0():
    assert spmatrix_create(1.0) is not None


def test_spmatrix_is_of_empty_matrix():
    assert spmatrix_is(spmatrix_create()) is True


def test_spmatrix_is_of_non_matrix_float_1():
    assert spmatrix_is(1.0) is False


def test_spmatrix_get_of_empty_matrix_with_zero_as_default():
    assert spmatrix_zero_get(spmatrix_create()) == 0.0


def test_spmatrix_get_of_empty_matrix_with_zero_as_2():
    assert spmatrix_zero_get(spmatrix_create(2.0)) == 2.0


def test_spmatrix_copy_of_empty_matrix_with_zero_as_2():
    assert spmatrix_zero_get(spmatrix_copy(spmatrix_create(2.0))) == 2.0


def test_spmatrix_is_after_spmatrix_copy_after_spmatrix_create():
    assert spmatrix_is(spmatrix_copy(spmatrix_create())) is True


def test_spmatrix_value_set_and_spmatrix_value_get():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 2), 12.5)
    assert spmatrix_value_get(mat, position_create(1, 2)) == 12.5
    spmatrix_value_set(mat, position_create(2, 1), 5.0)
    assert spmatrix_value_get(mat, position_create(2, 1)) == 5.0


def test_spmatrix_value_get_after_replacing_value_with_spmatrix_value_get():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 2), 12.5)
    assert spmatrix_value_get(mat, position_create(1, 2)) == 12.5
    spmatrix_value_set(mat, position_create(1, 2), 5.0)
    assert spmatrix_value_get(mat, position_create(1, 2)) == 5.0


def test_spmatrix_dim_of_empty_matrix():
    assert spmatrix_dim(spmatrix_create()) == ()


def test_spmatrix_dim_of_matrix_with_one_element():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 2), 5.0)
    dim = spmatrix_dim(mat)
    assert position_str(dim[0]) == '(1, 2)'
    assert position_str(dim[1]) == '(1, 2)'


def test_spmatrix_sparsity_of_m2x2_diagonal_matrix():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    assert spmatrix_sparsity(mat) == 0.5


def test_spmatrix_sparsity_of_matrix_with_1_element_after_element_removal_using_spmatrix_zero_set():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 12.5)
    spmatrix_value_set(mat, position_create(2,1), 5.0)
    spmatrix_zero_set(mat, 12.5)
    assert spmatrix_sparsity(mat) == 0.0


def test_spmatrix_str_of_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    assert spmatrix_str(mat, "%.1f") == '12.5 0.0' + '\n' + '0.0 5.0'


def test_spmatrix_row_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    mat_row = spmatrix_create()
    spmatrix_value_set(mat_row, position_create(1, 1), 12.5)
    assert spmatrix_row(mat, 1) == mat_row


def test_spmatrix_col_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    mat_col = spmatrix_create()
    spmatrix_value_set(mat_col, position_create(2, 2), 5.0)
    assert spmatrix_col(mat, 2) == mat_col


def test_spmatrix_col_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    mat_col = spmatrix_create()
    spmatrix_value_set(mat_col, position_create(2, 2), 5.0)
    assert spmatrix_col(mat, 2) == mat_col


def test_spmatrix_diagonal_m2x2_diagonal_zero():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 1), 12.5)
    spmatrix_value_set(mat, position_create(2, 2), 5.0)
    assert spmatrix_diagonal(mat) == mat


def test_spmatrix_diagonal_m2x2_anti_diagonal_zero():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1, 2), 12.5)
    spmatrix_value_set(mat, position_create(2, 1), 5.0)
    mat_diagonal = spmatrix_create()
    assert spmatrix_diagonal(mat) == mat_diagonal

def test_spmatrix_01_spmatrix_is():
    assert spmatrix_is((0.0,)) is False


def test_spmatrix_02_spmatrix_is():
    assert spmatrix_is([0.0]) is False


def test_spmatrix_03_spmatrix_is():
    assert spmatrix_is(True) is False


def test_spmatrix_04_spmatrix_is():
    assert spmatrix_is('0.0') is False


def test_spmatrix_05_spmatrix_is():
    assert spmatrix_is([{(-1, 0): 1.0}, 0.0]) is False


def test_spmatrix_06_spmatrix_is():
    assert spmatrix_is([0.0, {(-1, 0): 1.0}]) is False


def test_spmatrix_07_spmatrix_is():
    assert spmatrix_is([0.0, {(1, 1.1): 1.0}]) is False


def test_spmatrix_08_spmatrix_is():
    assert spmatrix_is([{(1, 1.1): 1.0}, 0.0]) is False


def test_spmatrix_09_spmatrix_is():
    assert spmatrix_is([0.0, {(0, 0): '0'}]) is False


def test_spmatrix_09a_spmatrix_is():
    assert spmatrix_is([{(0, 0): '0'}, 0.0]) is False


def test_spmatrix_10_spmatrix_is():
    assert spmatrix_is([0.0, {(1, 1): 0.0}]) is False


def test_spmatrix_10a_spmatrix_is():
    assert spmatrix_is([{(1, 1): 0.0}, 0.0]) is False


def test_spmatrix_12_spmatrix_is():
    assert spmatrix_is([0.0, {(1, 1): 1.1, (2, 2, 2): 2.2}]) is False


def test_spmatrix_12a_spmatrix_is():
    assert spmatrix_is([{(1, 1): 1.1, (2, 2, 2): 2.2}, 0.0]) is False


def test_spmatrix_13_spmatrix_is():
    assert spmatrix_is([0.0, {(1, 1): 1.1, '2, 2': 2.2}]) is False


def test_spmatrix_13a_spmatrix_is():
    assert spmatrix_is([{(1, 1): 1.1, '2, 2': 2.2}, 0.0]) is False


def test_spmatrix_14_spmatrix_is():
    assert spmatrix_is([{(1, 1): 1.1, (2, 2): 2.2, (3, 3): 3.3}, 'a']) is False


def test_spmatrix_14a_spmatrix_is():
    assert spmatrix_is(['a', {(1, 1): 1.1, (2, 2): 2.2, (3, 3): 3.3}]) is False


def test_spmatrix_15_spmatrix_create():
    try:
        spmatrix_create((0.0,))
    except ValueError as error:
        assert str(error) == 'spmatrix_create: invalid arguments'


def test_spmatrix_16_spmatrix_create():
    try:
        spmatrix_create([0.0])
    except ValueError as error:
        assert str(error) == 'spmatrix_create: invalid arguments'


def test_spmatrix_17_spmatrix_create():
    try:
        spmatrix_create(False)
    except ValueError as error:
        assert str(error) == 'spmatrix_create: invalid arguments'


def test_spmatrix_18_spmatrix_create():
    try:
        spmatrix_create('0.0')
    except ValueError as error:
        assert str(error) == 'spmatrix_create: invalid arguments'


def test_spmatrix_19_spmatrix_zero_get():
    m = spmatrix_create(1e7)
    assert spmatrix_zero_get(m) == 1e7


def test_spmatrix_20_spmatrix_value_set():
    try:
        spmatrix_value_set(spmatrix_create(1e7), position_create(1, 2), (0.0,))
    except ValueError as error:
        assert str(error) == 'spmatrix_value_set: invalid arguments'


def test_spmatrix_21_spmatrix_value_set():
    try:
        spmatrix_value_set(spmatrix_create(1e7), position_create(1, 2), [0.0])
    except ValueError as error:
        assert str(error) == 'spmatrix_value_set: invalid arguments'


def test_spmatrix_22_spmatrix_value_set():
    try:
        spmatrix_value_set(spmatrix_create(1e7), position_create(1, 2), False)
    except ValueError as error:
        assert str(error) == 'spmatrix_value_set: invalid arguments'


def test_spmatrix_23_spmatrix_value_set():
    try:
        spmatrix_value_set(spmatrix_create(1e7), position_create(1, 2), '0.0')
    except ValueError as error:
        assert str(error) == 'spmatrix_value_set: invalid arguments'


def test_spmatrix_24_spmatrix_value_get():
    try:
        spmatrix_value_get(spmatrix_create(1e7), (1, 1, 0))
    except ValueError as error:
        assert str(error) == 'spmatrix_value_get: invalid arguments'


def test_spmatrix_25_spmatrix_value_get():
    m = spmatrix_create(1e7)
    assert spmatrix_zero_get(m) == 1e7
    spmatrix_value_set(m, position_create(1, 2), 12.5)
    assert spmatrix_value_get(m, position_create(1, 2)) == 12.5


def test_spmatrix_26_spmatrix_dim():
    assert spmatrix_dim(spmatrix_create()) == ()


def test_spmatrix_27_spmatrix_dim():
    m = spmatrix_create(1e7)
    spmatrix_value_set(m, position_create(10000000, 10000000), 1.0)
    spmatrix_value_set(m, position_create(10000000, 10000000), 1e7)
    assert spmatrix_dim(m) == ()


def test_spmatrix_28_spmatrix_dim():
    try:
        assert spmatrix_dim([0, {(1, 1): 1.1, (2, 2, 2): 2.2, '3, 3': 3.3}]) is not None
    except ValueError as error:
        assert str(error) == 'spmatrix_dim: invalid arguments'


def test_spmatrix_29_spmatrix_copy():
    m = spmatrix_create(1e7)
    m2 = spmatrix_copy(m)
    assert spmatrix_is(m2) is True


def test_spmatrix_30_spmatrix_copy():
    try:
        assert spmatrix_copy([0, {(1, 1): 1.1, (2, 2, 2): 2.2, '3, 3': 3.3}]) is not False
    except ValueError as error:
        assert str(error) == 'spmatrix_copy: invalid arguments'


def test_spmatrix_31_spmatrix_sparsity():
    m = spmatrix_create(1e7)
    spmatrix_value_set(m, position_create(10000000, 10000000), 1.0)
    spmatrix_value_set(m, position_create(10000000, 10000000), 1e7)
    assert spmatrix_sparsity(m) == 1.0


def test_spmatrix_32_spmatrix_sparsity():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(1, 10000000), 1.0)
    spmatrix_value_set(m, position_create(10000000, 1), 1.0)
    assert spmatrix_sparsity(m) == float( 10000000 * 10000000 - 2 ) / float(10000000 * 10000000)


def test_spmatrix_33_spmatrix_sparsity():
    try:
        assert spmatrix_sparsity([0, {(1, 1): 1.1, (2, 2, 2): 2.2, '3, 3': 3.3}]) is not None
    except ValueError as error:
        assert str(error) == 'spmatrix_sparsity: invalid arguments'


def test_spmatrix_34_spmatrix_dim():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(1, 10000000), 1.0)
    spmatrix_value_set(m, position_create(10000000, 1), 1.0)
    dim = spmatrix_dim(m)
    assert position_row(dim[0]) == 1
    assert position_col(dim[0]) == 1
    assert position_row(dim[1]) == 10000000
    assert position_col(dim[1]) == 10000000


def test_spmatrix_35_spmatrix_sparsity():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(2, 0), 1.5)
    spmatrix_value_set(m, position_create(5, 5), 1.5)
    assert spmatrix_sparsity(m) == ( 24 - 2 ) / 24.0


def test_spmatrix_36_spmatrix_zero_set():
    m = spmatrix_create(6.0)
    spmatrix_value_set(m, position_create(1, 1), 1.0)
    spmatrix_value_set(m, position_create(2, 2), 2.0)
    spmatrix_value_set(m, position_create(3, 3), 3.0)
    spmatrix_value_set(m, position_create(4, 4), 4.0)
    spmatrix_value_set(m, position_create(5, 5), 5.0)
    spmatrix_zero_set(m, 1.0)
    spmatrix_zero_set(m, 2.0)
    spmatrix_zero_set(m, 3.0)
    spmatrix_zero_set(m, 4.0)
    spmatrix_zero_set(m, 5.0)
    assert spmatrix_zero_get(m) == 5.0


def test_spmatrix_37_spmatrix_str():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(1, 2), 2.5)
    spmatrix_value_set(m, position_create(2, 4), 5.2)
    assert spmatrix_str(m, "%.2f") == '2.50 0.00 0.00\n0.00 0.00 5.20'


def test_spmatrix_38_spmatrix_str():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(4, 2), 2.5)
    spmatrix_value_set(m, position_create(5, 4), 5.2)
    assert spmatrix_str(m, "%.2f") == '2.50 0.00 0.00\n0.00 0.00 5.20'


def test_spmatrix_39_spmatrix_str():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(4, 2), 2.5)
    spmatrix_value_set(m, position_create(5, 4), 5.2)
    assert spmatrix_str(m, "%.3f") == '2.500 0.000 0.000\n0.000 0.000 5.200'


def test_spmatrix_40_spmatrix_str():
    try:
        assert spmatrix_str([0, {(1, 1): 1.1, (2, 2, 2): 2.2, '3, 3': 3.3}], "%.2f") is not None
    except ValueError as error:
        assert str(error) == 'spmatrix_str: invalid arguments'


def test_spmatrix_41_spmatrix_row():
    m = spmatrix_create()
    lin = tuple([x for x in range(1, 100)])
    for i in lin:
        spmatrix_value_set(m, position_create(1, lin[-i]), i * 1.0)  # terceiro argumento deveria ser float ?
    m2 = spmatrix_row(m, 1)
    for i in lin:
        assert spmatrix_value_get(m2, position_create(1, lin[-i])) == \
               spmatrix_value_get(m, position_create(1, lin[-i]))


def test_spmatrix_42_spmatrix_col():
    m = spmatrix_create()
    lin = tuple([x for x in range(1, 100)])
    for i in lin:
        spmatrix_value_set(m, position_create(lin[-i], 10), i * 2.0)
    m2 = spmatrix_col(m, 10)
    for i in lin:
        assert spmatrix_value_get(m2, position_create(lin[-i], 10)) == \
               spmatrix_value_get(m, position_create(lin[-i], 10))


def test_spmatrix_43_spmatrix_diagonal():
    m = spmatrix_create(8 * 1.0) # nao devia tara passar um float ?
    spmatrix_value_set(m, position_create(1, 1), 1.1)
    spmatrix_value_set(m, position_create(5, 1), 5.0)
    spmatrix_value_set(m, position_create(1, 5), 0.5)
    spmatrix_value_set(m, position_create(5, 5), 5.5)
    m2 = spmatrix_diagonal(m)
    for i in range(1, 6):
        assert spmatrix_value_get(m2, position_create(i, i)) == \
               spmatrix_value_get(m, position_create(i, i))
    assert spmatrix_value_get(m2, position_create(5, 1)) == 8.0
    assert spmatrix_value_get(m2, position_create(1, 5)) == 8.0


def test_spmatrix_44_spmatrix_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(2, 0), 1.5)
    spmatrix_value_set(mat, position_create(5, 5), 1.5)
    try:
        assert spmatrix_diagonal(mat)
    except ValueError as error:
        assert str(error) == 'spmatrix_diagonal: matrix not square'


def test_spmatrix_45_spmatrix_diagonal():
    try:
        assert spmatrix_diagonal([0, {(1, 1): 1.1, (2, 2, 2): 2.2, '3, 3': 3.3}]) is not None
    except ValueError as error:
        assert str(error) == 'spmatrix_diagonal: invalid arguments'


def test_spmatrix_46_spmatrix_sparsity():
    seed = 100001

    def randint(a, b):
        nonlocal seed
        seed = (seed * 125) % 2796203
        return a + seed % (b - a + 1)

    vals = [position_create(randint(1, 999), randint(1, 999)) for x in range(10000)]
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(0, 0), 1.0)
    spmatrix_value_set(mat, position_create(1000, 1000), 1.0)
    for i in vals:
        spmatrix_value_set(mat, i, randint(1, 10000) * 1.0) # terceiro argumento nao deveria ser um float ?
    assert spmatrix_sparsity(mat) == (1001 * 1001 - 9631) / (1001 * 1001)

if __name__ == '__main__':
    pytest.main()