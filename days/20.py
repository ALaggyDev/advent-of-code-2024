import itertools
import aoc
from collections import defaultdict

day = 20
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def prepare(input: str):
    grid = [list(line) for line in input.splitlines()]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)

    distances = [[None] * len(grid[0]) for _ in range(len(grid))]
    distances[start[1]][start[0]] = 0

    pos = start
    path = [start]

    for i in itertools.count(1):
        positions = [(pos[0]+1, pos[1]),
                     (pos[0]-1, pos[1]),
                     (pos[0], pos[1]+1),
                     (pos[0], pos[1]-1)]

        for new_pos in positions:
            if grid[new_pos[1]][new_pos[0]] != "#" and distances[new_pos[1]][new_pos[0]] == None:
                distances[new_pos[1]][new_pos[0]] = i
                pos = new_pos
                path.append(pos)
                break
        else:
            break

    return (grid, distances, path)


def part_1(input: str):
    (grid, distances, path) = prepare(input)

    # Calculate

    total = 0

    for pos in path:
        positions = [(pos[0]+2, pos[1]),
                     (pos[0]-2, pos[1]),
                     (pos[0], pos[1]+2),
                     (pos[0], pos[1]-2)]

        for next_pos in positions:
            if 0 <= next_pos[1] < len(grid) and 0 <= next_pos[0] < len(grid[0]) and grid[next_pos[1]][next_pos[0]] != "#":
                next_d = distances[next_pos[1]][next_pos[0]]
                d = distances[pos[1]][pos[0]]
                saved = next_d - d - 2

                if saved >= 100:
                    total += 1

    return total


def part_2(input: str):
    (grid, distances, path) = prepare(input)

    # Calculate

    total = 0

    for pos in path:
        for off_y in range(-20, 21):
            for off_x in range(abs(off_y) - 20, 21 - abs(off_y)):
                next_pos = (pos[0] + off_x, pos[1] + off_y)

                if 0 <= next_pos[1] < len(grid) and 0 <= next_pos[0] < len(grid[0]) and grid[next_pos[1]][next_pos[0]] != "#":
                    next_d = distances[next_pos[1]][next_pos[0]]
                    d = distances[pos[1]][pos[0]]
                    saved = next_d - d - abs(off_x) - abs(off_y)

                    if saved >= 100:
                        total += 1

    return total

# ----------


use_example = False

if use_example:
    print(f"----- Day {day:02} ----- (Example Input)")
    input = aoc_example
else:
    print(f"----- Day {day:02} ----- (Actual Input)")
    input = aoc_input

aoc.run(lambda: part_1(input), part=1)
aoc.run(lambda: part_2(input), part=2)
