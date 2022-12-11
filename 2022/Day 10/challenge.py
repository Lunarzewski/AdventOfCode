def challenge_1(instructions):
    x = 1
    current_clock_cycle = 0
    signal_values = []
    for instruction in instructions:
        if instruction[0] == 'addx':
            current_clock_cycle += 1
            check_signal(current_clock_cycle, signal_values, x)
            current_clock_cycle += 1
            check_signal(current_clock_cycle, signal_values, x)

            x += int(instruction[1])
        else:
            current_clock_cycle += 1
            check_signal(current_clock_cycle, signal_values, x)
    print(f'Sum of strengths is {sum(signal_values)}')


def challenge_2(instructions):
    x = 1
    current_clock_cycle = 0
    message_string = ''
    for instruction in instructions:
        if instruction[0] == 'addx':
            current_clock_cycle += 1
            message_string = draw_pixel(current_clock_cycle, message_string, x)
            current_clock_cycle += 1
            message_string = draw_pixel(current_clock_cycle, message_string, x)
            x += int(instruction[1])
        else:
            current_clock_cycle += 1
            message_string = draw_pixel(current_clock_cycle, message_string, x)
    print(message_string)


def draw_pixel(current_clock_cycle, message_string, x):
    if x <= current_clock_cycle % 40 <= x + 2:
        message_string += '#'
    else:
        message_string += '.'
    if current_clock_cycle % 40 == 0:
        message_string += '\n'
    return message_string


def check_signal(current_clock_cycle, signal_values, x):
    if (current_clock_cycle - 20) % 40 == 0:
        signal = current_clock_cycle * x
        signal_values.append(signal)
        print(f'Signal value at clock cycle {current_clock_cycle} is {signal}')


if __name__ == '__main__':
    inst_list = [line.split() for line in open('challenge_input.txt').read().split('\n')]
    challenge_1(inst_list)
    challenge_2(inst_list)
