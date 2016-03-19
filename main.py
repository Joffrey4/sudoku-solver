# -*- coding: ascii -*-

import solver
import display
import data_structure as structs

table = ['420007010',
         '967005000',
         '008400500',
         '709020300',
         '500040006',
         '002030705',
         '004008600',
         '000200981',
         '090600074']

data_map = structs.convert_table(table)

# while not is_sudoku_solved(data_map):
for i in range(10):
    display.print_sudoku(data_map)
    data_map = solver.solve_sudoku(data_map)
    print '\n'
