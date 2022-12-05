import sys
from parse import parse


columns = 9
width = 4
stacks = []


def move(count, source, dest, maintain_order):
    #print(stacks)
    if maintain_order:
        stacks[dest].extend(stacks[source][-count:])
        del stacks[source][-count:]
    else:
        for _ in range(count):
            stacks[dest].append(stacks[source].pop())


def main():
    for _ in range(columns):
        stacks.append([])

    with open('day5-input') as input_file:
        for line in input_file:
            if '[' in line:
                # Populate the stacks
                for col in range(columns):
                    pos = col * width
                    if line[pos] == '[':
                        stacks[col].insert(0, line[pos+1])

            elif line.lower().startswith('move'):
                format_str = 'move {:d} from {:d} to {:d}\n'
                count, source, dest = parse(format_str, line)
                move(count, source-1, dest-1, True)

    #print(stacks)
    output = ''
    for stack in stacks:
        output += stack[-1]
    print(output)


if __name__ == "__main__":
    main()