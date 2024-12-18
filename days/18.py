import itertools
import aoc

day = 18
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def pathfinding(grid):
    distances = [[None] * dim for _ in range(dim)]
    distances[0][0] = 0

    queue = [(0, 0)]

    for step in itertools.count():
        new_queue = []
        for pos in queue:
            # Get all neighbours
            neighbours = []
            if 0 <= pos[0] + 1 < dim and 0 <= pos[1] < dim and grid[pos[1]][pos[0]+1]:
                neighbours.append((pos[0] + 1, pos[1]))
            if 0 <= pos[0] - 1 < dim and 0 <= pos[1] < dim and grid[pos[1]][pos[0]-1]:
                neighbours.append((pos[0] - 1, pos[1]))
            if 0 <= pos[0] < dim and 0 <= pos[1] + 1 < dim and grid[pos[1]+1][pos[0]]:
                neighbours.append((pos[0], pos[1] + 1))
            if 0 <= pos[0] < dim and 0 <= pos[1] - 1 < dim and grid[pos[1]-1][pos[0]]:
                neighbours.append((pos[0], pos[1] - 1))

            for neighbour in neighbours:
                # Not yet visited
                if distances[neighbour[1]][neighbour[0]] == None:
                    distances[neighbour[1]][neighbour[0]] = step + 1
                    new_queue.append(neighbour)

        queue = new_queue

        if distances[dim-1][dim-1] != None or not queue:
            break

    return distances[dim-1][dim-1]


def part_1(input: str):
    grid = [[True] * dim for _ in range(dim)]

    for line in input.splitlines()[:bytes_fallen]:
        (x, y) = map(int, line.split(","))
        grid[y][x] = False

    return pathfinding(grid)


def part_2(input: str):
    grid = [[True] * dim for _ in range(dim)]

    for line in input.splitlines():
        (x, y) = map(int, line.split(","))
        grid[y][x] = False

        if not pathfinding(grid):
            break

    return f"{x},{y}"

# ----------


use_example = False

dim = 7 if use_example else 71
bytes_fallen = 12 if use_example else 1024

if use_example:
    print(f"----- Day {day:02} ----- (Example Input)")
    input = aoc_example
else:
    print(f"----- Day {day:02} ----- (Actual Input)")
    input = aoc_input

aoc.run(lambda: part_1(input), part=1)
aoc.run(lambda: part_2(input), part=2)
