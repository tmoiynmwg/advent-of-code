import sys, math


class Polymer:

    def __init__(self, filename):
        with open(filename) as file:
            self.template = list(file.readline().strip())
            self.pairs, self.rules = {}, {}
            file.readline()
            for line in file:
                pair, char = line.strip().split(' -> ')
                self.rules[pair] = char
                self.pairs[pair] = 0
        self.init_pairs()


    def init_pairs(self):
        for i in range(len(self.template) - 1):
            pair = self.template[i] + self.template[i+1]
            self.pairs[pair] += 1


    def step(self, steps=1):
        """Each pair turns into an equal number of 2 new pairs."""
        for _ in range(steps):
            new_pairs = {p:0 for p in self.pairs}
            for pair, count in self.pairs.items():
                char = self.rules[pair]
                np1 = pair[0] + char
                np2 = char + pair[1]
                new_pairs[np1] += count
                new_pairs[np2] += count
            self.pairs = new_pairs


    def slow_step(self, steps=1):
        """Brute force method.

        Check each pair and perform insertions in reverse order."""
        for _ in range(steps):
            #c = self.template.copy()
            for i in reversed(range(len(self.template) - 1)):
                pair = self.template[i] + self.template[i+1]
                if pair in self.rules:
                    self.template.insert(i+1, self.rules[pair])
        #return self.template


    def most_minus_least(self):
        counts = {}
        #for c in self.template:
        #    if char in counts:
        #        counts[char] += 1
        #    else:
        #        counts[char] = 1
        for pair, count in self.pairs.items():
            for char in list(pair):
                if char in counts:
                    counts[char] += count
                else:
                    counts[char] = count
        # Each letter is duplicated in the pairs except the first and last
        # in the template, but we simply round up to account for those.
        counts = {k: math.ceil(v/2) for k, v in counts.items()}
        v = sorted(counts.values())
        return v[-1] - v[0]


def main():
    filename, steps = sys.argv[1:3]
    steps = int(steps)
    p = Polymer(filename)
    p.step(steps)
    print(p.most_minus_least())


if __name__ == "__main__":
    main()
