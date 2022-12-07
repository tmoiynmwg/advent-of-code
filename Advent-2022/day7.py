import sys
from parse import parse


class Directory:
    #small_dir_sum = 0
    sizes = []

    def __init__(self, parent):
        self.parent = parent
        self.size = None
        self.files = []     # only filesizes
        self.subdir = []

    def add_file(self, filesize):
        self.files.append(filesize)

    def add_subdir(self, folder):
        self.subdir.append(folder)

    # Recursively compute the total size of the directory and all
    # subdirectories and store the results in Directory.sizes
    def get_size(self):
        total = 0
        for folder in self.subdir:
            total += folder.get_size()
        total += sum(self.files)
        self.size = total
        Directory.sizes.append(total)
        #if total <= 100000:
        #    Directory.small_dir_sum += total
        return total

    def create_directories(logfile):
        root = Directory(None)
        current = root
        with open(logfile) as log:
            for line in log:
                line = line.strip()
                if line.startswith('$ cd '):
                    folder = parse('$ cd {}', line)[0]
                    if folder == '..':
                        current = current.parent
                    elif folder != '/':
                        # Create a new directory once when we move to it
                        new_dir = Directory(current)
                        current.add_subdir(new_dir)
                        current = new_dir
                elif line[0].isdigit():
                    filesize = int(line.split()[0])
                    current.add_file(filesize)
        return root

    def small_dir_sum(size):
        return sum([s for s in Directory.sizes if s <= size])

    def smallest_sufficient_dir(size):
        return min([s for s in Directory.sizes if s >= size])


def main():
    root = Directory.create_directories('day7-input')
    used_space = root.get_size()
    space_needed = used_space - 40000000
    print(Directory.small_dir_sum(100000))                   # Part 1
    print(Directory.smallest_sufficient_dir(space_needed))   # Part 2


if __name__ == "__main__":
    main()