import sys, statistics


def median(lst):
	# Returns the higher median in case of an even-sized list.
	return sorted(lst)[len(lst) // 2]


def mean(lst):
	# Returns a rounded mean.
	return int(round(sum(lst) / len(lst)))


def lin_dist(lst, val):
	dist = 0
	for x in lst:
		dist += abs(x - val)
	return dist


def tri_dist(lst, val):
	dist = 0
	for x in lst:
		d = abs(x - val)
		dist += d**2 + d
	return dist / 2


def print_dist(lst, mean, window, step):
	x = mean - window
	stop = mean + window
	#lowest = None
	dict = {}
	while x <= stop:
		dict[x] = tri_dist(lst, x)
		#if not lowest or lowest > ans:
		#	lowest = ans
		x += step
	for x, dist in dict.items():
		output = ''
		if abs(x - mean) < step / 10:
			output += f'*{x:.2f}*'
		else:
			output += f' {x:.2f} '
		if dist == min(dict.values()):
			output += f'\t*{dist:.2f}*'
		else:
			output += f'\t {dist:.2f} '
		print(output)


def main():
    filename = sys.argv[1]
    crabs = None
    with open(filename) as input_file:
        crabs = [int(x) for x in input_file.readline().split(',')]
    print('Part 1 solution: ', lin_dist(crabs, median(crabs)))
    print('Fuel cost to mean: ', tri_dist(crabs, mean(crabs)))
    print('Part 2 solution: ', min([tri_dist(crabs, p) for p in range(min(crabs), max(crabs) + 1)]))
    print()
    print_dist(crabs, statistics.mean(crabs), 2., 0.1)


if __name__ == "__main__":
    main()