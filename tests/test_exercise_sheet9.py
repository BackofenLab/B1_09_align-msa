import pytest
from exercise_sheet9 import *


def test_exercise_1a():
    assert True

def test_exercise_1b():
    a,b,c,d,e = exercise_1b()

    assert a is True
    assert b is False
    assert c is False
    assert d is True
    assert e is True

def test_exercise_2a():
    answer = exercise_2a()

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

def test_exercise_2b():
    answer = exercise_2b()

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