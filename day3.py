import math

def count_trees(filename, horiz, vert):
    with open(filename) as input_file:
        map = []
        for line in input_file:
            map.append(line.strip())

        x_size = len(map[0])
        trees = 0
        x, y = 0, 0

        while y < len(map):
            if map[y][x] == '#':
                trees += 1
            x = (x + horiz) % x_size
            y += vert

        return trees

def main():
    tree_count = [count_trees("day3-input.txt", 1, 1),
                  count_trees("day3-input.txt", 3, 1),
                  count_trees("day3-input.txt", 5, 1),
                  count_trees("day3-input.txt", 7, 1),
                  count_trees("day3-input.txt", 1, 2)]
    print(math.prod(tree_count))

if __name__ == "__main__":
    main()