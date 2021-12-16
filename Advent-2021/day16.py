import sys, math


class PacketDecoder:

    def __init__(self, hexstr):
        length = 4 * len(hexstr)
        self.bits = str(bin(int(hexstr, 16)))[2:].zfill(length)
        self.total_version = 0

    def parse_literal(self):
        cont, numstr = 1, ''
        while cont:
            cont = int(self.bits[0])
            numstr += self.bits[1:5]
            self.bits = self.bits[5:]
        return int(numstr, 2)

    #@staticmethod
    def gt(lst):
        return 1 if lst[0] > lst[1] else 0

    def lt(lst):
        return 1 if lst[0] < lst[1] else 0

    def eq(lst):
        return 1 if lst[0] == lst[1] else 0

    operators = {0: sum,
                 1: math.prod,
                 2: min,
                 3: max,
                 5: gt,
                 6: lt,
                 7: eq
    }

    def parse_packet(self):
        #print(self.bits)
        version = int(self.bits[:3], 2)
        typeID = int(self.bits[3:6], 2)
        self.bits = self.bits[6:]
        #print(version, typeID)
        self.total_version += version
        if typeID == 4:
            return self.parse_literal()
        subpackets = []
        length_type = int(self.bits[0], 2)
        self.bits = self.bits[1:]
        if length_type:
            subpacket_count = int(self.bits[:11], 2)
            self.bits = self.bits[11:]
            for _ in range(subpacket_count):
                subpackets.append(self.parse_packet())
        else:
            subpacket_length = int(self.bits[:15], 2)
            #print(subpacket_length)
            self.bits = self.bits[15:]
            temp = self.bits[subpacket_length:]
            self.bits = self.bits[:subpacket_length]
            while len(self.bits) > 0:
                subpackets.append(self.parse_packet())
            self.bits = temp
        #if typeID == 0:
        #    return sum(subpackets)
        #f typeID == 1:
        #    return math.prod(subpackets)
        #if typeID == 2:
        #    return min(subpackets)
        #if typeID == 3:
        #    return max(subpackets)
        return PacketDecoder.operators[typeID](subpackets)


def main():
    filename = sys.argv[1]
    with open(filename) as file:
        for line in file:
            line = line.strip()
            print(line)
            pd = PacketDecoder(line)
            print('Answer:', pd.parse_packet())
            print('Version:', pd.total_version)


if __name__ == "__main__":
    main()
