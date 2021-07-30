from sudoku import Sudoku
import sys 

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Please input a path to the sudoku puzzle text file. Example: python main.py path/to/file.txt")
    else:    
        print(f"loading file: {sys.argv[1]}")
        print(f"Press p to run solver")
        print(f"Press q to quit")
        game = Sudoku(sys.argv[1])
        game.event_loop()
        

