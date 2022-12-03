import sys


def priority(char):
    if ord(char) > 96:  # lowercase
        return ord(char) - 96
    else:
        return ord(char) - 38


def sum_matches(filename):
    total_priority = 0
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            half = int(len(line) / 2)
            comp1, comp2 = set(line[:half]), set(line[half:])
            #print(comp1)
            #print(comp2)
            common = comp1.intersection(comp2).pop()
            #print(common)
            total_priority += priority(common)
    return total_priority


def sum_badges(filename):
    total_priority = 0
    with open(filename) as input_file:
        sacks = []
        line_num = 0
        for line in input_file:
            line = line.strip()
            sacks.append(set(line))
            line_num += 1
            if line_num % 3 == 0:
                #print(sacks)
                common = sacks[0].intersection(sacks[1], sacks[2]).pop()
                #print(common)
                total_priority += priority(common)
                sacks.clear()
    return total_priority


def main():
    filename = "day3-input"
    print(sum_matches(filename))    # part 1
    print(sum_badges(filename))     # part 2


if __name__ == "__main__":
    main()