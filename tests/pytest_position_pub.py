import pytest
import sys, os

from position import *

sys.stdout = open(os.devnull)

# PYTHONPATH=./spmatrix_pmm PYTEST_ADDOPTS="--verbosity=1 --no-header --tb=no --durations-min=1.0 --durations=0 -rN --disable-warnings --color=no" python3 -m pytest position_pytest_pub.py


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


def test_position_12():
	pos = position_create(1, 2)
	assert position_equal(pos, pos) is True


if __name__ == '__main__':
	pytest.main()
