import math

def part1(filename):
    with open(filename) as input_file:
        start_time, bus_string = [line.strip() for line in list(input_file)]
    start_time = int(start_time)
    buses = [int(b) for b in bus_string.split(',') if b.isdecimal()]
    #print(buses)
    departures = [math.ceil(start_time / bus) * bus for bus in buses]
    departure_time = min(departures)
    earliest_bus = buses[departures.index(departure_time)]
    wait_time = departure_time - start_time
    return earliest_bus * wait_time

def euclid(x, y):
    # Extended Euclidean algorithm:
    # return the gcd as well as Bezout coefficients for x and y;
    # that is, (gcd, a, b) such that ax + by = gcd
    s0, s1 = 0, 1
    t0, t1 = 1, 0
    while x > 0:
        q = y // x
        s0, s1 = s1, s0 - s1*q
        t0, t1 = t1, t0 - t1*q
        x, y = y - x*q, x
    return (y, s0, t0)

def merge_residues(res1, mod1, res2, mod2):
    # Find minimal residue x such that x = r1 mod m1 and x = r2 mod m2
    gcd, bez1, bez2 = euclid(mod1, mod2)
    if res1 % gcd != res2 % gcd:
        raise ValueError(f'No solution. {res1} mod {mod1} and '
                         f'{res2} mod {mod2} are not compatible.')
    lcm = mod1 // gcd * mod2
    new_res = (res1*bez2*mod2 + res2*bez1*mod1) // gcd % lcm
    return (new_res, lcm)

def part2(filename):
    with open(filename) as input_file:
        bus_string = list(input_file)[1].strip()
    buses = [int(b) if b.isdecimal() else 0 for b in bus_string.split(',')]
    res, lcm = 0, 1
    for r, bus in enumerate(buses):
        if bus > 0:
            # res needs to be r minutes before a multiple of bus
            res, lcm = merge_residues(res, lcm, -r, bus)
    return res

def main():
    filename = 'day13-input.txt'
    print(part1(filename))
    print(part2(filename))

if __name__ == "__main__":
    main()
