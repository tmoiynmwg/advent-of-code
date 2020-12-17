
def sort_adapters(filename):
    with open(filename) as input_file:
        adapters = [int(j) for j in list(input_file)]
    adapters.sort()
    adapters.insert(0, 0)               # charging outlet
    adapters.append(adapters[-1] + 3)   # built-in adapter
    return adapters

def count_diffs(seq, max_diff):
    diffs = [0] * (max_diff + 1)
    for i in range(1, len(seq)):
        d = seq[i] - seq[i-1]
        if d > max_diff:
            raise ValueError(f'The difference {seq[i]} - '
                             f'{seq[i-1]} was out of bounds.')
        diffs[d] += 1
    return diffs

# Deprecated
def brute_force_count_paths(val, seq, max_step):
    if not seq:
        return 1
    paths = 0
    #for new_val in range(val + 1, val + max_step + 1):
    #    if new_val in seq:
    #        paths += count_paths(new_val, se)
    for i in range(min(max_step, len(seq))):
        if seq[i] <= val + max_step:
            paths += count_paths(seq[i], seq[i+1:], max_step)
        else:
            break
    return paths

"""Example: 4, 5, 6, 7
total_paths = paths_from_5_without_7 * paths_from_4_to_5 (2^0)
            + paths_from_6_without_7 * paths_from_4_to_6 (2^1)
            + paths_from_7           * paths_from_4_to_7 (2^2)
"""
def count_paths(val, seq, max_step):
    if not seq:
        return 1
    total_paths = 0
    # Find the window of possible jumps from val
    for i in reversed(range(min(max_step, len(seq)))):
        if seq[i] <= val + max_step:
            window, future = seq[:i+1], seq[i+1:]
            for j, new_val in enumerate(window):
                total_paths += 2**j * count_paths(new_val, future, max_step)
            break
    return total_paths

def main():
    adapters = sort_adapters('day10-input.txt')
    # Part 1
    diffs = count_diffs(adapters, 3)
    print(diffs[1] * diffs[3])
    # Part 2
    print(count_paths(0, adapters[1:], 3))

if __name__ == "__main__":
    main()
