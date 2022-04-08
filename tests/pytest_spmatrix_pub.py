import pytest
import sys, os

from spmatrix import *

sys.stdout = open(os.devnull)

# pytest spmatrix_pytest_pub.py --verbosity=1 --no-header --capture=no --color=yes --durations=0 --tb=no -rN
# PYTHONPATH=./spmatrix_pmm PYTEST_ADDOPTS="--verbosity=1 --no-header --tb=no --durations-min=1.0 --durations=0 -rN --disable-warnings --color=no" python3 -m pytest spmatrix_pytest_pub.py


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
    assert spmatrix_zero_get(spmatrix_create(2)) == 2.0


def test_spmatrix_copy_of_empty_matrix_with_zero_as_2():
    assert spmatrix_zero_get(spmatrix_copy(spmatrix_create(2))) == 2.0


def test_spmatrix_is_after_spmatrix_copy_after_spmatrix_create():
    assert spmatrix_is(spmatrix_copy(spmatrix_create())) is True


def test_spmatrix_value_set_and_spmatrix_value_get():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 12.5)
    assert spmatrix_value_get(mat, position_create(1,2)) == 12.5
    spmatrix_value_set(mat, position_create(2,1), 5.0)
    assert spmatrix_value_get(mat, position_create(2,1)) == 5.0


def test_spmatrix_value_get_after_replacing_value_with_spmatrix_value_get():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 12.5)
    assert spmatrix_value_get(mat, position_create(1,2)) == 12.5
    spmatrix_value_set(mat, position_create(1,2), 5.0)
    assert spmatrix_value_get(mat, position_create(1,2)) == 5.0


def test_spmatrix_dim_of_empty_matrix():
    assert spmatrix_dim(spmatrix_create()) == ()


def test_spmatrix_dim_of_matrix_with_one_element():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 5)
    dim = spmatrix_dim(mat)
    assert position_str(dim[0]) == '(1, 2)'
    assert position_str(dim[1]) == '(1, 2)'


def test_spmatrix_sparsity_of_m2x2_diagonal_matrix():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,1), 12.5)
    spmatrix_value_set(mat, position_create(2,2), 5.0)
    assert spmatrix_sparsity(mat) == 0.5


def test_spmatrix_sparsity_of_matrix_with_1_element_after_element_removal_using_spmatrix_zero_set():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 12.5)
    spmatrix_value_set(mat, position_create(2,1), 5.0)
    spmatrix_zero_set(mat, 12.5)
    assert spmatrix_sparsity(mat) == 0.0


def test_spmatrix_str_of_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,1), 12.5)
    spmatrix_value_set(mat, position_create(2,2), 5.0)
    assert spmatrix_str(mat, "%.1f") == '12.5 0.0\n0.0 5.0'


def test_spmatrix_row_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,1), 12.5)
    spmatrix_value_set(mat, position_create(2,2), 5.0)
    mat_row = spmatrix_create()
    spmatrix_value_set(mat_row, position_create(1,1), 12.5)
    assert spmatrix_row(mat, 1) == mat_row


def test_spmatrix_col_m2x2_diagonal():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,1), 12.5)
    spmatrix_value_set(mat, position_create(2,2), 5.0)
    mat_col = spmatrix_create()
    spmatrix_value_set(mat_col, position_create(2,2), 5.0)
    assert spmatrix_col(mat, 2) == mat_col


def test_spmatrix_diagonal_m2x2_diagonal_zero():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,1), 12.5)
    spmatrix_value_set(mat, position_create(2,2), 5.0)
    assert spmatrix_diagonal(mat) == mat


def test_spmatrix_diagonal_m2x2_anti_diagonal_zero():
    mat = spmatrix_create()
    spmatrix_value_set(mat, position_create(1,2), 12.5)
    spmatrix_value_set(mat, position_create(2,1), 5.0)
    mat_diagonal = spmatrix_create()
    assert spmatrix_diagonal(mat) == mat_diagonal


def test_spmatrix_15():
    try:
        spmatrix_create((0.0,))
    except ValueError as error:
        assert str(error) == 'spmatrix_create: invalid arguments'


def test_spmatrix_19():
    m = spmatrix_create(1e7)
    assert spmatrix_zero_get(m) == 1e7


def test_spmatrix_34():
    m = spmatrix_create()
    spmatrix_value_set(m, position_create(1, 10000000), 1.0)
    spmatrix_value_set(m, position_create(10000000, 1), 1.0)
    dim = spmatrix_dim(m)
    assert position_row(dim[0]) == 1
    assert position_col(dim[0]) == 1
    assert position_row(dim[1]) == 10000000
    assert position_col(dim[1]) == 10000000


if __name__ == '__main__':
    pytest.main()
