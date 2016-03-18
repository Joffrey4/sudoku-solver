import solver
import display
import data_structure as struct

table = ['000608430',
         '308570062',
         '704000800',
         '205700010',
         '080000020',
         '070006508',
         '009000105',
         '850041203',
         '037802000']

data_map = struct.convert_table(table)

# while not is_sudoku_solved(data_map):
for i in range(10):
    display.print_sudoku(data_map)
    data_map = solver.solve_sudoku(data_map)
    print '\n'
