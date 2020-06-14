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