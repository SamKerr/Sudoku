import solver
import printer

def getGrid(filepath):
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
    grid = getGrid("hard.txt")
    print(grid)
    solver = solver.SudokuSolver()
    answer = solver.solve(grid)
    if(answer is None):
        print("No answer found :(")
    else:
        prettyAnswer = printer.prettyPrint(answer)
        print(prettyAnswer)


