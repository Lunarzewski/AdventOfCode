from functools import cmp_to_key


def challenge_1(pairs):
    right_order_list = []
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) == -1:
            right_order_list.append(i + 1)
    print(sum(right_order_list))


def challenge_2(pairs):
    pairs.extend([[[2]], [[6]]])
    pairs.sort(key=cmp_to_key(compare))
    print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))


def compare(left_side, right_side):
    for i, val in enumerate(left_side):
        if isinstance(right_side, list) and i == len(right_side):
            return 1
        elif isinstance(val, int) and isinstance(right_side[i], list):
            x = compare([val], right_side[i])
            if x != 0:
                return x
        elif isinstance(val, list) and isinstance(right_side[i], int):
            x = compare(val, [right_side[i]])
            if x != 0:
                return x
        elif isinstance(val, list):
            x = compare(val, right_side[i])
            if x != 0:
                return x
        elif val < right_side[i]:
            return -1
        elif val > right_side[i]:
            return 1
    if len(left_side) < len(right_side):
        return -1
    return 0


if __name__ == '__main__':
    string_p = [pair.split('\n') for pair in open('challenge_input.txt').read().split('\n\n')]
    p_s = [[eval(s[0]), eval(s[1])] for s in string_p]
    challenge_1(p_s)
    p_s2 = (open('challenge_input.txt').read().replace('\n\n', '\n')).split('\n')
    challenge_2([eval(s) for s in p_s2])
