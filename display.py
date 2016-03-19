# -*- coding: ascii -*-


def print_sudoku(data_map):
    print '-------------------'

    for i in range(1, 10):
        line = '| '

        for j in range(1, 10):
            line += str(data_map.get((i, j), 0))
            if not j % 3:
                line += ' | '

        if not i % 3:
            line += '\n-------------------'

        print line
