
class AddMultiplyExpression:
	def __init__(self, str):
		# Add spaces next to parentheses and convert to a list
		str = str.replace('(', '( ').replace(')', ' )')
		self.expr = str.split()

	@staticmethod
	def calc(n1, operator, n2):
		if operator == '+':
			return n1 + n2
		elif operator == '*':
			return n1 * n2
		else:
			raise ValueError(f'{operator} is not a supported operator')

	def eval(self, start_index=0, end_index=float('inf')):
		i, operator, subtotal = start_index, None, None
		while i < end_index and self.expr:
			c = self.expr.pop(start_index)
			#print(c)
			if isinstance(c, int) or c.isdecimal():
				if operator:
					subtotal = self.calc(subtotal, operator, int(c))
					operator = None
				else:
					subtotal = int(c)
			elif c == '+' or c == '*':
				operator = c
			# Recursively calculate any expression inside parentheses
			elif c == '(':
				val = self.eval()
				if operator:
					subtotal = self.calc(subtotal, operator, val)
					operator = None
				else:
					subtotal = val
			elif c == ')':
				return subtotal
			i += 1
		return subtotal

	def eval_precedence(self, first_op, start_index=0):
		i = start_index
		while i < len(self.expr):
			c = self.expr[i]
			if c == first_op:
				# Reduce the expression
				prev, next = self.expr[i-1], self.expr[i+1]
				if next == '(':
					next = self.eval_precedence(first_op, i + 2)
				ans = self.calc(int(prev), c, int(next))
				self.expr[i-1:i+2] = [ans]
				continue
			elif c == '(':
				# Recursively evaluate until a closing parenthesis
				ans = self.eval_precedence(first_op, i + 1)
				self.expr[i] = ans
				#continue
			elif c == ')':
				# Evaluate and delete any lower-
				# precedence operations we skipped.
				return self.eval(start_index, i + 1)
			i += 1
		# Evaluate and delete any lower-
		# precedence operations we skipped.
		return self.eval(start_index, i)
		#self.expr.insert(start_index, ans)

def main():
	filename = 'day18-input.txt'
	part1, part2 = 0, 0
	with open(filename) as homework:
		for line in homework:
			expr = AddMultiplyExpression(line)
			#print(expr)
			part1 += expr.eval()
			expr = AddMultiplyExpression(line)
			part2 += expr.eval_precedence('+')
	print('Part 1:', part1)
	print('Part 2:', part2)

if __name__ == "__main__":
	main()
