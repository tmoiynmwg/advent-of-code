
def find_product(filename, year, addends):
    with open(filename) as input_file:
        number_set = set()
        for line in input_file:
            number = int(line)

            if addends == 2:
                if year-number in number_set:
                    return number * (year-number)
                number_set.add(number)

            elif addends == 3:
                target = year - number
                for n in number_set:
                    if target-n in number_set:
                        return number * n * (target-n)
                number_set.add(number)

def main():
    print(find_product("day1-input.txt", 2020, 3))

if __name__ == "__main__":
    main()