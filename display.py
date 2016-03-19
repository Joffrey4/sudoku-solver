# -*- coding: ascii -*-


def print_sudoku(data_map):
    for i in range(1, 10):
        line = ''
        for j in range(1, 10):
            line += str(data_map.get((i, j), 0))
        print line
    print '\n'
