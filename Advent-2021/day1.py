import sys

def count_increases(filename, window_size):
    window = []
    count = 0

    with open(filename) as input_file:
        for line in input_file:
            number = int(line)
            if len(window) < window_size:
                window.append(number)
            else:
                last_sum = sum(window)
                window.pop(0)
                window.append(number)
                new_sum = sum(window)
                if new_sum > last_sum:
                    count += 1
    return count

def main():
    print(count_increases("day1-input", 3))

if __name__ == "__main__":
    main()