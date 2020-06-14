def pretty_print(grid):
    s = ""
    for i in range(9):
        if(i % 3 == 0 and i > 0): 
            s += "-"*6*9
            s += "\n"
        for j in range(9):
            c = ""
            if(grid[i][j] is None):
                c = "X"
            else: 
                c = str(grid[i][j])
            s += "  " + c + "  "
            if((j+1) % 3 == 0 and j < 8):
                s += " | "
        s += "\n"
    return s 

def get_grid_from_filepath(filepath):
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