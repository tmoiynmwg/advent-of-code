import sys


class Lanternfish:

    def __init__(self, lst, gen1, gen2):
        self.fish = lst.copy()
        self.sieve = len(lst)
        self.gen1, self.gen2 = (gen2, gen1) if gen1 > gen2 else (gen1, gen2)
        self.pop = {}
        for i in range(gen2):
            self.pop[i] = len(self.fish)
            self.iterate()

    def __str__(self):
        return str(self.fish)

    def __len__(self):
        return len(self.fish)

    def iterate(self):
        for i, f in enumerate(self.fish[:]):
            if f == 0:
                self.fish.append(self.gen2 - 1)
                self.fish[i] = self.gen1 - 1
            else:
                self.fish[i] -= 1

    # Failed streamlining attempt
    def iterate7(self):
        i = 0
        new_fish = []
        for i, f in zip(range(self.sieve, len(self)), 
                        self.fish[self.sieve:]):
            if f < 7:
                new_fish.append(f + 2)
            else:
                self.fish[i] -= 7
        self.fish.extend([x + 2 for x in self.fish[:self.sieve]])
        self.fish.extend(new_fish)
        self.sieve = i + 1

    # Brute force method
    def multiply(self, days):
        q, r = days // 7, days % 7
        for _ in range(q):
            self.iterate7()
        for _ in range(r):
            self.iterate()

    # Recursive method
    def fibonacci(self, days):
        if days in self.pop:
            #print(days, self.gen1, self.gen2)
            return self.pop[days]
        else:
            answer = (self.fibonacci(days - self.gen1) 
                    + self.fibonacci(days - self.gen2))
            self.pop[days] = answer
            return answer


def main():
    filename, days = sys.argv[1:3]
    days = int(days)
    lf = None
    with open(filename) as input_file:
        lf = Lanternfish([int(x) for x in 
                input_file.readline().split(',')], 7, 9)
    #for i in range(days):
        #print(lf.fibonacci(i))
        #lf.multiply(1)
        #print(lf)
        #print(len(lf))
    print(lf.fibonacci(days))


if __name__ == "__main__":
    main()