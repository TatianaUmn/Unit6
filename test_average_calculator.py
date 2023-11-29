import pytest

from average_calculator import AverageCalculator


@pytest.fixture
def calculator():
    return AverageCalculator()


def test_calculate_average_with_empty_list(calculator):
    assert calculator.calculate_average([]) == 0


def test_calculate_average_with_non_empty_list(calculator):
    assert calculator.calculate_average([1, 2, 3, 4, 5]) == 3


def test_compare_averages_with_list1_greater(calculator):
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3]
    assert calculator.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"


def test_compare_averages_with_list2_greater(calculator):
    list1 = [1, 2, 3]
    list2 = [1, 2, 3, 4, 5]
    assert calculator.compare_averages(list1, list2) == "Второй список имеет большее среднее значение"


def test_compare_averages_with_equal_averages(calculator):
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    assert calculator.compare_averages(list1, list2) == "Средние значения равны"


def test_compare_averages_with_empty_lists(calculator):
    list1 = []
    list2 = []
    assert calculator.compare_averages(list1, list2) == "Средние значения равны"


def test_compare_averages_with_one_empty_list(calculator):
    list1 = []
    list2 = [1, 2, 3]
    assert calculator.compare_averages(list1, list2) == "Второй список имеет большее среднее значение"


def test_compare_averages_with_negative_numbers(calculator):
    list1 = [1, 2, 3]
    list2 = [-1, -2, -3]
    assert calculator.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"


def test_compare_averages_with_decimal_numbers(calculator):
    list1 = [1.5, 2.5, 3.5]
    list2 = [1.1, 2.2, 3.3]
    assert calculator.compare_averages(list1, list2) == "Первый список имеет большее среднее значение"
    