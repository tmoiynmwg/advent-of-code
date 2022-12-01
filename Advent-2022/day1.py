import sys


def calorie_totals(filename):
    totals = []
    with open(filename) as input_file:
        subtotal = 0
        for line in input_file:
            if line.isspace():
                totals.append(subtotal)
                subtotal = 0
            else:
                subtotal += int(line)
        if subtotal > 0:
            totals.append(subtotal)
    return totals


def main():
    calories = calorie_totals("day1-input")
    print(max(calories))                # part 1
    print(sum(sorted(calories)[-3:]))   # part 2


if __name__ == "__main__":
    main()