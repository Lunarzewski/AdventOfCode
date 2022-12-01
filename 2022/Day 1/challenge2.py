def most_3_calories(input_file_name):
    with open(input_file_name) as f:
        lines = f.readlines()
        totals_list = []

        current_count = 0
        for line in lines:
            if line == '\n':
                totals_list.append(current_count)
                current_count = 0
            else:
                current_count += int(line)
        max_count = 0
        for i in range(3):
            max_count += totals_list.pop(totals_list.index(max(totals_list)))
        print(max_count)


if __name__ == '__main__':
    most_3_calories('challenge_input.txt')
