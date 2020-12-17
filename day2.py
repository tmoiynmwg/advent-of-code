
def count_valid_passwords(filename, official_policy):
    with open(filename) as input_file:
        valid_passwords = 0

        for line in input_file:
            policy, password = line.split(": ")
            range, char = policy.split(" ")
            low, high = [int(x) for x in range.split("-")]

            if (official_policy):
                if (password[low-1] == char) != (password[high-1] == char):
                    valid_passwords += 1

            else:
                if low <= password.count(char) <= high:
                    valid_passwords += 1

        return valid_passwords

def main():
    print(count_valid_passwords("day2-input.txt", True))

if __name__ == "__main__":
    main()