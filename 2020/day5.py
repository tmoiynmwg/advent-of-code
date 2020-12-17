def convert_to_binary(string):
    binary = ''
    for c in string:
        if c == 'F' or c == 'L':
            binary += '0'
        elif c == 'B' or c == 'R':
            binary += '1'
    return int(binary, 2)

def generate_seatIDs(filename):
    with open(filename) as input_file:
        return set(map(convert_to_binary, input_file))

def main():
    occupied_seats = generate_seatIDs('day5-input.txt')
    # Part 1
    print(max(occupied_seats))
    # Part 2
    for s in range(min(occupied_seats) + 1, max(occupied_seats) - 1):
        if s not in occupied_seats:
            print(s)
            break

if __name__ == "__main__":
    main()