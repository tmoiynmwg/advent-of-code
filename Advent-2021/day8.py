import sys

# The translated segment positions:
#
#   aaaa  
#  b    c 
#  b    c  
#   dddd  
#  e    f  
#  e    f  
#   gggg  

digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
          'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']


def map_pos(input):
    """Given the codes for 0-9, generate a character dictionary."""
    codes = [set(s) for s in sorted(input, key=len)]
    pos = {}
    pos[(codes[1] - codes[0]).pop()] = 'a'
    for code in codes[6:9]:
        # 0, 6, and 9 each only have one missing segment
        sig = (set('abcdefg') - code).pop()
        #print(sig, input[2])
        if sig in codes[0]:
            # found 6
            #print(sig)
            pos[sig] = 'c'
            pos[(codes[0] - set(sig)).pop()] = 'f'
        elif sig in codes[2]:  # 4
            # found 0
            pos[sig] = 'd'
        else:
            # found 9
            pos[sig] = 'e'
    for sig in set('abcdefg') - pos.keys():
        if sig in codes[2]:
            pos[sig] = 'b'
        else:
            pos[sig] = 'g'
    return pos


def decipher(pos, cipher):
    """Use the pos dictionary to return the corresponding digit."""
    segs = set()
    for sig in cipher:
        segs.add(pos[sig])
    #print(segs)
    for digit, seg_str in enumerate(digits):
        if segs == set(seg_str):
            return digit


def main():
    filename = sys.argv[1]
    unique_count, output_val = 0, 0
    with open(filename) as input_file:
        for line in input_file:
            input, output = [side.split() for side in line.split(' | ')]
            #print(input, output)
            for string in output:
                if len(string) in (2, 3, 4, 7):
                    # these four digits have unique segment counts
                    unique_count += 1
            seg_dict = map_pos(input)
            #print(seg_dict)
            # Interpret the 4-digit output as a single 4-digit number
            for i, o in enumerate(reversed(output)):
                output_val += 10**i * decipher(seg_dict, o)
    print('Unique outputs: ', unique_count)
    print('Total output value: ', output_val)


if __name__ == "__main__":
    main()