# 0 -> air
# 1 -> solid
# 2 -> solid sand
from collections import defaultdict


def challenge_1(grid):
    sand = (500, 0)
    sx, sy = sand
    directions = ((0, 1), (-1, 1), (1, 1))
    maxy = max(y for x, y in grid)
    while True:
        blocked = True
        for dx, dy in directions:
            if grid[(sx + dx, sy + dy)] == 0:
                sx += dx
                sy += dy
                blocked = False
                break
        if sy > maxy:
            break
        if blocked:
            grid[sx, sy] = 2
            if (sx, sy) == sand:
                break
            sx, sy = sand
    print(sum(1 for v in grid.values() if v == 2))


def challenge_2(grid):
    sand = (500, 0)
    sx, sy = sand
    directions = ((0, 1), (-1, 1), (1, 1))
    maxy = max(y for x, y in grid)
    for x in range(-1000, 1000):
        grid[x, maxy + 2] = 1
    while True:
        blocked = True
        for dx, dy in directions:
            if grid[(sx + dx, sy + dy)] == 0:
                sx += dx
                sy += dy
                blocked = False
                break
        if blocked:
            grid[sx, sy] = 2
            if (sx, sy) == sand:
                break
            sx, sy = sand
    print(sum(1 for v in grid.values() if v == 2))

def build_grid(rocks):
    grid = defaultdict(lambda: 0)
    for path in rocks:
        for (ax, ay), (bx, by) in zip(path, path[1:]):
            dx = abs(bx - ax)
            dy = abs(by - ay)
            if dx != 0:
                for i in range(dx + 1):
                    grid[ax + i if ax < bx else ax - i, ay] = 1
            if dy != 0:
                for i in range(dy + 1):
                    grid[ax, ay + i if ay < by else ay - i] = 1
    return grid


if __name__ == '__main__':
    r = [[tuple(map(int, y.split(","))) for y in x.split(' -> ')] for x in (open('challenge_input.txt').read().split('\n'))]
    challenge_1(build_grid(r))
    challenge_2(build_grid(r))
