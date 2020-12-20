import copy
import itertools

grid_size = 3

def initialize(filename, dimensions):
	assert dimensions > 1
	grid = 0
	for i in range(dimensions):
		grid = [copy.deepcopy(grid) for _ in range(grid_size)]
	#grid = [[[0] * grid_size for _ in range(grid_size)] for _ in range(grid_size)]
	# Get the plane at grid[0]...[0]
	plane = grid
	for i in range(dimensions - 2):
		plane = plane[0]
	with open(filename) as input_file:
		for y, line in enumerate(input_file):
			for x, c in enumerate(line):
				if c == '#':
					plane[y][x] = 1
	return grid

def count(grid, dimensions, val):
	#return sum(sum(sum(row) for row in plane) for plane in grid)
	total = 0
	for coords in itertools.product(range(grid_size), repeat=dimensions):
		cell = grid
		for c in coords:
			cell = cell[c]
		if cell == val:
			total += 1
	return total

def count_neighbors(grid, x, y, z):
	#mods = (-1, 0, 1)
	active_neighbors = 0
	for xn, yn, zn in itertools.product(
				(x-1, x, x+1), (y-1, y, y+1), (z-1, z, z+1)):
		if xn != x or yn != y or zn != z:
			xn %= grid_size
			yn %= grid_size
			zn %= grid_size
			active_neighbors += grid[zn][yn][xn]
	return active_neighbors

def conway(grid):
	gridc = copy.deepcopy(grid)
	for z, plane in enumerate(grid):
		for y, row in enumerate(plane):
			for x, val in enumerate(row):
				neighbors = count_neighbors(grid, x, y, z)
				if val:
					if neighbors < 2 or neighbors > 3:
						gridc[z][y][x] = 0
				else:
					if neighbors == 3:
						gridc[z][y][x] = 1
	return gridc

def main():
	filename = 'day17-input2.txt'
	"""
	# Part 1
	grid = initialize(filename, 3)
	#print(grid)
	for gen in range(6):
		#print(gen, count_active(grid))
		grid = conway(grid)
	#print(grid)
	print(count(grid, 3, '#'))
	"""
	# Part 2
	grid = initialize(filename, 4)
	print(count(grid, 4, 1))

if __name__ == "__main__":
	main()