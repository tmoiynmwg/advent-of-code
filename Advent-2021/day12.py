import sys


class Cave:

    def __init__(self, name, big):
        self.name = name
        self.big = big
        self.links = set()
        self.visited = False

    def __str__(self):
        size = 'big' if self.big else 'small'
        return f'{self.name} ({size})'

    def link(self, cave):
        self.links.add(cave)
        cave.links.add(self)


class Traverse:

    def __init__(self, start, end, revisit_small):
        self.start = start
        self.end = end
        self.path = [start.name]
        self.revisited_small = not revisit_small

    def count_paths(self):
        return self.count_paths_from(self.start)

    def count_paths_from(self, cave):
        """Depth-first traversal to count every path to the end."""
        if cave == self.end:
            #print(cave.name, '\n')
            #print(self.path)
            return 1
        revert_revisit = self.revisited_small
        revert_visited = cave.visited
        if cave.visited and not cave.big:
            if self.revisited_small or cave == self.start:
                return 0
            self.revisited_small = True
            #print(self.path)
        count = 0
        cave.visited = True
        #print(cave.name)
        for n in cave.links:
            self.path.append(n.name)
            count += self.count_paths_from(n)
            self.path.pop()
        cave.visited = revert_visited
        self.revisited_small = revert_revisit
        return count


def main():
    s, e = 'start', 'end'
    filename = sys.argv[1]
    caves = {}
    with open(filename) as file:
        for line in file:
            entr, exit = line.strip().split('-')
            for name in (entr, exit):
                if name not in caves:
                    big = name == name.upper()
                    caves[name] = Cave(name, big)
            caves[entr].link(caves[exit])
    #for c in caves.values():
    #    print(c)
    t = Traverse(caves[s], caves[e], True)
    print('Total paths:', t.count_paths())


if __name__ == "__main__":
    main()
