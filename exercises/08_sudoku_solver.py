"""
Write a function, which solves sudoku.

"""

SUDOKU_TEST_EXAMPLE = [
    [None, 2, None, 5, None, 1, None, 9, None],
    [8, None, None, 2, None, 3, None, None, 6],
    [None, 3, None, None, 6, None, None, 7, None],
    [None, None, 1, None, None, None, 6, None, None],
    [5, 4, None, None, None, None, None, 1, 9],
    [None, None, 2, None, None, None, 7, None, None],
    [None, 9, None, None, 3, None, None, 8, None],
    [2, None, None, 8, None, 4, None, None, 7],
    [None, 1, None, 9, None, 7, None, 6, None]
]

SUDOKU_TEST_EXAMPLE_SOLVED = [
    [4, 2, 6, 5, 7, 1, 3, 9, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2]
]


def print_sudoku(grids):
    """
    Prints sudoku grids to stdout.

    :param grids:
    :return: None
    """
    for row_no, row in enumerate(grids):
        if row_no % 3 == 0:
            print("-" * 25)
        row_formatted = [str(val if val else "_") for val in row]
        row_formatted.append("|")
        row_formatted.insert(6, "|")
        row_formatted.insert(3, "|")
        row_formatted.insert(0, "|")
        print(" ".join(row_formatted))
    print("-" * 25)


def solve_sudoku(grids):
    """
    Function tries to solve sudoku, filling values in-place in grids

    :param grids:
    :return: bool - returns status if sudoku was solved
    """

    return False


if __name__ == "__main__":
    print_sudoku(SUDOKU_TEST_EXAMPLE)
    solve_sudoku(SUDOKU_TEST_EXAMPLE)
    print_sudoku(SUDOKU_TEST_EXAMPLE)
    # assert SUDOKU_TEST_EXAMPLE == SUDOKU_TEST_EXAMPLE_SOLVED
