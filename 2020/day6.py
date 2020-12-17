
def count_answers(filename, everyone):
    total = 0
    with open(filename) as input_file:
        charset = set()
        start_of_group = True
        for line in input_file:
            if line.isspace():
                total += len(charset)
                charset.clear()
                start_of_group = True
            else:
                newchars = set(line.strip())
                if start_of_group:
                    charset = newchars
                    start_of_group = False
                elif everyone:
                    charset.intersection_update(newchars)
                else:
                    charset.update(newchars)
        total += len(charset)
    return total

def main():
    print(count_answers("day6-input3.txt", False))
    print(count_answers("day6-input3.txt", True))

if __name__ == "__main__":
    main()