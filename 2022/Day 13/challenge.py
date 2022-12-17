def challenge_1(pairs):
    right_order_list = []
    for i, pair in enumerate(pairs):



if __name__ == '__main__':
    string_p = [pair.split('\n') for pair in open('challenge_input.txt').read().split('\n\n')]
    p_s = [[eval(s[0]), eval(s[1])]for s in string_p]
    challenge_1(p_s)
