# -*- coding: ascii -*-

import solver
import display
import data_structure as structs

table = ['020800690',
         '800009007',
         '009026000',
         '090410005',
         '058000710',
         '300058060',
         '000360400',
         '900200008',
         '043007050']

data_map = structs.convert_table(table)

# Solve the sudoku.
while not solver.is_sudoku_solved(data_map):
    data_map = solver.solve_sudoku(data_map)

display.print_sudoku(data_map)
