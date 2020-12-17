
def generate_parents(filename):
    parent_dict = {}
    with open(filename) as input_file:
        for line in input_file:
            subject, predicate = line.strip().rstrip('.').split(' contain ')
            if 'no other bags' in predicate:
                continue

            parent = subject.removesuffix(' bags')
            clauses = predicate.split(', ')
            children = set()
            for clause in clauses:
                words = clause.split()
                children.add(' '.join(words[1:-1]))

            for child in children:
                if child in parent_dict:
                    parent_dict[child].add(parent)
                else:
                    parent_dict[child] = {parent}
    return parent_dict

def find_all_ancestors(color, parent_dict):
    if color not in parent_dict:
        return set()
    parents = parent_dict[color]
    ancestors = set(parents)
    parent_dict.pop(color)
    for p in parents:
        ancestors.update(find_all_ancestors(p, parent_dict))
    return ancestors

def generate_children(filename):
    child_dict = {}
    with open(filename) as input_file:
        for line in input_file:
            subject, predicate = line.strip().rstrip('.').split(' contain ')
            parent = subject.removesuffix(" bags")
            if 'no other bags' in predicate:
                child_dict[parent] = set()
            else:
                clauses = predicate.split(', ')
                children = set()
                for clause in clauses:
                    words = clause.split()
                    children.add((int(words[0]), ' '.join(words[1:-1])))
                child_dict[parent] = children
    return child_dict

def count_descendants(color, child_dict):
    if color not in child_dict:
        return 0
    total_descendants = 0
    children = child_dict[color]
    for child in children:
        bag_num, bag_color = child
        total_descendants += count_descendants(bag_color,
                                               child_dict) * bag_num + bag_num
    return total_descendants

def main():
    # Part 1
    dict = generate_parents("day7-input.txt")
    print(len(find_all_ancestors('shiny gold', dict)))
    # Part 2
    dict = generate_children('day7-input.txt')
    print(count_descendants('shiny gold', dict))

if __name__ == "__main__":
    main()