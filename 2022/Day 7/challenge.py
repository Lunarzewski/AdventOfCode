class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.directories = []
        self.files = []
        self.parent = parent

    def add_file(self, file):
        self.files.append(file)

    def add_directory(self, directory):
        self.directories.append(directory)

    def total_size(self):
        size = 0
        for file in self.files:
            size += file.size

        for directory in self.directories:
            size += directory.total_size()
        return size


def challenge_1(elf_commands):
    home_directory = Directory('/', None)
    directories = [home_directory]
    current_directory = home_directory

    for command in elf_commands[2:]:
        if 'dir' in command:
            directory = Directory(command.split()[1], current_directory)
            current_directory.add_directory(directory)
            directories.append(directory)
        elif command.split()[0].isnumeric():
            file = File(command.split()[1], int(command.split()[0]))
            current_directory.add_file(file)
        elif command.split()[1] == 'cd' and command.split()[2] != '..':
            current_directory = next(directory for directory in current_directory.directories if directory.name == command.split()[2])
        elif command.split()[1] == 'cd' and command.split()[2] == '..':
            current_directory = current_directory.parent

    total = 0
    for directory in directories:
        if directory.total_size() <= 100_000:
            # print(f'Name: {directory.name}. Size: {directory.total_size()}')
            total += directory.total_size()
    print(total)

    directories.sort(key=lambda d: d.total_size(), reverse=True)
    directory_to_delete = directories[0]
    for directory in directories[1:]:
        x = directory.total_size()
        if 70_000_000 - (home_directory.total_size() - directory.total_size()) >= 30_000_000:
            directory_to_delete = directory
        else:
            print(directory_to_delete.total_size())
            return


if __name__ == '__main__':
    commands = open('challenge_input.txt').read().split('\n')
    challenge_1(commands)
