import itertools
import aoc

day = 15
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    lines = iter(input.splitlines())

    # Construct grid
    grid = []
    pos = None
    for (y, line) in enumerate(lines):
        if line == "":
            break
        row = []
        for (x, char) in enumerate(line):
            if char == "@":
                pos = (x, y)
            row.append(char)
        grid.append(row)

    # Perform moves
    for move in "".join(lines):
        if move == "<":
            offset = (-1, 0)
        elif move == ">":
            offset = (1, 0)
        elif move == "^":
            offset = (0, -1)
        elif move == "v":
            offset = (0, 1)

        cur = pos

        while True:
            cur = (cur[0] + offset[0], cur[1] + offset[1])

            item = grid[cur[1]][cur[0]]
            if item == ".":
                # Move
                grid[cur[1]][cur[0]] = "O"
                grid[pos[1]][pos[0]] = "."
                pos = (pos[0] + offset[0], pos[1] + offset[1])
                grid[pos[1]][pos[0]] = "@"
                break
            elif item == "#":
                # Hit wall
                break

    # Calculate GPS
    d = 0
    for (y, line) in enumerate(grid):
        for (x, char) in enumerate(line):
            if char == "O":
                d += 100 * y + x

    return d


def part_2(input: str):
    lines = iter(input.splitlines())

    # Construct grid
    grid = []
    pos = None
    for (y, line) in enumerate(lines):
        if line == "":
            break
        row = []
        for (x, char) in enumerate(line):
            if char == "#":
                row.extend("##")
            elif char == "O":
                row.extend("[]")
            elif char == ".":
                row.extend("..")
            elif char == "@":
                pos = (x * 2, y)
                row.extend("@.")
        grid.append(row)

    # Perform moves
    for move in "".join(lines):
        if move == "<":
            offset = (-1, 0)
        elif move == ">":
            offset = (1, 0)
        elif move == "^":
            offset = (0, -1)
        elif move == "v":
            offset = (0, 1)

        # Find all moving tiles

        queue = [pos]
        hit_wall = False

        for i in itertools.count():
            if i >= len(queue):
                break
            cur = queue[i]

            cur_next = (cur[0] + offset[0], cur[1] + offset[1])
            cur_next_item = grid[cur_next[1]][cur_next[0]]

            if cur_next_item == "[":
                if cur_next not in queue:
                    queue.append(cur_next)
                if (cur_next[0] + 1, cur_next[1]) not in queue:
                    queue.append((cur_next[0] + 1, cur_next[1]))
            elif cur_next_item == "]":
                if cur_next not in queue:
                    queue.append(cur_next)
                if (cur_next[0] - 1, cur_next[1]) not in queue:
                    queue.append((cur_next[0] - 1, cur_next[1]))
            elif cur_next_item == "#":
                # Hit wall
                hit_wall = True
                break

        if hit_wall:
            continue

        # Move tiles

        pos = (pos[0] + offset[0], pos[1] + offset[1])

        items = [grid[cur[1]][cur[0]] for cur in queue]
        for (cur, item) in zip(queue, items):
            grid[cur[1] + offset[1]][cur[0] + offset[0]] = item
            if (cur[0] - offset[0], cur[1] - offset[1]) not in queue:
                grid[cur[1]][cur[0]] = "."

    # Calculate GPS
    d = 0
    for (y, line) in enumerate(grid):
        for (x, char) in enumerate(line):
            if char == "[":
                d += 100 * y + x

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
