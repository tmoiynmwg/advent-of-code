import sys


class CRT:
	def __init__(self, start, step, width):
		self.x = 1
		self.c = 0
		self.total_signal = 0
		self.start = start
		self.step = step
		self.width = width
		self.pixels = [[]]

	def log_signal_strength(self):
		if self.c >= self.start and (self.c - self.start) % self.step == 0:
			self.total_signal += self.c * self.x

	def draw(self):
		# Start a new row when the width is reached
		if len(self.pixels[-1]) == self.width:
			self.pixels.append([])
		# Draw pos 0 during cycle 1
		pos = (self.c - 1) % self.width
		# Draw a lit pixel if x is within 1 pixel of the current position
		if abs(pos - self.x) <= 1:
			self.pixels[-1].append('#')
		else:
			self.pixels[-1].append('.')

	def cycle(self):
		self.c += 1
		self.log_signal_strength()	# Part 1
		self.draw()					# Part 2

	def parse_instructions(self, filename):
		with open(filename) as instructions:
			for line in instructions:
				line = line.strip().lower()
				if line == 'noop':
					self.cycle()
				elif line.startswith('addx'):
					# Addition happens after 2 full cycles
					self.cycle()
					self.cycle()
					addend = int(line.split()[1])
					self.x += addend

	def print_screen(self):
		output = ''
		for row in self.pixels:
			output += '\n' + ''.join(row)
		print(output)


def main():
	device = CRT(20, 40, 40)
	device.parse_instructions(sys.argv[1])
	print(device.total_signal)	# Part 1
	device.print_screen()		# Part 2


if __name__ == "__main__":
    main()
