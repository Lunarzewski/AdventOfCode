def challenge_1(inst_list):
    H = [0, 0]
    T = [0, 0]
    trail = [[0, 0]]
    for inst in inst_list:
        match inst[0]:
            case 'D':
                for i in range(inst[1]):
                    H[0] -= 1
                    if (H[0] - T[0])**2 > 1:
                        T[0] -= 1
                        T[1] = H[1]
                        trail.append(T.copy())
            case 'U':
                for i in range(inst[1]):
                    H[0] += 1
                    if (H[0] - T[0]) ** 2 > 1:
                        T[0] += 1
                        T[1] = H[1]
                        trail.append(T.copy())
            case 'L':
                for i in range(inst[1]):
                    H[1] -= 1
                    if (H[1] - T[1]) ** 2 > 1:
                        T[1] -= 1
                        T[0] = H[0]
                        trail.append(T.copy())
            case 'R':
                for i in range(inst[1]):
                    H[1] += 1
                    if (H[1] - T[1]) ** 2 > 1:
                        T[1] += 1
                        T[0] = H[0]
                        trail.append(T.copy())
    unique_spaces = [list(mark) for mark in set(tuple(mark) for mark in trail)]
    print(len(unique_spaces))


def challenge_2(inst_list):
    snake = [[0, 0] for _ in range(10)]
    trail = [[0, 0]]
    for inst in inst_list:
        for _ in range(inst[1]):
            match inst[0]:
                case 'D':
                    snake[0][0] -= 1
                case 'U':
                    snake[0][0] += 1
                case 'L':
                    snake[0][1] -= 1
                case 'R':
                    snake[0][1] += 1
            for i, knot in enumerate(snake[1:]):
                if verticle_distance(i, knot, snake) and horizontal_distance(i, knot, snake):
                    if head_to_right(i, knot, snake):
                        knot[1] += 1
                    if head_to_left(i, knot, snake):
                        knot[1] -= 1
                    if head_above(i, knot, snake):
                        knot[0] += 1
                    if head_below(i, knot, snake):
                        knot[0] -= 1
                if verticle_distance(i, knot, snake):
                    knot[1] = snake[i][1]
                    if head_above(i, knot, snake):
                        knot[0] += 1
                    if head_below(i, knot, snake):
                        knot[0] -= 1
                if horizontal_distance(i, knot, snake):
                    if head_to_right(i, knot, snake):
                        knot[1] += 1
                    if head_to_left(i, knot, snake):
                        knot[1] -= 1
                    knot[0] = snake[i][0]
            trail.append(snake[-1].copy())

    unique_spaces = [list(mark) for mark in set(tuple(mark) for mark in trail)]
    print(len(unique_spaces))


def head_to_left(i, knot, snake):
    return snake[i][1] < knot[1]


def head_to_right(i, knot, snake):
    return snake[i][1] > knot[1]


def head_above(i, knot, snake):
    return snake[i][0] > knot[0]


def head_below(i, knot, snake):
    return snake[i][0] < knot[0]


def horizontal_distance(i, knot, snake):
    return (snake[i][1] - knot[1]) ** 2 > 1


def verticle_distance(i, knot, snake):
    return (snake[i][0] - knot[0]) ** 2 > 1


if __name__ == '__main__':
    instructions = open('challenge_input.txt').read().split('\n')
    instruction_list = []
    for instruction in instructions:
        instruction_list.append([instruction.split()[0], int(instruction.split()[1])])
    # challenge_1(instruction_list)
    challenge_2(instruction_list)
