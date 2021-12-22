import pytest
from exercise_sheet9 import *


def refactor_alignment(alignment):
    return set([sequence.lower() for sequence in alignment])


def refactor_answer(answer):
    """
    refactor answer to make it order and case insensitive
    """

    refactored_answer = []
    for entry in answer:
        alignment = refactor_alignment(entry[0])
        score = entry[1]
        refactored_answer.append((alignment, score))

    return refactored_answer


def test_exercise_1a():
    answer = refactor_alignment(exercise_1a())

    group1 = "ctcaca", \
             "gt⬥ac⬥",

    expected = refactor_alignment(group1)

    assert answer == expected


def test_exercise_1b():
    answer = refactor_answer(exercise_1b())

    a1_expected = "ctcaca", \
                  "--cac-"
    ss1_expected = 0

    a2_expected = "ctcaca", \
                  "c--ac-"
    ss2_expected = 0

    a3_expected = "-c-ac-", \
                  "gt⬥ac⬥"
    ss3_expected = 1

    a4_expected = "c--ac-", \
                  "gt⬥ac⬥"
    ss4_expected = 1

    expected = refactor_answer([(a1_expected, ss1_expected),
                                (a2_expected, ss2_expected),
                                (a3_expected, ss3_expected),
                                (a4_expected, ss4_expected)])

    for entry in expected:
        assert entry in answer


def test_exercise_1c():
    answer = [refactor_alignment(group) for group in exercise_1c()]

    group2_1 = "ctcaca", \
               "-c-ac-", \
               "gt⬥ac⬥"

    group2_2 = "ctcaca", \
               "c--ac-", \
               "gt⬥ac⬥"

    expected = [refactor_alignment(group) for group in [group2_1, group2_2]]

    for entry in expected:
        assert entry in answer


def test_exercise_1d():
    answer_alignment = exercise_1c()
    answer_scores = exercise_1d()

    answer = refactor_answer(list(zip(answer_alignment, answer_scores)))

    group2_1 = "ctcaca", \
               "-c-ac-", \
               "gt⬥ac⬥"
    sp1 = 1

    group2_2 = "ctcaca", \
               "c--ac-", \
               "gt⬥ac⬥"
    sp2 = 2

    expected = refactor_answer([(group2_1, sp1),
                                (group2_2, sp2)])

    for entry in expected:
        assert entry in answer


def test_exercise_1e():
    answer = refactor_alignment(exercise_1e())

    group2_2 = "ctcaca", \
               "c--ac-", \
               "gt⬥ac⬥"

    excepted = refactor_alignment(group2_2)

    assert answer == excepted


def test_exercise_1f():
    answer = refactor_answer(exercise_1f())

    group2_1 = "ctcaca", \
               "-⬥cac-", \
               "-gtac-"
    SP_group2_1 = 1

    group2_2 = "ctcaca", \
               "⬥-cac-", \
               "g-tac-"
    SP_group2_2 = 1

    group2_3 = "ctcaca", \
               "⬥c-ac-", \
               "gt-ac-"
    SP_group2_3 = 1


    expected = refactor_answer([(group2_1, SP_group2_1),
                                (group2_2, SP_group2_2),
                                (group2_3, SP_group2_3)])

    for entry in expected:
        assert entry in answer


def test_exercise_2():
    correct_answer = ["physicochemical","disruptions", "substitution","nonfunctional","evolutionary","distances","identity","divergent","extrapolation","phylogenetic"]
    assert exercise2a() == correct_answer

    
########################################################
############## Programming tasks #######################
########################################################
