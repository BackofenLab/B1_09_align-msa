

def zero_init_correct(seq1, seq2):
    return [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]


def nw_init_correct(seq1, seq2, scoring):
    match, mismatch, gap, persistent_gap_score = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["persistent_gap_score"]
    )
    matrix = zero_init_correct(seq1, seq2)

    first_row = [0]
    penalty_row = 0
    for index, char in enumerate(seq2):
        if char != "_":
            penalty_row += gap
            first_row.append(penalty_row)
        else:
            first_row.append(penalty_row)
    matrix[0] = first_row

    first_column = [0]
    penalty_column = 0
    for index, char in enumerate(seq1):
        if char != "_":
            penalty_column += gap
            first_column.append(penalty_column)
        else:
            first_column.append(penalty_column)

    for column, penalty in zip(matrix, first_column):
        column[0] = penalty
    return matrix


def nw_extended_forward_correct(seq1, seq2, scoring):
    matrix = nw_init_correct(seq1, seq2, scoring)
    match_score, mismatch_score, gap_score, persistent_gap_score = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["persistent_gap_score"]
    )

    for row_index, row in enumerate(matrix[1:], 1):
        for column_index, column in enumerate(row[1:], 1):
            char_seq_1, char_seq_2 = (
                seq1[row_index - 1],
                seq2[column_index - 1],
            )

            if char_seq_1 == char_seq_2:
                no_gap_score = match_score
            elif (char_seq_1 == "_") or (char_seq_1 == "_"):
                no_gap_score = persistent_gap_score
            else:
                no_gap_score = mismatch_score

            left_diamond_score = gap_score if (char_seq_2 != "_") else persistent_gap_score
            top_diamond_score = gap_score if (char_seq_1 != "_") else persistent_gap_score

            diagonal = matrix[row_index - 1][column_index - 1] + no_gap_score
            left = matrix[row_index][column_index - 1] + left_diamond_score
            top = matrix[row_index - 1][column_index] + top_diamond_score
            max_val = max(top, left, diagonal)
            matrix[row_index][column_index] = max_val

    print("_________________")
    for row in matrix:
        print(row)
    print("_________________")
    return matrix


def previous_cells_correct(seq1, seq2, scoring, nw_matrix, cell):
    match_score, mismatch_score, gap_score, persistent_gap_score = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
        scoring["persistent_gap_score"]
    )

    prev_cells = []
    row, column = cell

    top = (row - 1, column) if row > 0 else None
    left = (row, column - 1) if column > 0 else None
    diagonal = (row - 1, column - 1) if (row > 0 and column > 0) else None

    cur_val = nw_matrix[row][column]
    char_first, char_second = seq1[row - 1], seq2[column - 1]

    if char_first == char_second:
        no_gap_score = match_score
    elif (char_first == "_") or (char_second == "_"):
        no_gap_score = persistent_gap_score
    else:
        no_gap_score = mismatch_score

    left_diamond_score = gap_score if (char_second != "_") else persistent_gap_score
    top_diamond_score = gap_score if (char_first != "_") else persistent_gap_score

    if diagonal:
        diagonal_val = nw_matrix[diagonal[0]][diagonal[1]]
        if (diagonal_val + no_gap_score) == cur_val:
            prev_cells.append(diagonal)

    if top:
        top_val = nw_matrix[top[0]][top[1]]
        if (top_val + top_diamond_score) == cur_val:
            prev_cells.append(top)

    if left:
        left_val = nw_matrix[left[0]][left[1]]
        if (left_val + left_diamond_score) == cur_val:
            prev_cells.append(left)

    return prev_cells


def build_all_traceback_paths_correct(seq1, seq2, scoring, nw_matrix):
    list_traceback_paths = []

    cell = len(nw_matrix) - 1, len(nw_matrix[0]) - 1
    frontier = [[cell]]
    while frontier:
        partial_path = frontier.pop()
        last_cell_partial = partial_path[-1]
        next_steps = previous_cells_correct(
            seq1, seq2, scoring, nw_matrix, last_cell_partial
        )
        for next_step in next_steps:
            new_traceback_path = partial_path + [next_step]
            if next_step == (0, 0):
                list_traceback_paths.append(new_traceback_path)
            else:
                frontier.append(new_traceback_path)

    return list_traceback_paths


def build_alignment_correct(seq1, seq2, alignment_path):
    align_seq1 = ""
    align_seq2 = ""

    alignment_path = alignment_path[::-1]

    prev_cell = 0, 0
    for cell in alignment_path[1:]:
        prev_row, prev_column = prev_cell
        row, column = cell

        if (row > prev_row) and (column > prev_column):
            align_seq1 += seq1[row - 1]
            align_seq2 += seq2[column - 1]

        elif row > prev_row:
            align_seq1 += seq1[row - 1]
            align_seq2 += "-"

        else:
            align_seq1 += "-"
            align_seq2 += seq2[column - 1]

        prev_cell = cell

    return align_seq1, align_seq2


def nw_complete(seq1, seq2, scoring):
    forward = nw_extended_forward_correct(seq1, seq2, scoring)
    score = forward[-1][-1]
    all_traceback = build_all_traceback_paths_correct(seq1, seq2, scoring, forward)
    alignments = [build_alignment_correct(seq1, seq2, path) for path in all_traceback]
    return score, alignments, seq1, seq2


def replace_with_diamonds(seq):
    """
    How often do you create a function which is basically a one-liner?
    Eventually you start questioning yourself as a human being.
    Later you create a funny comment, so nobody would even think that you are screaming inside.
    Pretending that everything is ok.

    Move on!
    Everything is going to be OK!
    """
    return seq.replace("-", "_")


def step1(seq1, seq2, seq3, scoring):
    a12 = nw_complete(seq1, seq2, scoring)
    a13 = nw_complete(seq1, seq3, scoring)
    a23 = nw_complete(seq2, seq3, scoring)

    return max([a12, a13, a23], key=lambda x: x[0])


def step2(existing_alignment, new_seq, scoring):
    pairs = []
    for seq in existing_alignment:
        seq_diamonds = replace_with_diamonds(seq)
        pairs.append(nw_complete(new_seq, seq_diamonds, scoring))
    print(pairs)


def main():
    # Do not forget to tell the students that we do MAXIMIZATION and not minimization

    # if this comment is still there it means nobody reads the comments
    # and nobody will ever know that i am a russian spy

    scoring = {"match": 1, "mismatch": 0, "gap_introduction": -1, "persistent_gap_score": 0}

    seq1 = "CTCACA"
    seq2 = "CAC"
    seq3 = "GTAC"

    max_align_pair = step1(seq1, seq2, seq3, scoring)
    last_seq = list({seq1, seq2, seq3}.difference(set(max_align_pair[2:])))[0]

    alignments_of_first_pair = max_align_pair[1]
    first_possible_alignment = alignments_of_first_pair[0]
    step2(first_possible_alignment, last_seq, scoring)






if __name__ == "__main__":
    main()


