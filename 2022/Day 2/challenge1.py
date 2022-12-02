def rps_strategy(input_file):
    strategies_rows = open(input_file).read().split('\n')
    strategies = [strategy.split(' ') for strategy in strategies_rows]
    total_score = 0
    for strategy in strategies:
        total_score += determine_winner(strategy)
        total_score += determine_points(strategy[1])
    print(total_score)


def determine_winner(strategy):
    if strategy[0] == 'A' and strategy[1] == 'Y':
        return 6
    if strategy[0] == 'A' and strategy[1] == 'Z':
        return 0
    if strategy[0] == 'B' and strategy[1] == 'X':
        return 0
    if strategy[0] == 'B' and strategy[1] == 'Z':
        return 6
    if strategy[0] == 'C' and strategy[1] == 'X':
        return 6
    if strategy[0] == 'C' and strategy[1] == 'Y':
        return 0
    return 3


def determine_points(pick):
    if pick == 'X':
        return 1
    if pick == 'Y':
        return 2
    if pick == 'Z':
        return 3


if __name__ == '__main__':
    rps_strategy('challenge_input.txt')
