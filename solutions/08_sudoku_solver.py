"""
Write a function, which solves sudoku.

"""
import random
from itertools import chain


def is_in_row(grids, row_number, value):
    """
    Checks if given value is already used in specified row

    :param grids:
    :param row_number:
    :param value:
    :return: bool
    """
    return value in grids[row_number]


def is_in_column(grids, column_number, value):
    """
    Checks if given value is already used in specified column

    :param grids:
    :param column_number:
    :param value:
    :return: bool
    """
    return value in list(zip(*grids))[column_number]


def _get_flat_subgrid(grids, row_number, column_number):
    """
    Returns subgrid as flat 1 dimersion list of its values

    :param grids:
    :param row_number:
    :param column_number:
    :return: list
    """
    row_number //= 3
    column_number //= 3
    return chain.from_iterable(row[column_number * 3: (column_number + 1) * 3]
                               for row in grids[row_number * 3:(row_number + 1) * 3])


def is_in_subgrid(grids, row_number, column_number, value):
    """
    Checks if given value is allowed to use in specified subgrid

    :param grids:
    :param row_number:
    :param column_number:
    :param value:
    :return: bool
    """
    return value in list(_get_flat_subgrid(grids, row_number, column_number))


def is_value_allowed(grids, row_number, column_number, value):
    """
    Check if given value is allowed to use in specified cell at given row and column number
    :param grids:
    :param row_number:
    :param column_number:
    :param value:
    :return: bool
    """
    return (not is_in_row(grids, row_number, value) and
            not is_in_column(grids, column_number, value) and
            not is_in_subgrid(grids, row_number, column_number, value))


def get_empty_cell_coordinates(grids):
    """
    Returns 2 elements tuple with coordinates of first empty cell.

    :param grids:
    :return: tuple(int, int)
    """
    for row_no, row in enumerate(grids):
        for col_no, cell in enumerate(row):
            if not cell:
                return row_no, col_no


def solve_sudoku(grids):
    """
    Function tries to solve sudoku, filling values in-place

    :param grids:
    :return: bool - returns status if sudoku was solved
    """
    empty_cell_x_y = get_empty_cell_coordinates(grids)
    if not empty_cell_x_y:
        # no empty cell found, sudoku is solved
        return True
    row_no, col_no = empty_cell_x_y

    for val in range(1, 10):
        if is_value_allowed(grids, row_no, col_no, val):
            grids[row_no][col_no] = val
            if solve_sudoku(grids):
                return True
            grids[row_no][col_no] = None
    return False


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


def create_random_board(n=20):
    """
    Helper function to create random sudoku grids

    :param n: int - number of prefilled cells
    :return: list - 2 dimensional list (9x9)
    """
    allowed_values = range(1, 10)
    indexes = range(9)

    grids = [[None for _ in indexes] for _ in indexes]
    for _ in range(n):
        x, y = random.choice(indexes), random.choice(indexes)
        while grids[x][y]:
            x, y = random.choice(indexes), random.choice(indexes)

        val = grids[x][y]
        while not val:
            val = random.choice(allowed_values)
            val = val if is_value_allowed(grids, x, y, val) else None
        grids[x][y] = val
    return grids


def is_row_column_subgrid_solved(elements):
    """
    Helper function to check if row/column/subgrid was solved
    :param elements: list
    :return: bool
    """
    return len(set(range(1, 10)).difference(set(elements))) == 0


def is_sudoku_solved(grids):
    """
    Helper function to check if sudoku was solved.
    :param grids:
    :return: bool
    """
    all_rows_solved = all(is_row_column_subgrid_solved(row) for row in grids)
    all_cols_solved = all(is_row_column_subgrid_solved(col) for col in zip(*grids))
    all_subgrid_solved = all(is_row_column_subgrid_solved(_get_flat_subgrid(grids, x, y))
                             for x in range(9)
                             for y in range(9) if x % 3 == 0 and y % 3 == 0)
    return all_rows_solved and all_cols_solved and all_subgrid_solved


def main():
    print("Sudoku to solve:")
    random_example = create_random_board()
    print_sudoku(random_example)
    is_solved = solve_sudoku(random_example)
    if is_solved:
        print("Sudoku was solved")
    else:
        print("Sudoku was not solved")
    print_sudoku(random_example)

    assert is_solved == is_sudoku_solved(random_example)


if __name__ == '__main__':
    main()
