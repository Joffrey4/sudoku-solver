def convert_table(table):
    """Generate 9x9 sudoku table from sudoku data.
    It convert an inputed sudoku data into a dictionnary of positions.

    Paramater:
    ----------
        table: a list of the sudoku table (list).
    Return:
    -------
        data_map: the sudoku's data (dict).
    """
    data_map = {}

    # Parcours chaque case.
    for i in range(9):
        for j in range(9):

            # Enregistre la case si elle contient un chiffre.
            if not table[i][j] == '0':
                data_map[(i + 1, j + 1)] = int(table[i][j])

    return data_map