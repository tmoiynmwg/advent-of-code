import sys, math


class HeightMap:

	def __init__(self, filename):
		self.grid = []
		with open(filename) as file:
			for line in file:
				self.grid.append([int(c) for c in line.strip()])
		self.height = len(self.grid)
		self.width = len(self.grid[0])
		self.marked = [[False] * self.width for _ in range(self.height)]

	def __str__(self):
		output = ''
		for row in self.grid:
			output += str(row) + '\n'
		return output

	def risk_level(self, row, col):
		return self.grid[row][col] + 1

	def neighbors(self, row, col):
		nb = []
		if row > 0:
			nb.append(self.grid[row - 1][col])
		if row < self.height - 1:
			nb.append(self.grid[row + 1][col])
		if col > 0:
			nb.append(self.grid[row][col - 1])
		if col < self.width - 1:
			nb.append(self.grid[row][col + 1])
		return nb

	def is_low_point(self, row, col):
		height = self.grid[row][col]
		nb = self.neighbors(row, col)
		return height < min(nb)

	def low_points(self):
		lp = []
		for r in range(self.height):
			for c in range(self.width):
				if self.is_low_point(r, c):
					lp.append((r, c))
		return lp

	def basin_size(self, row, col):
		"""Flow up from a low point and count unmarked nodes 
		until a 9 or plateau is reached.
		"""
		val = self.grid[row][col]
		if val >= 9 or self.marked[row][col]:
			return 0
		#hm = self.grid.copy()
		self.marked[row][col] = True
		node_count = 1
		if row > 0 and self.grid[row - 1][col] > val:
			node_count += self.basin_size(row - 1, col)
		if col > 0 and self.grid[row][col - 1] > val:
			node_count += self.basin_size(row, col - 1)
		if row < self.height - 1 and self.grid[row + 1][col] > val:
			node_count += self.basin_size(row + 1, col)
		if col < self.width - 1 and self.grid[row][col + 1] > val:
			node_count += self.basin_size(row, col + 1)
		return node_count


def main():
    filename = sys.argv[1]
    hm = HeightMap(filename)
    lp = hm.low_points()
    total_risk = 0
    for row, col in lp:
    	total_risk += hm.risk_level(row, col)
    print(total_risk)
    basins = sorted([hm.basin_size(r, c) for r, c in lp])
    print(math.prod(basins[-3:]))


if __name__ == "__main__":
    main()