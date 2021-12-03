
def inc_or_dec(bit):
    if bit == '0':
        return -1
    elif bit == '1':
        return 1
    else:
        print("Non-binary input")
        return 0

def binary_list_to_decimal(list):
    num = 0
    for bit in list:
        num = 2 * num + bit
    return num

def part1(filename):
    with open(filename) as input_file:
        length = len(input_file.readline()) - 1  # newline character
        ones_minus_zeroes = [0] * length
        input_file.seek(0)   # return to beginning of file
        for line in input_file:
            for index, bit in enumerate(line.strip()):
                #print(index, bit)
                ones_minus_zeroes[index] += inc_or_dec(bit)

    gamma, epsilon = [], []
    for bit in ones_minus_zeroes:
        if bit > 0:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    return binary_list_to_decimal(gamma) * binary_list_to_decimal(epsilon)

def most_common_bit(lst, pos):
    ones_minus_zeroes = 0
    for line in lst:
        ones_minus_zeroes += inc_or_dec(line[pos])
    return 0 if ones_minus_zeroes < 0 else 1

def part2(filename):
    with open(filename) as input_file:
        oxygen = [x.strip() for x in list(input_file)]
        co2 = oxygen.copy()
        length = len(oxygen[0])
        ones_minus_zeroes = [0] * length
        input_file.seek(0)

        for index in range(length):
            if len(oxygen) <= 1:
                break
            keep = str(most_common_bit(oxygen, index))
            oxygen = [x for x in oxygen if x[index] == keep]
        for index in range(length):
            if len(co2) <= 1:
                break
            disc = str(most_common_bit(co2, index))
            co2 = [x for x in co2 if x[index] != disc]
        return int(oxygen[0], 2) * int(co2[0], 2)

def main():
    print(part1("day3-input"))
    print(part2("day3-input"))

if __name__ == "__main__":
    main()