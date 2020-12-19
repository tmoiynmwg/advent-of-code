def counting_game(starting_numbers, target):
    last_index = {}
    for i, n in enumerate(starting_numbers[:-1]):
        last_index[n] = i
    last_num = starting_numbers[-1]
    for i in range(len(starting_numbers) - 1, target - 1):
        if last_num in last_index:
            new_num = i - last_index[last_num]
        else:
            new_num = 0
        last_index[last_num] = i
        last_num = new_num
    return last_num

def main():
    starting_numbers = [11,18,0,20,1,7,16]
    print(counting_game(starting_numbers, 2020))
    print(counting_game(starting_numbers, 30000000))

if __name__ == "__main__":
    main()
