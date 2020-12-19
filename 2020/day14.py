def bitmask(decimal, mask):
    #print(decimal, mask)
    binary = format(decimal, 'b').rjust(len(mask), '0')
    result = ''
    for i in range(len(mask)):
        result += mask[i] if mask[i].isnumeric() else binary[i]
    #print(result)
    return int(result, 2)

def bitmask_v2(decimal, mask):
    binary = format(decimal, 'b').rjust(len(mask), '0')
    addresses = ['']
    for i, m in enumerate(mask):
        new_addresses = []
        for addr in addresses:
            if m == '0':
                new_addresses.append(addr + binary[i])
            elif m == '1':
                new_addresses.append(addr + m)
            elif m == 'X':
                new_addresses.append(addr + '0')
                new_addresses.append(addr + '1')
            else:
                raise ValueError('Mask contains illegal character')
        addresses = new_addresses
    return set(int(a, 2) for a in addresses)

def decode(filename, v2):
    with open(filename) as input_file:
        mask = 'X' * 36
        mem = {}
        for line in input_file:
            var, val = line.strip().split(' = ')
            if var == 'mask':
                mask = val
            elif var.startswith('mem['):
                addr = int(var[4:-1])
                if not v2:
                    mem[addr] = bitmask(int(val), mask)
                else:
                    addresses = bitmask_v2(addr, mask)
                    for a in addresses:
                        mem[a] = int(val)
    return sum(mem.values())

def main():
    filename = 'day14-input.txt'
    print(decode(filename, False))
    print(decode(filename, True))

if __name__ == "__main__":
    main()
