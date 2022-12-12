step_count = 0
path_list = []

def challenge_1(maze):
    start_coords, end_coords = get_coords(maze)
    traverse(start_coords, end_coords)


def traverse(start_coords, end_coords, maze, came_from):
    global step_count
    global path_list
    step_count += 1
    # Check if end
    if start_coords == end_coords:
        step_count -= 1
        path_list.append(step_count)
        return

    # Move up
    if start_coords[0] != len(maze) - 1 and ord(maze[start_coords[0]][start_coords[1]]) <= ord(maze[start_coords[0]][start_coords[1]]) - 1 and came_from != 'D':
        traverse([start_coords[0] + 1, start_coords[1]], end_coords, maze, 'U')

    # Move down
    if start_coords[0] != len(maze) - 1 and ord(maze[start_coords[0]][start_coords[1]]) <= ord(
            maze[start_coords[0]][start_coords[1]]) - 1 and came_from != 'D':
        traverse([start_coords[0] + 1, start_coords[1]], end_coords, maze, 'U')

    # Move down
    if start_coords[0] != len(maze) - 1 and ord(maze[start_coords[0]][start_coords[1]]) <= ord(
            maze[start_coords[0]][start_coords[1]]) - 1 and came_from != 'D':
        traverse([start_coords[0] + 1, start_coords[1]], end_coords, maze, 'U')

    # Move down
    if start_coords[0] != len(maze) - 1 and ord(maze[start_coords[0]][start_coords[1]]) <= ord(
            maze[start_coords[0]][start_coords[1]]) - 1 and came_from != 'D':
        traverse([start_coords[0] + 1, start_coords[1]], end_coords, maze, 'U')

def get_coords(maze):
    s_x, s_y = 0, 0
    e_x, e_y = 0, 0
    for i, row in enumerate(maze):
        for j, column in enumerate(row):
            if maze[i][j] == 'S':
                s_x, s_y = i, j
            if maze[i][j] == 'E':
                e_x, e_y = i, j
    return [s_x, s_y], [e_x, e_y]


if __name__ == '__main__':
    m = [[*line] for line in open('challenge_input.txt').read().split('\n')]
    challenge_1(m)
