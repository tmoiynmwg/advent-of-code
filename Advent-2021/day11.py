import sys


class Octopodes:

	def __init__(self, filename):
		self.grid = []
		with open(filename) as file:
			for line in file:
				self.grid.append([int(c) for c in line.strip()])
		self.height = len(self.grid)
		self.width = len(self.grid[0])
		self.flash_threshold = 10
		self.flash_count = 0
		self.synchronized = False

	def __str__(self):
		output = ''
		for row in self.grid:
			output += str(row) + '\n'
		return output

	def inc(self, row, col):
		"""Generate a flash iff the cell reached exactly 10."""
		if 0 <= row < self.height and 0 <= col < self.width:
			self.grid[row][col] += 1
			if self.grid[row][col] == self.flash_threshold:
				self.flash(row, col)

	def flash(self, row, col):
		"""Increment each neighboring cell."""
		self.flash_count += 1
		for r in (-1, 0, 1):
			for c in (-1, 0, 1):
				if r != 0 or c != 0:
					self.inc(row + r, col + c)

	def step(self):
		"""Increment each octopus, then reset flashed cells to 0."""
		for r in range(self.height):
			for c in range(self.width):
				self.inc(r, c)
		self.synchronized = True
		for r in range(self.height):
			for c in range(self.width):
				if self.grid[r][c] >= self.flash_threshold:
					self.grid[r][c] = 0
				else:
					self.synchronized = False


def main():
    filename, steps = sys.argv[1:3]
    steps = int(steps)
    octo = Octopodes(filename)
    for s in range(steps):
    	octo.step()
    	if octo.synchronized:
    		break
    print(octo)
    print('Steps: ', s + 1)
    print('Flashes: ', octo.flash_count)


if __name__ == "__main__":
    main()
