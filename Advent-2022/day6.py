import sys


def find_no_repeats(string, length):
    for i in range(length, len(string)):
        substr = string[i-length:i]
        if len(set(substr)) == len(substr):
            return i


# Not needed - misunderstood part 2
def find_distinct_characters(string, num):
    chars = set()
    for i, c in enumerate(string):
        chars.add(c)
        if len(chars) == num:
            return i + 1


def main():
    with open('day6-input') as filename:
        data = filename.read()
    print(find_no_repeats(data, 4))     # Part 1
    print(find_no_repeats(data, 14))    # Part 2


if __name__ == "__main__":
    main()