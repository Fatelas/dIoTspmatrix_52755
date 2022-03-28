import pytest

from position import *

def test_position_create_valid_1_2():
    assert position_create(1,2) is not None

def test_position_create_valid_1000_0():
    assert position_create(1000,0) is not None

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

if __name__ == '__main__':
    pytest.main()