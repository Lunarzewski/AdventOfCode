def most_calories(input_file_name):
    with open(input_file_name) as f:
        lines = f.readlines()
        largest_calories = 0
        current_count = 0

        for line in lines:
            if line == '\n':
                if current_count > largest_calories:
                    largest_calories = current_count
                current_count = 0
            else:
                current_count += int(line)
        print(largest_calories)


if __name__ == '__main__':
    most_calories('challenge_input.txt')
