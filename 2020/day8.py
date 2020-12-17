import copy

def import_boot_code(filename):
    instructions = []
    with open(filename) as input_file:
        for line in input_file:
            op, arg = line.split()
            instructions.append([op, int(arg)])
    return instructions

def run_until_loop(instructions):
    stack_trace = []
    line_num, accum = 0, 0

    while line_num not in stack_trace and line_num < len(instructions):
        stack_trace.append(line_num)
        op, arg = instructions[line_num]
        if op == 'jmp':
            line_num += arg
        elif op == 'acc':
            accum += arg
            line_num += 1
        else:
            line_num += 1

    return (line_num == len(instructions), accum, stack_trace)

def fix_infinite_loop(instructions, stack_trace):
    for alter_line in stack_trace:
        op = instructions[alter_line][0]
        if op == 'jmp' or op == 'nop':
            new_code = copy.deepcopy(instructions)
            if op == 'jmp':
                new_code[alter_line][0] = 'nop'
            else:
                new_code[alter_line][0] = 'jmp'

            successful_exit, accum = run_until_loop(new_code)[:2]
            if successful_exit:
                return accum

def main():
    boot_code = import_boot_code('day8-input.txt')
    stack_trace = run_until_loop(boot_code)[2]
    print(fix_infinite_loop(boot_code, stack_trace))

if __name__ == "__main__":
    main()