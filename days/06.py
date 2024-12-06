import aoc

day = 6
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def find_pos(grid: list[list[str]]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                return (x, y)


def run_grid(grid: list[list[str]], pos: tuple[int, int]):
    direction = 0

    states = set()

    stuck = False

    while True:
        # Add visited
        if (pos, direction) in states:
            # Stuck in a loop
            stuck = True
            break
        else:
            states.add((pos, direction))

        while True:
            # Try to move
            if direction == 0:
                next_pos = (pos[0], pos[1] - 1)
            elif direction == 1:
                next_pos = (pos[0] + 1, pos[1])
            elif direction == 2:
                next_pos = (pos[0], pos[1] + 1)
            elif direction == 3:
                next_pos = (pos[0] - 1, pos[1])

            # Check out of bounds
            out_of_bounds = not (0 <= next_pos[0] < len(
                grid) and 0 <= next_pos[1] < len(grid[0]))
            if out_of_bounds:
                break

            # Check obstacle
            if grid[next_pos[1]][next_pos[0]] == "#":
                direction = (direction + 1) % 4
            else:
                pos = next_pos
                break

        if out_of_bounds:
            break

    return (stuck, states)


def part_1(input: str):
    grid = [list(line) for line in input.splitlines()]

    # Run grid
    start_pos = find_pos(grid)
    (_, states) = run_grid(grid, start_pos)

    return len(set(state[0] for state in states))


def part_2(input: str):
    grid = [list(line) for line in input.splitlines()]

    # Run grid
    start_pos = find_pos(grid)
    (_, states) = run_grid(grid, start_pos)

    d = 0

    for pos in set(state[0] for state in states):
        if grid[pos[1]][pos[0]] == "^":
            continue

        # Run grid, but add obstacle to the current pos
        grid[pos[1]][pos[0]] = "#"
        (stuck, _) = run_grid(grid, start_pos)
        grid[pos[1]][pos[0]] = "."

        if stuck:
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
