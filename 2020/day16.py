
def parse_input(filename):
	with open(filename) as input_file:
		raw_data = input_file.read().strip()
		# Create 3 lists of lines
		field_data, your_data, nearby_data = [
			d.split('\n') for d in raw_data.split('\n\n')]
		# Store field rules as a dict of intervals
		field_rules = {}
		for line in field_data:
			name, ranges = line.split(': ')
			ranges = ranges.split(' or ')
			intervals = [tuple(int(v) for v in r.split('-')) for r in ranges]
			field_rules[name] = intervals
		# Remove "your ticket" and "nearby tickets" lines
		your_data, nearby_data = your_data[1], nearby_data[1:]
		your_ticket = [int(n) for n in your_data.split(',')]
		nearby_tickets = []
		for line in nearby_data:
			nearby_tickets.append([int(n) for n in line.split(',')])
		return (field_rules, your_ticket, nearby_tickets)

def legal_intervals(rules):
	all_intervals = []
	for intervals in rules.values():
		for interval in intervals:
			all_intervals.append(interval)
	return all_intervals

def in_interval(num, interval):
	return num >= interval[0] and num <= interval[1]

def check_intervals(fmatr, field_rules, tickets):
	for ticket in tickets:
		for i, num in enumerate(ticket):
			for key, val in field_rules.items():
				for interval in val:
					if in_interval(num, interval):
						break
				else:
					fmatr[i][key] = False

	return fmatr

def check_rows(matr):
	for i, row in enumerate(matr):
		true_count, true_key = 0, ''
		for key, val in row.items():
			if val:
				true_count += 1
				true_key = key
		if true_count == 1:
			# Found an exact match for this row, so
			# mark the rest of this column as False
			for r in matr[:i] + matr[i+1:]:
				r[true_key] = False
	return matr

def check_cols(matr):
	for field in matr[0]:
		true_count, true_index = 0, 0
		for i, row in enumerate(matr):
			if row[field]:
				true_count += 1
				true_index = i
		if true_count == 1:
			row = matr[true_index]
			for key in row:
				if key != field:
					row[key] = False
	return matr

def possible_fields(fmatr):
	output, fully_solved = [], True
	for row in fmatr:
		fields = [key for key in row if row[key]]
		if len(fields) > 1:
			fully_solved = False
		output.append(fields)
	return (output, fully_solved)

def main():
	field_rules, your_ticket, nearby_tickets = parse_input('day16-input.txt')
	# Part 1
	intervals = legal_intervals(field_rules)
	error_rate = 0
	#print(nearby_tickets)
	for ticket in nearby_tickets[:]:
		has_error = False
		for num in ticket:
			for interval in intervals:
				if in_interval(num, interval):
					break
			else:
				has_error = True
				error_rate += num
		# Discard the ticket if it is invalid
		if has_error:
			nearby_tickets.remove(ticket)
	print(error_rate)

	# Part 2
	tickets = nearby_tickets
	tickets.insert(0, your_ticket)
	fmatr = [{field:True for field in field_rules} for f in field_rules]
	fmatr = check_intervals(fmatr, field_rules, tickets)
	pspace, solved = possible_fields(fmatr)
	while not solved:
		fmatr = check_rows(fmatr)
		fmatr = check_cols(fmatr)
		pspace, solved = possible_fields(fmatr)
	departure_product = 1
	for i, num in enumerate(your_ticket):
		if pspace[i][0].startswith('departure'):
			departure_product *= num
	print(departure_product)

if __name__ == "__main__":
	main()