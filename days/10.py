from collections import defaultdict
import aoc

day = 10
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1_count(grid, x, y):
    trails = set([(x, y)])

    for i in range(1, 10):
        new_trails = set()
        for trail in trails:
            positions = [(trail[0] - 1, trail[1]),
                         (trail[0] + 1, trail[1]),
                         (trail[0], trail[1] - 1),
                         (trail[0], trail[1] + 1)]
            for pos in positions:
                if 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0]) and grid[pos[1]][pos[0]] == i:
                    new_trails.add(pos)

        trails = new_trails

    return len(trails)


def part_2_count(grid, x, y):
    trails = defaultdict(int, {(x, y): 1})

    for i in range(1, 10):
        new_trails = defaultdict(int)
        for (trail, rating) in trails.items():
            positions = [(trail[0] - 1, trail[1]),
                         (trail[0] + 1, trail[1]),
                         (trail[0], trail[1] - 1),
                         (trail[0], trail[1] + 1)]
            for pos in positions:
                if 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0]) and grid[pos[1]][pos[0]] == i:
                    new_trails[pos] += rating

        trails = new_trails

    return sum(trails.values())


def part_1(input: str):
    grid = [[int(char) for char in line] for line in input.splitlines()]

    d = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                continue

            d += part_1_count(grid, x, y)

    return d


def part_2(input: str):
    grid = [[int(char) for char in line] for line in input.splitlines()]

    d = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                continue

            d += part_2_count(grid, x, y)

    return d

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
