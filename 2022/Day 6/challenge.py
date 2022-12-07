def challenge_1():
    packet = open('challenge_input.txt').read()
    for i, c in enumerate(packet):
        if len(set(packet[i:i+4])) == len(packet[i:i+4]):
            print(i + 4)
            return


def challenge_2():
    packet = open('challenge_input.txt').read()
    for i, c in enumerate(packet):
        if len(set(packet[i:i + 14])) == len(packet[i:i + 14]):
            print(i + 14)
            return


if __name__ == '__main__':
    challenge_1()
    challenge_2()

class Directory:
    def __init
