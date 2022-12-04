def challenge_1(input_file):
    elf_pairs_text = open(input_file).read().split()
    elf_pairs = list(map(split_elf_pairs_to_number_ranges, elf_pairs_text))
    count = 0
    for elf in elf_pairs:
        if elf[0].issubset(elf[1]) or elf[1].issubset(elf[0]):
            count += 1
    print(count)


def challenge_2(input_file):
    elf_pairs_text = open(input_file).read().split()
    elf_pairs = list(map(split_elf_pairs_to_number_ranges, elf_pairs_text))
    count = 0
    for elf in elf_pairs:
        if bool(elf[0].intersection(elf[1])):
            count += 1
    print(count)


def split_elf_pairs_to_number_ranges(elf_pair_text):
    elf_pair = elf_pair_text.split(',')
    elf_1 = elf_pair[0].split('-')
    elf_2 = elf_pair[1].split('-')
    elf_section_range_1 = set(range(int(elf_1[0]), int(elf_1[1])+1))
    elf_section_range_2 = set(range(int(elf_2[0]), int(elf_2[1])+1))
    return [elf_section_range_1, elf_section_range_2]


if __name__ == '__main__':
    challenge_1('challenge_input.txt')
    challenge_2('challenge_input.txt')
