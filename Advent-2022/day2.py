import sys


def convert_shape(char):
    if char == 'A' or char == 'X':
        return 1    # rock
    if char == 'B' or char == 'Y':
        return 2    # paper
    if char == 'C' or char == 'Z':
        return 3    # scissors
    raise TypeError(f'Character {char} not recognized as rock, paper, or scissors')


def convert_result(char):
    if char == 'X':
        return 0    # lose
    if char == 'Y':
        return 3    # draw
    if char == 'Z':
        return 6    # win
    raise TypeError(f'Character {char} not recognized as win, loss, or draw')


def matchup(them, us):
    if (them - us) % 3 == 1:
        return 0    # lose
    if them == us:
        return 3    # draw
    if (them - us) % 3 == 2:
        return 6    # win
    raise TypeError(f'them {them} and us {us} must be 1, 2, or 3')


def need_to_play(them, result):
    if result == 'X':
        play = them - 1
        if play == 0:
            play = 3
    if result == 'Y':
        play = them
    if result == 'Z':
        play = them + 1
        if play == 4:
            play = 1
    return play


def rps_points(filename, part1):
    total = 0
    with open(filename) as input_file:
        for line in input_file:
            if part1:
                them, us = [convert_shape(char) for char in line.split()]
                total += us
                total += matchup(them, us)

            else:
                them, result = line.split()
                them = convert_shape(them)
                total += need_to_play(them, result)
                total += convert_result(result)
    return total


def main():
    print(rps_points("day2-input", True))
    print(rps_points("day2-input", False))


if __name__ == "__main__":
    main()