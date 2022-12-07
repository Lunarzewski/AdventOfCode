def challenge_1(elf_commands):
    directories = get_directories(elf_commands)
    print(directories)


def get_directories(elf_commands):
    directories = []
    for command in elf_commands:
        if 'cd' in command:
            directories.append(command.replace('$ cd ', ''))
    directories.remove('..')
    return [directory for directory in directories if directory != '..']


if __name__ == '__main__':
    commands = open('challenge_input.txt').read().split('\n')
    challenge_1(commands)
