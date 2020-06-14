import solver
import printer

def get_grid(filepath):
    grid = []
    with open(filepath, 'r') as f:
        for line in f:
            row = []
            vals = line.rstrip().split(" ")
            for v in vals: 
                if(v == 'X'):
                    row.append(None)
                else:
                    row.append(int(v))
            grid.append(row)
    return grid


if __name__ == "__main__":
    grid = get_grid("hard.txt")
    print(grid)
    solver = solver.SudokuSolver()
    answer = solver.solve(grid)
    if(answer is None):
        print("No answer found :(")
    else:
        prettyAnswer = printer.pretty_print(answer)
        print(prettyAnswer)


