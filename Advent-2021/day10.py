import sys, statistics


open_brack = ['(', '[', '{', '<']
close_brack = [')', ']', '}', '>']


def scan(line):
    """Scan a line and return whether it's corrupted.

    If yes, also return the corrupt closing bracket.
    If not, also return the incomplete stack.
    """
    stack = []
    for char in line:
        if char in open_brack:
            stack.append(char)
        elif char in close_brack:
            if len(stack) == 0:
                return (True, char)
            last = stack.pop()
            if open_brack.index(last) != close_brack.index(char):
                return (True, char)
    return (False, stack)


def syntax_score(char):
    if char == close_brack[0]:
        return 3
    elif char == close_brack[1]:
        return 57
    elif char == close_brack[2]:
        return 1197
    elif char == close_brack[3]:
        return 25137
    else:
        return 0


def autocomplete_score(stack):
    score = 0
    while len(stack) > 0:
        score *= 5
        score += open_brack.index(stack.pop()) + 1
    return score


def main():
    filename = sys.argv[1]
    with open(filename) as input_file:
        corrupt_score, incomplete_scores = 0, []
        for line in input_file:
            corrupt, error = scan(line)
            if corrupt:
                corrupt_score += syntax_score(error)
            else:
                incomplete_scores.append(autocomplete_score(error))
    print('Part 1 solution: ', corrupt_score)
    print('Part 2 solution: ', statistics.median(incomplete_scores))


if __name__ == "__main__":
    main()