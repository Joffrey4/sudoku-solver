# -*- coding: ascii -*-


def solve_sudoku(data_map):
    """Check each sudoku's cell and try to solve it.
    Parameter:
    ----------
        data_map: the sudoku's data (dict).
    Return:
    -------
        data_map: the solved sudoku's data (dict).
    """
    # Take each cell of the sudoku.
    for i in range(1, 10):
        for j in range(1, 10):

            # Check if the cell isn't filled yet.
            if not (i, j) in data_map:
                # Define a list of all possible number to fill.
                available_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                # Check the numbers on the line correspond to the cell, and delete it from the list.
                for line in range(1, 10):
                    if (line, j) in data_map and data_map[(line, j)] in available_number:
                        available_number.remove(data_map[(line, j)])

                # Check the numbers on the column correspond to the cell, and delete it from the list.
                for column in range(1, 10):
                    if (i, column) in data_map and data_map[(i, column)] in available_number:
                        available_number.remove(data_map[(i, column)])

                # Check the numbers that are in the big cell (3x3) correspond to the cell.
                if 1 <= i <= 3 and 1 <= j <= 3:
                    available_number = explore_cell(data_map, available_number, (1, 1))
                elif 1 <= i <= 3 and 4 <= j <= 6:
                    available_number = explore_cell(data_map, available_number, (1, 4))
                elif 1 <= i <= 3 and 7 <= j <= 9:
                    available_number = explore_cell(data_map, available_number, (1, 7))
                elif 4 <= i <= 6 and 1 <= j <= 3:
                    available_number = explore_cell(data_map, available_number, (4, 1))
                elif 4 <= i <= 6 and 4 <= j <= 6:
                    available_number = explore_cell(data_map, available_number, (4, 4))
                elif 4 <= i <= 6 and 7 <= j <= 9:
                    available_number = explore_cell(data_map, available_number, (4, 7))
                elif 7 <= i <= 9 and 1 <= j <= 3:
                    available_number = explore_cell(data_map, available_number, (7, 1))
                elif 7 <= i <= 9 and 4 <= j <= 6:
                    available_number = explore_cell(data_map, available_number, (7, 4))
                elif 7 <= i <= 9 and 7 <= j <= 9:
                    available_number = explore_cell(data_map, available_number, (7, 7))

                # In the list, if there's one number left, it's saved.
                if len(available_number) == 1:
                    data_map[(i, j)] = available_number[0]

    return data_map


def explore_cell(data_map, available_number, begin_coord):
    # Take a 3x3 big cell of the sudoku.
    for i in range(3):
        for j in range(3):

            # Delete the number from the list if it does already exist.
            if (begin_coord[0] + i, begin_coord[1] + j) in data_map:
                if data_map[(begin_coord[0] + i, begin_coord[1] + j)] in available_number:
                    available_number.remove(data_map[(begin_coord[0] + i, begin_coord[1] + j)])

    return available_number


def is_sudoku_solved(data_map):
    """Check the sudoku state. If the sudoku is complete, return True. If not, return False.
    Parameter:
    ----------
        data_map: the sudoku's data (dict).
    Return:
    -------
        True/False: True if the sudoku is complete. False if not (bool).
    """
    if len(data_map) == 81:
        return True
    else:
        return False


def generate_solving_list(data_map):
    """Read the sudoku and generate list of number to speed up the solving."""

    # Creation of the data structures.
    line_data = [[]] * 9
    column_data = [[]] * 9
    cell_data = [[]] * 9

    # Take each cell of the sudoku.
    for line in range(1, 10):
        for column in range(1, 10):

            # Check if the cell is filled.
            if (line, column) in data_map:

                # Save its number in the corresponding line_data's list.
                if not data_map[(line, column)] in line_data[line - 1]:
                    line_data[line - 1].append(data_map[(line, column)])

                # Save its number in the corresponding column_data's list.
                if not data_map[(line, column)] in column_data[column - 1]:
                    column_data[column - 1].append(data_map[(line, column)])

                if 1 <= line <= 3 and 1 <= column <= 3:
                    save_number_in_cell_data(0, (line, column), data_map, cell_data)
                elif 1 <= line <= 3 and 4 <= column <= 6:
                    save_number_in_cell_data(1, (line, column), data_map, cell_data)
                elif 1 <= line <= 3 and 7 <= column <= 9:
                    save_number_in_cell_data(2, (line, column), data_map, cell_data)
                elif 4 <= line <= 6 and 1 <= column <= 3:
                    save_number_in_cell_data(3, (line, column), data_map, cell_data)
                elif 4 <= line <= 6 and 4 <= column <= 6:
                    save_number_in_cell_data(4, (line, column), data_map, cell_data)
                elif 4 <= line <= 6 and 7 <= column <= 9:
                    save_number_in_cell_data(5, (line, column), data_map, cell_data)
                elif 7 <= line <= 9 and 1 <= column <= 3:
                    save_number_in_cell_data(6, (line, column), data_map, cell_data)
                elif 7 <= line <= 9 and 4 <= column <= 6:
                    save_number_in_cell_data(7, (line, column), data_map, cell_data)
                elif 7 <= line <= 9 and 7 <= column <= 9:
                    save_number_in_cell_data(8, (line, column), data_map, cell_data)

    return line_data, column_data, cell_data


def save_number_in_cell_data(cell_id, cell_coord, data_map, cell_data):
    """Function of generate_solving_list. Save the number when it's filled"""
    if not data_map[(cell_coord[0], cell_coord[1])] in cell_data[cell_id]:
        cell_data[cell_id].append(data_map[cell_coord])
    return cell_data
