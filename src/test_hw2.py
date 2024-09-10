"""Module to test"""
import hw2_debugging


def test_merge_1():
    """Empty array test"""
    assert hw2_debugging.merge_sort([]) == []


def test_merge_2():
    """Test with an already sorted array"""
    assert hw2_debugging.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_3():
    """Test with an arbitrarily ordered array with repeated elements"""
    assert hw2_debugging.merge_sort([4, 4, 4, 1, 3]) == [1, 3, 4, 4, 4]
