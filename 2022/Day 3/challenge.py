def ruck_sack_challenge_1(input_file):
    rucksacks = open(input_file).read().split('\n')
    rucksacks_compartments = list(map(split_string, rucksacks))
    priority_sum = 0
    for rucksack in rucksacks_compartments:
        item = (set(rucksack[0]).intersection(rucksack[1])).pop()
        priority_sum += get_letter_value(item)
    print(priority_sum)


def ruck_sack_challenge_2(input_file):
    rucksacks = open(input_file).read().split()
    groups = list(zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3]))
    priority_sum = 0
    for group in groups:
        item = (set(group[0]).intersection(group[1]).intersection(group[2])).pop()
        priority_sum += get_letter_value(item)
    print(priority_sum)


def split_string(string):
    return [string[:len(string)//2], string[len(string)//2:]]


def get_letter_value(letter):
    ascii_value = ord(letter)
    if letter.isupper():
        return ascii_value - 38
    return ascii_value - 96


if __name__ == '__main__':
    ruck_sack_challenge_1('challenge_input.txt')
    ruck_sack_challenge_2('challenge_input.txt')
