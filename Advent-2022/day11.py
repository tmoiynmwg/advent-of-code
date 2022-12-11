import sys
import numpy


WORRY_DECAY = 1


class Monkey:
    def __init__(self, starting_items, operation_id, divisor):
        self.items = starting_items
        self.id = operation_id
        self.divisor = divisor
        self.activity = 0

    def set_targets(self, true_target, false_target):
        self.true_target = true_target
        self.false_target = false_target

    def add_item(self, item):
        self.items.append(item)

    def op(self, item):
        if self.id == 0:
            item *= 3
        elif self.id == 1:
            item += 7
        elif self.id == 2:
            item += 5
        elif self.id == 3:
            item += 8
        elif self.id == 4:
            item += 4
        elif self.id == 5:
            item *= 2
        elif self.id == 6:
            item += 6
        elif self.id == 7:
            item *= item
        return item // WORRY_DECAY  # In part 1 we always divide by 3

    def div_test(self, item):
        return item % self.divisor == 0

    def turn(self, max_worry = 0):
        while len(self.items) > 0:
            # Inspect and throw away each item in order
            self.activity += 1
            item = self.op(self.items.pop(0))
            if max_worry > 0:
                # Roll over values that are too large
                item %= max_worry
            if self.div_test(item):
                self.true_target.add_item(item)
            else:
                self.false_target.add_item(item)


def main():
    divisors = [5, 2, 13, 19, 11, 3, 7, 17]
    max_worry = numpy.lcm.reduce(divisors)
    monkeys = [Monkey([78, 53, 89, 51, 52, 59, 58, 85], 0, divisors[0]),
               Monkey(                            [64], 1, divisors[1]),
               Monkey(                [71, 93, 65, 82], 2, divisors[2]),
               Monkey(        [67, 73, 95, 75, 56, 74], 3, divisors[3]),
               Monkey(                    [85, 91, 90], 4, divisors[4]),
               Monkey(    [67, 96, 69, 55, 70, 83, 62], 5, divisors[5]),
               Monkey(            [53, 86, 98, 70, 64], 6, divisors[6]),
               Monkey(                        [88, 64], 7, divisors[7])]
    monkeys[0].set_targets(monkeys[2], monkeys[7])
    monkeys[1].set_targets(monkeys[3], monkeys[6])
    monkeys[2].set_targets(monkeys[5], monkeys[4])
    monkeys[3].set_targets(monkeys[6], monkeys[0])
    monkeys[4].set_targets(monkeys[3], monkeys[1])
    monkeys[5].set_targets(monkeys[4], monkeys[1])
    monkeys[6].set_targets(monkeys[7], monkeys[0])
    monkeys[7].set_targets(monkeys[2], monkeys[5])

    rounds = int(sys.argv[1])
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.turn(max_worry)

    activity = [m.activity for m in monkeys]
    activity.sort(reverse=True)
    print(activity[0] * activity[1])


if __name__ == "__main__":
    main()
