from task7idea import division
import pytest


# $py -m pytest --html=report.html test_7idea.py
# Run from terminal for generating html report
# report.html - where 'report' is name of file
# more info see on https://pytest-html.readthedocs.io/en/latest/user_guide.html


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 2, 0),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_answer(a, b, expected_result):
    assert division(a, b) == expected_result

# def test_division_answer():
#     assert division(10, 2) == 5
