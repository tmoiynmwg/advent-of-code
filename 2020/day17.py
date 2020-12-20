import copy
import itertools

class Matrix:
	def __init__(self, dimensions, size, filename):
		if dimensions < 2:
			raise ValueError('Matrix must have at least'
							f' 2 dimensions to import {filename}.')
		self.dim = dimensions
		self.size = size

		grid = 0
		for i in range(dimensions):
			grid = [copy.deepcopy(grid) for _ in range(size)]
		self.neigh_sum = copy.deepcopy(grid)
		#grid = [[[0] * size for _ in range(size)] for _ in range(size)]

		# Get the plane at grid[0]...[0]
		plane = grid
		for i in range(dimensions - 2):
			plane = plane[0]
		with open(filename) as input_file:
			for y, line in enumerate(input_file):
				for x, c in enumerate(line):
					if c == '#':
						plane[y][x] = 1
						prefix = [0] * (dimensions - 2)
						self.adjust_neighbors(1, *prefix, y, x)
		self.grid = grid

	def adjust_neighbors(self, val, *coords):
		# Add val to the neighbor sum of each neighbor
		for mods in itertools.product((-1, 0, 1), repeat=self.dim):
			if mods != tuple([0] * self.dim):
				new_coords = [(c+m) % self.size for c, m in zip(coords, mods)]
				cell = self.neigh_sum
				for c in new_coords[:-1]:
					cell = cell[c]
				cell[new_coords[-1]] += val

	def get(self, *coords):
		cell = self.grid
		for c in coords:
			cell = cell[c]
		return cell
	
	def neighbor_sum(self, *coords):
		cell = self.neigh_sum
		for c in coords:
			cell = cell[c]
		return cell
	
	def set(self, val, *coords):
		cell = self.grid
		for c in coords[:-1]:
			cell = cell[c]
		diff = val - cell[coords[-1]]
		if diff != 0:
			self.adjust_neighbors(diff, *coords)
		cell[coords[-1]] = val
	"""
	def add_ns(self, val, *coords):
		cell = self.neigh_sum
		for c in coords[:-1]:
			cell = cell[c]
		cell[coords[-1]] = val
	"""

	def count(self, val):
		#return sum(sum(sum(row) for row in plane) for plane in grid)
		total = 0
		for coords in itertools.product(range(self.size), repeat=self.dim):
			if self.get(*coords) == val:
				total += 1
		return total

	# Deprecated
	def count_neighbors(self, val, *coords):
		neighbors = 0
		"""
		for xn, yn, zn in itertools.product(
					(x-1, x, x+1), (y-1, y, y+1), (z-1, z, z+1)):
			if xn != x or yn != y or zn != z:
				xn %= size
				yn %= size
				zn %= size
				active_neighbors += grid[zn][yn][xn]
		"""
		for mods in itertools.product((-1, 0, 1), repeat=self.dim):
			if mods != tuple([0] * self.dim):
				new_coords = [(c+m) % self.size for c, m in zip(coords, mods)]
				if self.get(*new_coords) == val:
					neighbors += 1
		return neighbors

	def iterate_conway(self):
		matr = copy.deepcopy(self)
		"""
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
		"""
		for coords in itertools.product(range(matr.size), repeat=matr.dim):
			cell = matr.get(*coords)
			active_neighbors = matr.neighbor_sum(*coords)
			if cell:
				if active_neighbors < 2 or active_neighbors > 3:
					self.set(0, *coords)
			else:
				if active_neighbors == 3:
					self.set(1, *coords)

	def conway(self, generations):
		for gen in range(generations):
			print(gen, self.count(1))
			self.iterate_conway()
		print(generations, self.count(1))

def main():
	filename = 'day17-input.txt'
	# Part 1
	matr = Matrix(3, 20, filename)
	matr.conway(6)
	print()
	# Part 2
	matr = Matrix(4, 20, filename)
	matr.conway(6)

if __name__ == "__main__":
	main()
