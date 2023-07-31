"""Test file for test 3"""

from test_3 import sum_current_time


def test_sum_time_base_case_1():

    result = sum_current_time('01:02:03')

    assert result == 6


def test_sum_time_base_case_2():

    result = sum_current_time('01:01:01')

    assert result == 3


def test_sum_time_base_case_3():

    result = sum_current_time('09:09:09')

    assert result == 27


def test_sum_time_edge_case_1():

    result = sum_current_time('00:00:00')

    assert result == 0


def test_sum_time_edge_case_2():

    result = sum_current_time('11:11:11')

    assert result == 6