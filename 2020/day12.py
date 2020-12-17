import math

def vector(direction, magnitude):
    theta = math.radians(direction)
    x = magnitude * math.cos(theta)
    y = magnitude * math.sin(theta)
    return (x, y)

def angle(x, y):
    return math.degrees(math.atan2(y, x))

def rotate(x, y, degrees):
    theta = angle(x, y) + degrees
    return vector(theta, math.hypot(x, y))

def move_ship(filename):
    bearing, x, y = 0, 0, 0
    with open(filename) as input_file:
        for line in input_file:
            act, val = line[0], int(line[1:])
            if act == 'N':
                y += val
            elif act == 'S':
                y -= val
            elif act == 'E':
                x += val
            elif act == 'W':
                x -= val
            elif act == 'L':
                bearing += val
            elif act == 'R':
                bearing -= val
            elif act == 'F':
                x1, y1 = vector(bearing, val)
                x += x1
                y += y1
    return (x, y)

def move_with_waypoint(filename, wx, wy):
    sx, sy = 0, 0
    with open(filename) as input_file:
        for line in input_file:
            act, val = line[0], int(line[1:])
            if act == 'N':
                wy += val
            elif act == 'S':
                wy -= val
            elif act == 'E':
                wx += val
            elif act == 'W':
                wx -= val
            elif act == 'L':
                wx, wy = rotate(wx, wy, val)
            elif act == 'R':
                wx, wy = rotate(wx, wy, -val)
            elif act == 'F':
                sx += wx * val
                sy += wy * val
    return (sx, sy)

def manhattan(x, y):
    return abs(x) + abs(y)

def main():
    filename = 'day12-input.txt'
    # Part 1
    x, y = move_ship(filename)
    print(manhattan(x, y))
    # Part 2
    x, y = move_with_waypoint(filename, 10, 1)
    print(manhattan(x, y))

if __name__ == "__main__":
    main()
