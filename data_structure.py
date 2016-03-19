# -*- coding: ascii -*-


def convert_table(table):
    """Generate 9x9 sudoku table from sudoku data.
    It convert an inputted sudoku data into a dictionary of positions.

    Parameter:
    ----------
        table: a list of the sudoku table (list).
    Return:
    -------
        data_map: the sudoku's data (dict).
    """
    data_map = {}

    # Take each cell of the sudoku.
    for i in range(9):
        for j in range(9):

            # Save the cell if it has a number.
            if not table[i][j] == '0':
                data_map[(i + 1, j + 1)] = int(table[i][j])

    return data_map
