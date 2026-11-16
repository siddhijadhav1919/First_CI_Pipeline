import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_basic_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_k_larger_than_length():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


def test_negative_k_rotates_left():
    assert rotate_list([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]


def test_k_zero_returns_new_list():
    original = [1, 2, 3]
    result = rotate_list(original, 0)
    assert result == [1, 2, 3]
    assert result is not original
