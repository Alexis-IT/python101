from task7idea import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 2, 0),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_answer(a, b, expected_result):
    assert division(a, b) == expected_result

# def test_division_answer():
#     assert division(10, 2) == 5
