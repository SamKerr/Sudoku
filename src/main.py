from sudoku_class import Sudoku

if __name__ == "__main__":
    game = Sudoku("input/hard.txt")
    game.play_with_solver()

