from functions.level_1_5.one_median import get_median_value
import pytest


@pytest.mark.parametrize(
    'items, expected_result',
    [
        ([], None),
        ([8, 1, 3, 2, 5, 7], 6),
        ([8, 1, 3, 2, 5], 2),
    ],
)
def test__get_median_value__success(items, expected_result):
    assert get_median_value(items) == expected_result


@pytest.mark.parametrize(
    'items, exception_type',
    [
        ([8, 1, 3, 2], IndexError),
    ],
)
def test__get_median_value__exception(items, exception_type):
    with pytest.raises(exception_type):
        get_median_value(items)
