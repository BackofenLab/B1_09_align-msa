from typing import runtime_checkable, Tuple, List
import numpy as np


def exercise_1a():
    """
    Exercise 1 a


    """

def exercise_1b():
    """
    Exercise 1 b

    """


"""
    Given the sequences S_1 = CTCACA, S_2 = CAC, S_3 = GTAC

                  | +1 if S_i == S_j
    s(S_i, S_j) = | -1 S_i or S_j is a gap
                  | 0 if S_i != S_j or S_i AND S_j are both gaps

    We want to do progressive alignment following Feng and Doolittle.
    The needed pairwise alignments are calculated using the Needleman-Wunsch
    and are as follows:

    A_12        A_13        A_23
    CTCACA      CTCACA      GTAC
    --CAC-      GT-AC-      -CAC

    In the following the guide trees are given in Newick format.
"""
def exercise_2a():
    """
    Exercise 2 a

    Given the guide tree ((S_1, S_2), S_3), what are the possible
    resulting multiple sequence alignments.

    Use the Needleman-Wunsch implementation of the Freiburg RNA tools webserver
    to recomputethe pairwise alignments. (check README should the webserver be unavailable)

    Replace place-holder symbols with gap symbols.

    Calculate the sum-of-pair scores for each of the computed alignments.
    """

    alignment1 = "------", \
                 "------", \
                 "------"
    score1 = 0

    alignment2 = "------", \
                 "------", \
                 "------"
    score2 = 0

    alignment3 = "------", \
                 "------", \
                 "------"
    score3 = 0

    return [(set(alignment1), score1), (set(alignment2), score2), (set(alignment3), score3)]

def exercise_2b():
    """
    Exercise 2 b

    What are the alignments and sum-of-pairs scores forthe guide tree ((S_2, S_3), S_1)
    """


########################################################
############## Programming tasks #######################
########################################################
