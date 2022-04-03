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
    spmatrix_value_set(mat, position_create(1, 2), 12.5)
    spmatrix_value_set(mat, position_create(2, 1), 5.0)
    spmatrix_zero_set(mat, 12.5)
    assert spmatrix_sparsity(mat) == 1.0


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


if __name__ == '__main__':
    pytest.main()
