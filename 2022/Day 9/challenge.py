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
                    if (snake[0][0] - snake[1][0]) ** 2 > 1:
                        snake[1][0] -= 1
                        snake[1][1] = snake[0][1]
                    for i, knot in enumerate(snake[2:]):
                        if (snake[i+1][0] - knot[0]) ** 2 > 1:
                            knot[0] -= 1
                            if knot[1] != snake[i+1][1] and snake[i+1][1] < knot[1]:
                                knot[1] -= 1
                            if knot[1] != snake[i+1][1] and snake[i+1][1] > knot[1]:
                                knot[1] += 1
                        if (snake[i+1][1] - knot[1]) ** 2 > 1 and snake[i+1][1] < knot[1]:
                            knot[0] -= 1
                            knot[1] = snake[i+1][1] + 1
                        if (snake[i+1][1] - knot[1]) ** 2 > 1 and snake[i+1][1] > knot[1]:
                            knot[0] -= 1
                            knot[1] = snake[i+1][1] - 1
                case 'U':
                    snake[0][0] += 1
                    if (snake[0][0] - snake[1][0]) ** 2 > 1:
                        snake[1][0] += 1
                        snake[1][1] = snake[0][1]
                    for i, knot in enumerate(snake[2:]):
                        if (snake[i + 1][0] - knot[0]) ** 2 > 1:
                            knot[0] += 1
                            if knot[1] != snake[i + 1][1] and snake[i + 1][1] < knot[1]:
                                knot[1] -= 1
                            if knot[1] != snake[i + 1][1] and snake[i + 1][1] > knot[1]:
                                knot[1] += 1
                        if (snake[i + 1][1] - knot[1]) ** 2 > 1 and snake[i + 1][1] < knot[1]:
                            knot[0] += 1
                            knot[1] = snake[i + 1][1] + 1
                        if (snake[i + 1][1] - knot[1]) ** 2 > 1 and snake[i + 1][1] > knot[1]:
                            knot[0] += 1
                            knot[1] = snake[i + 1][1] - 1
                case 'L':
                    snake[0][1] -= 1
                    if (snake[0][1] - snake[1][1]) ** 2 > 1:
                        snake[1][1] -= 1
                        snake[1][0] = snake[0][0]
                    for i, knot in enumerate(snake[2:]):
                        if (snake[i+1][1] - knot[1]) ** 2 > 1:
                            knot[1] -= 1
                            if knot[0] != snake[i+1][0] and snake[i+1][0] < knot[0]:
                                knot[0] -= 1
                            if knot[0] != snake[i+1][0] and snake[i+1][0] > knot[0]:
                                knot[0] += 1
                        if (snake[i+1][0] - knot[0]) ** 2 > 1 and snake[i+1][0] < knot[0]:
                            knot[1] -= 1
                            knot[1] = snake[i+1][1] + 1
                        if (snake[i+1][0] - knot[0]) ** 2 > 1 and snake[i+1][0] > knot[0]:
                            knot[1] -= 1
                            knot[0] = snake[i+1][0] - 1
                case 'R':
                    snake[0][1] += 1
                    if (snake[0][1] - snake[1][1]) ** 2 > 1:
                        snake[1][1] += 1
                        snake[1][0] = snake[0][0]
                    for i, knot in enumerate(snake[2:]):
                        if (snake[i + 1][1] - knot[1]) ** 2 > 1:
                            knot[1] += 1
                            if knot[0] != snake[i+1][0] and snake[i+1][0] < knot[0]:
                                knot[0] -= 1
                            if knot[0] != snake[i+1][0] and snake[i+1][0] > knot[0]:
                                knot[0] += 1
                        if (snake[i + 1][0] - knot[0]) ** 2 > 1 and snake[i + 1][0] < knot[0]:
                            knot[1] += 1
                            knot[1] = snake[i + 1][1] + 1
                        if (snake[i + 1][0] - knot[0]) ** 2 > 1 and snake[i + 1][0] > knot[0]:
                            knot[1] += 1
                            knot[0] = snake[i + 1][0] - 1

        trail.append(snake[-1].copy())
    unique_spaces = [list(mark) for mark in set(tuple(mark) for mark in trail)]
    print(len(unique_spaces))


if __name__ == '__main__':
    instructions = open('challenge_input.txt').read().split('\n')
    instruction_list = []
    for instruction in instructions:
        instruction_list.append([instruction.split()[0], int(instruction.split()[1])])
    # challenge_1(instruction_list)
    challenge_2(instruction_list)
