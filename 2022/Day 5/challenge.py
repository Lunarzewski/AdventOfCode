def challenge_1():
    instructions, stacks = read_data()
    for instruction in instructions:
        for _ in range(instruction[0]):
            crate = stacks[instruction[1][0] - 1].pop()
            stacks[instruction[1][1] - 1].append(crate)

    for stack in stacks:
        print(stack.pop())


def challenge_2():
    instructions, stacks = read_data()
    for instruction in instructions:
        crates = [stacks[instruction[1][0] - 1].pop() for _ in range(instruction[0])]
        crates.reverse()
        stacks[instruction[1][1] - 1].extend(crates)
    for stack in stacks:
        print(stack.pop())


def read_data():
    file_lines = open('challenge_input.txt').readlines()
    stack_lines = file_lines[0:8]
    instruction_lines = file_lines[10:]
    stacks = create_stacks(stack_lines)
    instructions = get_instructions(instruction_lines)
    return instructions, stacks


def create_stacks(stack_lines):
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in stack_lines:
        for i, value in enumerate(list(range(40)[4::4])):
            if any(c.isalpha() for c in line[i * 4:value]):
                stacks[i].append(line[i * 4 + 1])
    for stack in stacks:
        stack.reverse()
    return stacks


def get_instructions(instruction_lines):
    instructions = []
    for line in instruction_lines:
        instructions.append([int(line[5:7]), [int(line[12:14]), int(line[17:19])]])
    return instructions


if __name__ == '__main__':
    challenge_1()
    challenge_2()
