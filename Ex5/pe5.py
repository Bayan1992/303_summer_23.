
def create_multi_table():
    multi_table: list[list[str | int]] = [["X" if i==0 and j==0 else i if j==0 else j if i==0 else i*j for j in range(13)] for i in range(13)]
    return multi_table


import pytest
from pe5 import create_multi_table


def test_basic_1():
    multi_table = create_multi_table()
    assert multi_table[1][1] == 1


def test_basic_2():
    multi_table = create_multi_table()
    assert multi_table[12][12] == 144


@pytest.mark.xfail
def test_expected_to_fail():
    multi_table = create_multi_table()
    assert multi_table[1][1] == 2


def test_out_of_range():
    # Test IndexError
    with pytest.raises(IndexError):
        multi_table = create_multi_table()
        x = multi_table[13][13]


@pytest.mark.parametrize("row, col, expected", [(1, 1, 1), (2, 2, 4), (12, 12, 144), (1, 12, 12)])
def test_parametrized(row, col, expected):
    multi_table = create_multi_table()
    assert multi_table[row][col] == expected