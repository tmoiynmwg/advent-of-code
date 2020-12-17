import copy

def import_map(filename):
    with open(filename) as input_file:
        matrix = [list(row.strip()) for row in list(input_file)]
    return matrix

def count_adj(matrix, r, c, val):
    count = 0
    for rdiff in (-1, 0, 1):
        rnew = r + rdiff
        if rnew >= 0 and rnew < len(matrix):
            for cdiff in (-1, 0, 1):
                if (rdiff, cdiff) == (0, 0):
                    continue
                cnew = c + cdiff
                if cnew >= 0 and cnew < len(matrix[rnew]):
                    if matrix[rnew][cnew] == val:
                        count += 1
    return count

def count_los(matrix, r, c, val):
    count = 0
    for rdir in (-1, 0, 1):
        for cdir in (-1, 0, 1):
            if (rdir, cdir) == (0, 0):
                continue
            rnew, cnew = r, c
            while True:
                rnew += rdir
                cnew += cdir
                if (rnew < 0 or cnew < 0 or rnew >= len(matrix)
                                         or cnew >= len(matrix[rnew])):
                    break
                cell = matrix[rnew][cnew]
                if cell == val:
                    count += 1
                    break
                elif cell != '.':
                    # Found a seat in this direction that doesn't match
                    break
    return count

def step(matrix, use_los, threshold):
    new_matrix = copy.deepcopy(matrix)
    for r, row in enumerate(matrix):
        for c, cell in enumerate(row):
            if cell == 'L':
                if use_los:
                    if count_los(matrix, r, c, '#') == 0:
                        new_matrix[r][c] = '#'
                else:
                    if count_adj(matrix, r, c, '#') == 0:
                        new_matrix[r][c] = '#'
            elif cell == '#':
                if use_los:
                    if count_los(matrix, r, c, '#') >= threshold:
                        new_matrix[r][c] = 'L'
                else:
                    if count_adj(matrix, r, c, '#') >= threshold:
                        new_matrix[r][c] = 'L'
    return new_matrix

def final_state(matrix, use_los, threshold):
    matrix2 = []
    while matrix != matrix2:
        matrix2 = matrix
        matrix = step(matrix, use_los, threshold)
    return matrix

def count_occurrences(matrix, val):
    return sum(row.count(val) for row in matrix)

def main():
    seat_map = import_map('day11-input.txt')
    # Part 1
    final_map = final_state(seat_map, False, 4)
    #print(final_map)
    print(count_occurrences(final_map, '#'))
    # Part 2
    final_map = final_state(seat_map, True, 5)
    print(count_occurrences(final_map, '#'))

if __name__ == "__main__":
    main()
