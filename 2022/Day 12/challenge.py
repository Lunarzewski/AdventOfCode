from collections import deque


def challenge_1(maze, start_coords, end_coords):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_x, max_y = len(maze), len(maze[0])
    path_list = deque([start_coords])
    explored_list = [start_coords]
    step_count_list = [0]
    while len(path_list) > 0:
        current_path = path_list.popleft()
        if current_path == end_coords:
            break
        for dx, dy in dirs:
            nx, ny = current_path[0] + dx, current_path[1] + dy
            if nx in range(max_x) and ny in range(max_y) and (nx, ny) not in explored_list:
                if maze[current_path[0]][current_path[1]] >= maze[nx][ny] - 1:
                    step_count_list.append(step_count_list[explored_list.index((current_path[0], current_path[1]))] + 1)
                    explored_list.append((nx, ny))
                    path_list.append((nx, ny))
    step_count_list.sort()
    print(step_count_list)


def get_coords(maze):
    s_x, s_y = 0, 0
    e_x, e_y = 0, 0
    for i, row in enumerate(maze):
        for j, column in enumerate(row):
            if maze[i][j] == 'S':
                s_x, s_y = i, j
                maze[i][j] = 'a'
            if maze[i][j] == 'E':
                e_x, e_y = i, j
                maze[i][j] = 'z'
    return (s_x, s_y), (e_x, e_y)


def challenge_2(maze, end_coords):
    starting_points_list = []
    for i, row in enumerate(maze):
        for j, column in enumerate(row):
            if maze[i][j] == 0:
                starting_points_list.append((i, j))

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_x, max_y = len(maze), len(maze[0])

    max_steps_list = []
    for start_coords in starting_points_list:
        path_list = deque([start_coords])
        explored_list = [start_coords]
        step_count_list = [0]
        while len(path_list) > 0:
            current_path = path_list.popleft()
            if current_path == end_coords:
                step_count_list.sort()
                max_steps_list.append(step_count_list[-1])
                break
            for dx, dy in dirs:
                nx, ny = current_path[0] + dx, current_path[1] + dy
                if nx in range(max_x) and ny in range(max_y) and (nx, ny) not in explored_list:
                    if maze[current_path[0]][current_path[1]] >= maze[nx][ny] - 1:
                        step_count_list.append(
                            step_count_list[explored_list.index((current_path[0], current_path[1]))] + 1)
                        explored_list.append((nx, ny))
                        path_list.append((nx, ny))
    max_steps_list.sort()
    print(max_steps_list)


if __name__ == '__main__':
    m = [[*line] for line in open('challenge_input.txt').read().split('\n')]
    s, e = get_coords(m)
    g = [[ord(c) - ord("a") for c in r] for r in m]
    challenge_1(g, s, e)
    challenge_2(g, e)
