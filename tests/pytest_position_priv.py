import pytest
import sys, os

from position import *

sys.stdout = open(os.devnull)

# PYTHONPATH=./spmatrix_pmm PYTEST_ADDOPTS="--verbosity=1 --no-header --tb=no --durations-min=1.0 --durations=0 -rN --disable-warnings --color=no" python3 -m pytest position_pytest_priv.py


def test_position_01_position_create():
	try:
		position_create(1.0, 2.0)
	except ValueError as error:
		assert str(error) == 'position_create: invalid arguments'


def test_position_02_position_create():
	assert position_create(2 ** 30, 2 ** 30) is not None


# REMOVER ESTE TESTE QUE TRUE É INT NO PYTHON
def test_position_03_position_is():
	assert position_is(True) is False


def test_position_04_position_is():
	assert position_is((1.0, 2.0)) is False


def test_position_05_position_is():
	assert position_is((0, -1)) is False


def test_position_06_position_row():
	assert position_row(position_create(0, 2)) == 0


def test_position_07_position_row():
	try:
		position_row((0, 1.1))
	except ValueError as error:
		assert str(error) == 'position_row: invalid arguments'


def test_position_08_position_row():
	try:
		position_row((0, 0, 0))
	except ValueError as error:
		assert str(error) == 'position_row: invalid arguments'


def test_position_09_position_col():
	assert position_col(position_create(1, 0)) == 0


def test_position_10_position_col():
	try:
		position_col((1.1, 0))
	except ValueError as error:
		assert str(error) == 'position_col: invalid arguments'


def test_position_11_position_col():
	try:
		position_col((0, 0, 0))
	except ValueError as error:
		assert str(error) == 'position_col: invalid arguments'


def test_position_12_position_equal():
	pos = position_create(1, 2)
	assert position_equal(pos, pos) is True


def test_position_13_position_equal():
	assert position_equal(position_create(0, 0), position_create(0, 1)) is False


def test_position_14_position_equal():
	try:
		position_equal(position_create(2, 1), (2.0, 1.0))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_15_position_equal():
	try:
		position_equal((2.0, 1.0), (2.0, 1.0))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_16_position_equal():
	try:
		position_equal(position_create(2, 1), (2, 1, 0))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_17_position_equal():
	try:
		position_equal((0, -1), (0, -1))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_18_position_equal():
	try:
		position_equal((0, 1, 2), (0, 1, 2))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_19_position_equal():
	try:
		position_equal((0.0, 1.0), (0, 1))
	except ValueError as error:
		assert str(error) == 'position_equal: invalid arguments'


def test_position_20_position_str():
	assert position_str(position_create(0, 0)) == '(0, 0)'


def test_position_21_position_str():
	assert position_str(position_create(2 ** 30, 2 ** 30)) == '(' + str(2 ** 30) + ', ' + str(2 ** 30) + ')'


def test_position_22_position_str():
	try:
		position_str((1.1, 0))
	except ValueError as error:
		assert str(error) == 'position_str: invalid arguments'


def test_position_23_position_str():
	try:
		position_str((0, 0, 1))
	except ValueError as error:
		assert str(error) == 'position_str: invalid arguments'


if __name__ == '__main__':
	pytest.main()
