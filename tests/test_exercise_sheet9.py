import pytest
from exercise_sheet9 import *


def test_exercise_1a():
    answer = exercise_1a()

    alignment1 = "CTCACA", \
                 "--CAC-", \
                 "GT-AC-"
    score1 = 0

    alignment2 = "CTCACA", \
                 "-C-AC-", \
                 "GT-AC-"
    score2 = 1

    alignment3 = "CTCACA", \
                 "C--AC-", \
                 "GT-AC-"
    score3 = 2

    expected = [(set(alignment1), score1), (set(alignment2), score2), (set(alignment3), score3)]

    assert set(answer) == set(expected)

def test_exercise_1b():
    answer = exercise_1b()

    alignment1 = "CTCACA", \
                 "--CAC-", \
                 "-GTAC-"
    score1 = 1

    alignment2 = "CTCACA", \
                 "--CAC-", \
                 "G-TAC-"
    score2 = 1

    alignment3 = "CTCACA", \
                 "-C-AC-", \
                 "GT-AC-"
    score3 = 1

    expected = [(set(alignment1), score1), (set(alignment2), score2), (set(alignment3), score3)]

    assert set(answer) == set(expected)

########################################################
############## Programming tasks #######################
########################################################