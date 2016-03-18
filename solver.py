def solve_sudoku(data_map):
    """Check each sudoku's cell and try to solve it.
    
    Parameter:
    ----------
        data_map: the sudoku's data (dict).
        
    Return:
    -------
        data_map: the solved sudoku's data (dict).
    """
    # Prend chacune des cases
    for i in range(1, 10):
        for j in range(1, 10):

            # Vérifie qu'elles ne sont pas déjà remplies.
            if not data_map.has_key((i, j)):
                available_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                # Regarde les numéros entré sur sa ligne et les supprime de la liste.
                for line in range(1, 10):
                    if data_map.has_key((line, j)):
                        if data_map[(line, j)] in available_number:
                            available_number.remove(data_map[(line, j)])

                # Regarde les numéros entré sur sa collone et les supprime de la liste.
                for collumn in range(1, 10):
                    if data_map.has_key((i, collumn)):
                        if data_map[(i, collumn)] in available_number:
                            available_number.remove(data_map[(i, collumn)])

                # Regarde les numéros entrés dans la case et les supprime de la liste.
                if (i, j) >= (1, 1) and (i, j) <= (3, 3):
                    available_number = explore_cell(data_map, available_number, (1, 1))
                elif (i, j) >= (4, 1) and (i, j) <= (6, 3):
                    available_number = explore_cell(data_map, available_number, (4, 1))
                elif (i, j) >= (7, 1) and (i, j) <= (9, 3):
                    available_number = explore_cell(data_map, available_number, (7, 1))
                elif (i, j) >= (1, 4) and (i, j) <= (3, 6):
                    available_number = explore_cell(data_map, available_number, (1, 4))
                elif (i, j) >= (4, 4) and (i, j) <= (6, 6):
                    available_number = explore_cell(data_map, available_number, (4, 4))
                elif (i, j) >= (7, 4) and (i, j) <= (9, 6):
                    available_number = explore_cell(data_map, available_number, (7, 4))
                elif (i, j) >= (1, 7) and (i, j) <= (3, 9):
                    available_number = explore_cell(data_map, available_number, (1, 7))
                elif (i, j) >= (4, 7) and (i, j) <= (6, 9):
                    available_number = explore_cell(data_map, available_number, (4, 7))
                elif (i, j) >= (7, 7) and (i, j) <= (9, 9):
                    available_number = explore_cell(data_map, available_number, (7, 7))

                # S'il n'y a qu'une possibilité pour compléter la case, on la complète.
                if len(available_number) == 1:
                    data_map[(i, j)] = available_number[0]

    return data_map


def explore_cell(data_map, available_number, begin_coord):
    # Parcours chaque case de la cellule
    for i in range(3):
        for j in range(3):

            # Supprime le numéro de available_number s'il existe déjà.
            if data_map.has_key((begin_coord[0] + i, begin_coord[1] + j)):
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