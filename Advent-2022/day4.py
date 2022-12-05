import sys


def count_overlaps(filename, full_only):
    count = 0
    with open(filename) as input_file:
        for line in input_file:
            r1, r2 = line.strip().split(',')
            min1, max1 = [int(s) for s in r1.split('-')]
            min2, max2 = [int(s) for s in r2.split('-')]

            if full_only:   # part 1
                if ((min1 <= min2 and max1 >= max2) or 
                    (min1 >= min2 and max1 <= max2)):
                    count += 1
            else:           # part 2
                if (min1 <= min2 <= max1 or min1 <= max2 <= max1 or 
                    min2 <= min1 <= max2 or min2 <= max1 <= max2):
                    count += 1
    return count


def main():
    print(count_overlaps('day4-input', True))
    print(count_overlaps('day4-input', False))


if __name__ == "__main__":
    main()