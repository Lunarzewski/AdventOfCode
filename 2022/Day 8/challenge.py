def construct_grid():
    input_lines = open('challenge_input.txt').read().split()
    return [[int(height) for height in list(line)] for line in input_lines]


def challenge_1(tree_grid):
    visible_trees = 0
    for i, row in enumerate(tree_grid):
        for j, tree in enumerate(row):
            if j == 0 or check_left(tree_grid, i, j, tree):
                visible_trees += 1
            elif j == len(row) - 1 or check_right(tree_grid, i, j, tree):
                visible_trees += 1
            elif i == 0 or check_up(tree_grid, i, j, tree):
                visible_trees += 1
            elif i == len(tree_grid) - 1 or check_down(tree_grid, i, j, tree):
                visible_trees += 1
    print(visible_trees)


def go_left(curr_score, tree_grid, i, j, tree):
    if j > 0:
        if tree > tree_grid[i][j - 1]:
            curr_score += 1
            curr_score = go_left(curr_score, tree_grid, i, j-1, tree)
        else:
            curr_score += 1
    return curr_score


def go_right(curr_score, tree_grid, i, j, tree):
    if j < len(tree_grid[0]) - 1:
        if tree > tree_grid[i][j + 1]:
            curr_score += 1
            curr_score = go_right(curr_score, tree_grid, i, j+1, tree)
        else:
            curr_score += 1
    return curr_score


def go_up(curr_score, tree_grid, i, j, tree):
    if i > 0:
        if tree > tree_grid[i - 1][j]:
            curr_score += 1
            curr_score = go_up(curr_score, tree_grid, i-1, j, tree)
        else:
            curr_score += 1
    return curr_score


def go_down(curr_score, tree_grid, i, j, tree):
    if i < len(tree_grid) - 1:
        if tree > tree_grid[i + 1][j]:
            curr_score += 1
            curr_score = go_down(curr_score, tree_grid, i+1, j, tree)
        else:
            curr_score += 1
    return curr_score


def challenge_2(tree_grid):
    highest_score = 0
    for i, row in enumerate(tree_grid):
        for j, tree in enumerate(row):

            left_score = go_left(0, tree_grid, i, j, tree)
            right_score = go_right(0, tree_grid, i, j, tree)
            up_score = go_up(0, tree_grid, i, j, tree)
            down_score = go_down(0, tree_grid, i, j, tree)
            total_score = left_score * right_score * up_score * down_score
            if total_score > highest_score:
                highest_score = total_score
    print(highest_score)


def check_left(tree_grid, i, j, tree):
    if j > 0:
        if tree > tree_grid[i][j - 1]:
            return check_left(tree_grid, i, j - 1, tree)
        else:
            return False
    return True


def check_right(tree_grid, i, j, tree):
    if j < len(tree_grid[0]) - 1:
        if tree > tree_grid[i][j + 1]:
            return check_right(tree_grid, i, j + 1, tree)
        else:
            return False
    return True


def check_up(tree_grid, i, j, tree):
    if i > 0:
        if tree > tree_grid[i - 1][j]:
            return check_up(tree_grid, i - 1, j, tree)
        else:
            return False
    return True


def check_down(tree_grid, i, j, tree):
    if i < len(tree_grid) - 1:
        if tree > tree_grid[i + 1][j]:
            return check_down(tree_grid, i + 1, j, tree)
        else:
            return False
    return True


if __name__ == '__main__':
    grid = construct_grid()
    challenge_1(grid)
    challenge_2(grid)
