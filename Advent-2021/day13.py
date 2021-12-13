import sys
import copy


class FoldableGrid:

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.grid = [[False] * xsize for _ in range(ysize)]
        self.dots = 0

    def __str__(self):
        output = ''
        for y in range(self.ysize):
            for x in range(self.xsize):
                if self.grid[y][x]:
                    output += '#'
                else:
                    output += ' '
            output += '\n'
        return output
        
    def mark(self, x, y):
        if not self.grid[y][x]:
            self.dots += 1
            self.grid[y][x] = True

    def fold_up(self, fold_y):
        g = copy.deepcopy(self.grid[:fold_y])
        for y in range(fold_y, self.ysize):
            for x in range(self.xsize):
                if self.grid[y][x]:
                    y1 = 2*fold_y - y
                    if g[y1][x]:
                        self.dots -= 1
                    g[y1][x] = True
        self.ysize = fold_y
        self.grid = g

    def fold_left(self, fold_x):
        g = [self.grid[y][:fold_x] for y in range(self.ysize)]
        for y in range(self.ysize):
            for x in range(fold_x, self.xsize):
                if self.grid[y][x]:
                    x1 = 2*fold_x - x
                    if g[y][x1]:
                        self.dots -= 1
                    g[y][x1] = True
        self.xsize = fold_x
        self.grid = g


def main():
    filename, size = sys.argv[1:3]
    size = int(size)
    g = FoldableGrid(size, size)
    with open(filename) as file:
        for line in file:
            if line.isspace():
                break
            x, y = [int(n) for n in line.strip().split(',')]
            g.mark(x, y)
        for line in file:
            ins, val = line.strip().split('=')
            val = int(val)
            if ins.endswith('x'):
                g.fold_left(val)
            elif ins.endswith('y'):
                g.fold_up(val)
            print(g.dots)
    print(g)


if __name__ == "__main__":
    main()
