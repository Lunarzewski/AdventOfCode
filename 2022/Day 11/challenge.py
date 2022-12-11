class Monkey:
    def __init__(self, items, operation, test_value):
        self.items = items
        self.operation = operation
        self.test_value = test_value
        self.true_monkey = None
        self.false_monkey = None
        self.items_inspected = 0

    def inspect(self, worry_less=True):
        for item in self.items:
            self.items_inspected += 1
            inspected_value = self.operation(item)
            if worry_less:
                inspected_value = inspected_value // 3
            else:
                inspected_value = inspected_value % 9699690
            if inspected_value % self.test_value == 0:
                self.true_monkey.items.append(inspected_value)
            else:
                self.false_monkey.items.append(inspected_value)
        self.items = []


def challenge_1(monkey_list):
    for _ in range(20):
        for monkey in monkey_list:
            monkey.inspect()
    monkey_list.sort(key=lambda m: m.items_inspected, reverse=True)
    print(monkey_list[0].items_inspected * monkey_list[1].items_inspected)


def challenge_2(monkey_list):
    for i in range(10000):
        if i % 100 == 0:
            print(f'Round {i}')
        for monkey in monkey_list:
            monkey.inspect(worry_less=False)
    monkey_list.sort(key=lambda m: m.items_inspected, reverse=True)
    print(monkey_list[0].items_inspected * monkey_list[1].items_inspected)


if __name__ == '__main__':
    monkeys = [
        Monkey([54, 98, 50, 94, 69, 62, 53, 85], lambda x: x * 13, 3),
        Monkey([71, 55, 82], lambda x: x + 2, 13),
        Monkey([77, 73, 86, 72, 87], lambda x: x + 8, 19),
        Monkey([97, 91], lambda x: x + 1, 17),
        Monkey([78, 97, 51, 85, 66, 63, 62], lambda x: x * 17, 5),
        Monkey([88], lambda x: x + 3, 7),
        Monkey([87, 57, 63, 86, 87, 53], lambda x: x * x, 11),
        Monkey([73, 59, 82, 65], lambda x: x + 6, 2),
    ]
    monkeys[0].true_monkey = monkeys[2]
    monkeys[0].false_monkey = monkeys[1]

    monkeys[1].true_monkey = monkeys[7]
    monkeys[1].false_monkey = monkeys[2]

    monkeys[2].true_monkey = monkeys[4]
    monkeys[2].false_monkey = monkeys[7]

    monkeys[3].true_monkey = monkeys[6]
    monkeys[3].false_monkey = monkeys[5]

    monkeys[4].true_monkey = monkeys[6]
    monkeys[4].false_monkey = monkeys[3]

    monkeys[5].true_monkey = monkeys[1]
    monkeys[5].false_monkey = monkeys[0]

    monkeys[6].true_monkey = monkeys[5]
    monkeys[6].false_monkey = monkeys[0]

    monkeys[7].true_monkey = monkeys[4]
    monkeys[7].false_monkey = monkeys[3]

    challenge_1(monkeys)

    monkeys = [
        Monkey([54, 98, 50, 94, 69, 62, 53, 85], lambda x: x * 13, 3),
        Monkey([71, 55, 82], lambda x: x + 2, 13),
        Monkey([77, 73, 86, 72, 87], lambda x: x + 8, 19),
        Monkey([97, 91], lambda x: x + 1, 17),
        Monkey([78, 97, 51, 85, 66, 63, 62], lambda x: x * 17, 5),
        Monkey([88], lambda x: x + 3, 7),
        Monkey([87, 57, 63, 86, 87, 53], lambda x: x * x, 11),
        Monkey([73, 59, 82, 65], lambda x: x + 6, 2),
    ]
    monkeys[0].true_monkey = monkeys[2]
    monkeys[0].false_monkey = monkeys[1]

    monkeys[1].true_monkey = monkeys[7]
    monkeys[1].false_monkey = monkeys[2]

    monkeys[2].true_monkey = monkeys[4]
    monkeys[2].false_monkey = monkeys[7]

    monkeys[3].true_monkey = monkeys[6]
    monkeys[3].false_monkey = monkeys[5]

    monkeys[4].true_monkey = monkeys[6]
    monkeys[4].false_monkey = monkeys[3]

    monkeys[5].true_monkey = monkeys[1]
    monkeys[5].false_monkey = monkeys[0]

    monkeys[6].true_monkey = monkeys[5]
    monkeys[6].false_monkey = monkeys[0]

    monkeys[7].true_monkey = monkeys[4]
    monkeys[7].false_monkey = monkeys[3]
    challenge_2(monkeys)
