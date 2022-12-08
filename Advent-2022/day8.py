import sys
from enum import Enum
from math import prod


class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Tree:
    def __init__(self, height):
        self.height = height
        self.visible = False
        self.neighbors = [None] * len(Dir)

    def __gt__(self, other):
        return self.height > other.height

    def __ge__(self, other):
        return self.height >= other.height

    def mark_visible(self):
        if self.visible:
            return 0
        else:
            self.visible = True
            return 1

    def link(self, direction, other):
        self.neighbors[direction.value] = other

    def look(self, direction):
        visible_trees = 0
        tree = self.neighbors[direction.value]
        while tree is not None:
            visible_trees += 1
            if tree >= self:
                break
            tree = tree.neighbors[direction.value]
        return visible_trees

    def scenic_score(self):
        # Multiply the number of visible trees in the 4 cardinal directions
        return prod(self.look(d) for d in Dir)


class Grid:
    MAX_HEIGHT = 9

    def __init__(self, filename):
        self.grid = []
        with open(filename) as input_file:
            for line in input_file:
                row = []
                for c in line.strip():
                    height = int(c)
                    row.append(Tree(height))
                self.grid.append(row)
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])

        for y in range(self.num_rows):
            for x in range(self.num_cols):
                tree = self.grid[y][x]
                if y > 0:
                    tree.link(Dir.UP, self.grid[y-1][x])
                if y < self.num_rows - 1:
                    tree.link(Dir.DOWN, self.grid[y+1][x])
                if x > 0:
                    tree.link(Dir.LEFT, self.grid[y][x-1])
                if x < self.num_cols - 1:
                    tree.link(Dir.RIGHT, self.grid[y][x+1])

    def count_visible_trees(self):
        if self.num_rows < 3 or self.num_cols < 3:
            # Grid is too small so all trees are visible
            return self.num_rows * self.num_cols
        # Automatically count the 4 corners
        total_vis = 4

        # Look from left and right skipping the top and bottom rows
        for row in self.grid[1:-1]:
            treeline = row[0]
            vis_left = treeline.mark_visible()
            for tree in row[1:]:
                if treeline.height == self.MAX_HEIGHT:
                    break
                if tree > treeline:
                    treeline = tree
                    vis_left += tree.mark_visible()

            treeline = row[-1]
            vis_right = treeline.mark_visible()
            for tree in row[-2::-1]:
                if treeline == self.MAX_HEIGHT:
                    break
                if tree > treeline:
                    treeline = tree
                    vis_right += tree.mark_visible()
            total_vis += vis_left + vis_right

        # Look from top and bottom skipping the left- and right-most columns
        for x in range(1, self.num_cols - 1):
            col = [row[x] for row in self.grid]
            treeline = col[0]
            vis_top = treeline.mark_visible()
            for tree in col[1:]:
                if treeline == self.MAX_HEIGHT:
                    break
                if tree > treeline:
                    treeline = tree
                    vis_top += tree.mark_visible()

            treeline = col[-1]
            vis_bottom = treeline.mark_visible()
            for tree in col[-2::-1]:
                if treeline == self.MAX_HEIGHT:
                    break
                if tree > treeline:
                    treeline = tree
                    vis_bottom += tree.mark_visible()
            total_vis += vis_top + vis_bottom
        return total_vis

    def max_scenic_score(self):
        high_score = 0
        # Again, ignore the borders as they all have a product of 0
        for row in self.grid[1:-1]:
            for tree in row[1:-1]:
                score = tree.scenic_score()
                if score > high_score:
                    high_score = score
        return high_score


# Pass filename as first argument to script!
def main():
    g = Grid(sys.argv[1])
    print(g.count_visible_trees())  # Part 1
    print(g.max_scenic_score())     # Part 2


if __name__ == "__main__":
    main()