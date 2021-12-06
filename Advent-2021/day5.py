class Grid:
    def __init__(self, xsize, ysize):
        self.grid = [[0] * xsize for _ in range(ysize)]
        self.overlaps = 0

    def __str__(self):
        output = ''
        for row in self.grid:
            for cell in row:
                if cell == 0:
                    output += '.'
                else:
                    output += str(cell)
            output += '\n'
            #print(output)
        return output

    def increment(self, x, y):
        self.grid[y][x] += 1
        if self.grid[y][x] == 2:
            self.overlaps += 1

    def import_lines(self, filename, diagonals):
        with open(filename) as input_file:
            for line in input_file:
                # x1, y1, x2, y2 = [c.split(',') for p in 
                # line.split(' -> ') for c in p.split(',')]
                coords1, coords2 = line.split(' -> ')
                x1, y1 = [int(c) for c in coords1.split(',')]
                x2, y2 = [int(c) for c in coords2.split(',')]
                if x1 == x2:
                    y1, y2 = (y2, y1) if y1 > y2 else (y1, y2)
                    for y in range(y1, y2+1):
                        self.increment(x1, y)
                    #print(self)
                elif y1 == y2:
                    x1, x2 = (x2, x1) if x1 > x2 else (x1, x2)
                    for x in range(x1, x2+1):
                        self.increment(x, y1)
                    #print(self)
                elif diagonals:
                    xstep = -1 if x1 > x2 else 1
                    ystep = -1 if y1 > y2 else 1
                    for x, y in zip(range(x1, x2+xstep, xstep), 
                                    range(y1, y2+ystep, ystep)):
                        self.increment(x, y)

def main():
    size = 1000
    g = Grid(size, size)
    #str(g)
    #print(g)
    g.import_lines("day5-input", True)
    #print(g)
    print(g.overlaps)

if __name__ == "__main__":
    main()