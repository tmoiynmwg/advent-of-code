
def follow_directions(filename, pos, depth):
    with open(filename) as input_file:
        for line in input_file:
            command, param = line.split(" ")
            command = command.lower()
            param = int(param)

            if command == "forward":
                pos += param
            elif command == "down":
                depth += param
            elif command == "up":
                depth -= param
    return [pos, depth]

def follow_aim(filename, pos, depth, aim):
    with open(filename) as input_file:
        for line in input_file:
            command, param = line.split(" ")
            command = command.lower()
            param = int(param)

            if command == "forward":
                pos += param
                depth += aim * param
            elif command == "down":
                aim += param
            elif command == "up":
                aim -= param
    return [pos, depth]

def main():
    pos, depth = follow_directions("day2-input", 0, 0)
    print(f"{pos} * {depth} = {pos * depth}")
    pos, depth = follow_aim("day2-input", 0, 0, 0)
    print(f"{pos} * {depth} = {pos * depth}")

if __name__ == "__main__":
    main()