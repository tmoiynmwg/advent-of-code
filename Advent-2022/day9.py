import sys
from numpy import sign


class Graph:
    def unit_vector(direction):
        if direction == 'U':
            return (0, 1)
        elif direction == 'D':
            return (0, -1)
        elif direction == 'L':
            return (-1, 0)
        elif direction == 'R':
            return (1, 0)

    def add(coords1, coords2):
        # Add 2 sets of coordinates of any iterable type
        if len(coords1) != len(coords2):
            raise TypeError(
                f'{coords1} and {coords2} must have the same dimensions')
        return [c1 + c2 for (c1, c2) in zip(coords1, coords2)]


class Rope:
    def __init__(self, length):
        self.knots = [[0, 0] for _ in range(length)]
        self.tail_positions = set()
        self.tail_positions.add((0, 0))
        
    def move_head(self, direction, distance = 1):
        for _ in range(distance):
            self.knots[0] = Graph.add(self.knots[0], 
                                      Graph.unit_vector(direction))
            self.move_knot(1)

    def move_knot(self, k):
        # Each knot will recursively follow the last iff it is not adjacent
        if 0 < k < len(self.knots):
            last_knot = self.knots[k - 1]
            curr_knot = self.knots[k]
            x_dist = last_knot[0] - curr_knot[0]
            y_dist = last_knot[1] - curr_knot[1]

            if abs(x_dist) > 1 or abs(y_dist) > 1:
                curr_knot[0] += sign(x_dist)
                curr_knot[1] += sign(y_dist)
                if k < len(self.knots) - 1:
                    self.move_knot(k + 1)
                else:
                    # Log the tail's position after it moved,
                    # then the recursion ends
                    self.tail_positions.add(tuple(curr_knot))
                    #print(curr_knot)


def main():
    short_rope = Rope(2)
    long_rope = Rope(10)
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            direction, distance = line.split()
            distance = int(distance)
            short_rope.move_head(direction, distance)   # Part 1
            long_rope.move_head(direction, distance)    # Part 2
    print(len(short_rope.tail_positions))
    print(len(long_rope.tail_positions))


if __name__ == "__main__":
    main()
