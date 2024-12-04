import numpy as np
import aoc

day = 4
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    grid = np.array([list(line) for line in input.splitlines()])
    d = 0

    # Horizontal
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 3):
            s = "".join(grid[y, x:x+4])
            if s == "XMAS" or s == "SAMX":
                d += 1

    # Vertical
    for y in range(len(grid) - 3):
        for x in range(len(grid[0])):
            s = "".join(grid[y:y+4, x])
            if s == "XMAS" or s == "SAMX":
                d += 1

    # Downward diagonal
    for y in range(len(grid) - 3):
        for x in range(len(grid[0]) - 3):
            s = "".join(grid[y + i, x + i] for i in range(4))
            if s == "XMAS" or s == "SAMX":
                d += 1

    # Upward diagonal
    for y in range(len(grid) - 3):
        for x in range(3, len(grid[0])):
            s = "".join(grid[y + i, x - i] for i in range(4))
            if s == "XMAS" or s == "SAMX":
                d += 1

    return d


def part_2(input: str):
    grid = np.array([list(line) for line in input.splitlines()])
    d = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y, x] != "A":
                continue

            a = (grid[y-1, x-1] == "M" and grid[y+1, x+1] ==
                 "S") or (grid[y-1, x-1] == "S" and grid[y+1, x+1] == "M")
            b = (grid[y+1, x-1] == "M" and grid[y-1, x+1] ==
                 "S") or (grid[y+1, x-1] == "S" and grid[y-1, x+1] == "M")
            if a and b:
                d += 1

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
