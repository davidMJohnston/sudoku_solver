from Grid import Grid
from solver_01 import solver

if __name__ == "__main__":
	grid = Grid("....6.8....45.....8........9...7.2.41.58.9..7.27.......8....4...7..9.62.2...8...9")
	print("Original grid:")
	grid.draw()
	grid.solve(solver)
	print("Solution:")
	grid.draw()
