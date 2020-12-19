
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

def main():
    field_rules, your_ticket, nearby_tickets = parse_input('day16-input.txt')
    # Part 1
    intervals = legal_intervals(field_rules)
    error_rate = 0
    #print(nearby_tickets)
    for ticket in nearby_tickets[:]:
    	for num in ticket:
    		has_error = False
    		for interval in intervals:
    			if in_interval(num, interval):
    				break
    		else:
    			has_error = True
    			error_rate += num
    		# Discard any erroneous tickets
    		if has_error:
    			nearby_tickets.remove(ticket)
    print(error_rate)
    # Part 2
    fmatr = [{field:True for field in field_rules} for f in field_rules]
    print(fmatr)

if __name__ == "__main__":
    main()