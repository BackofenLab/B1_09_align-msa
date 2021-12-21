from typing import runtime_checkable, Tuple, List
import numpy as np


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
def exercise_1a():
    """
    Exercise 1 a

    Starting with the guide tree ((S1, S3), S2), what would be the starting group1?

    Remember to use the place-holder symbol for gaps: ⬥ (in our case)
    """


    group1 = "------", \
             "------",

    return group1

def exercise_1b():
    """
    Exercise 1 b

    Use the Needleman-Wunsch algorithm to generate all pairwise alignments
    against group1 and calculate their respective similarity score.

    Order of sequences and alignments does not matter.
    Remember to use the place-holder symbol for the gaps in sequences of group1
    """

    alignment1 = "------", \
                 "------"
    similarity_score1 = 0

    alignment2 = "------", \
                 "------"
    similarity_score2 = 0

    alignment3 = "------", \
                 "------"
    similarity_score3 = 0

    alignment4 = "------", \
                 "------"
    similarity_score4 = 0

    return [(alignment1, similarity_score1),
            (alignment2, similarity_score2),
            (alignment3, similarity_score3),
            (alignment4, similarity_score4)]


def exercise_1c():
    """
    Exercise 1 c

    Based on the previously calculated pairwise alignments what are the possible choices for group2?

    """

    group2_1 = "------", \
               "------", \
               "------"

    group2_2 = "------", \
               "------", \
               "------"

    return [group2_1, group2_2]

def exercise_1d():
    """
    Exercise 1 d

    Calculate the sum-of-pairs scores for each of the possible group2 choices.

    Remember to replace the placeholder symbols with gaps for the calculation of the SP scores
    """

    SP_group2_1 = None
    SP_group2_2 = None

    return [SP_group2_1, SP_group2_2]

def exercise_1e():
    """
    Exercise 1 e

    Which alignment will be chosen as group2 for the next step?

    Remember to use the place-holder symbol for gaps: ⬥ (in our case)
    """

    group2 = "------", \
             "------", \
             "------"

    return group2

def exercise_1f():
    """
    Exercise 1 f

    Based on what you have learned, what are the alignments
    and sum-of-pairs scores for the guide tree ((S2, S3), S1)?
    """

    group2_1 = "------", \
               "------", \
               "------"
    SP_group2_1 = 0

    group2_2 = "------", \
               "------", \
               "------"
    SP_group2_2 = 0

    group2_3 = "------", \
               "------", \
               "------"
    SP_group2_3 = 0

    return [(group2_1, SP_group2_1),
            (group2_2, SP_group2_2),
            (group2_3, SP_group2_3)]

########################################################
############## Programming tasks #######################
########################################################
