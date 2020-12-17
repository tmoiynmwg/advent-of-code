import itertools

def import_cipher(filename, preamble_length):
    with open(filename) as input_file:
        cipher = [int(x) for x in list(input_file)]
    return (cipher[:preamble_length], cipher[preamble_length:])

def first_non_xmas_number(preamble, cipher):
    for number in cipher:
        is_xmas = False
        for a, b in itertools.combinations(preamble, 2):
            if a != b and a + b == number:
                break
        else:
            return number

        preamble.pop(0)
        preamble.append(number)

def encryption_weakness(cipher, target, min_length):
    for length in range(min_length, len(cipher)):
        for start in range(len(cipher) - length + 1):
            numbers = cipher[start:start+length]
            if sum(numbers) == target:
                return max(numbers) + min(numbers)

def main():
    preamble, cipher = import_cipher('day9-input.txt', 25)
    invalid_number = first_non_xmas_number(preamble, cipher)
    print(encryption_weakness(preamble + cipher, invalid_number, 2))

if __name__ == "__main__":
    main()