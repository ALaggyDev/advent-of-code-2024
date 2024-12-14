import itertools
import time
import aoc

day = 14
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def parse_robots(input: str):
    robots = []

    for line in input.splitlines():
        (a, b) = line.split(" ")
        pos = tuple(map(int, a[2:].split(",")))
        vel = tuple(map(int, b[2:].split(",")))

        robots.append({"pos": pos, "vel": vel})

    return robots


def update_robots(robots: list):
    for robot in robots:
        new_pos = (robot["pos"][0] + robot["vel"][0],
                   robot["pos"][1] + robot["vel"][1])
        new_pos = (new_pos[0] % dims[0], new_pos[1] % dims[1])
        robot["pos"] = new_pos


def print_robots(robots: list):
    grid = [[" "] * dims[0] for _ in range(dims[1])]

    for robot in robots:
        grid[robot["pos"][1]][robot["pos"][0]] = "*"

    print("|" * dims[0])
    for line in grid:
        print("|" + "".join(line) + "|")
    print("|" * dims[0])


def part_1(input: str):
    robots = parse_robots(input)

    for _ in range(100):
        update_robots(robots)

    a = sum(1 for robot in robots if robot["pos"]
            [0] < dims[0]//2 and robot["pos"][1] < dims[1]//2)
    b = sum(1 for robot in robots if robot["pos"]
            [0] < dims[0]//2 and robot["pos"][1] > dims[1]//2)
    c = sum(1 for robot in robots if robot["pos"]
            [0] > dims[0]//2 and robot["pos"][1] < dims[1]//2)
    d = sum(1 for robot in robots if robot["pos"]
            [0] > dims[0]//2 and robot["pos"][1] > dims[1]//2)

    return a * b * c * d


def part_2(input: str):
    robots = parse_robots(input)

    for i in itertools.count():
        if (i - 27) % 103 == 0 and (i - 52) % 101 == 0:
            print_robots(robots)
            print(f"Iteration: {i}")
            time.sleep(.2)

        update_robots(robots)


# ----------
use_example = False

dims = (11, 7) if use_example else (101, 103)

if use_example:
    print(f"----- Day {day:02} ----- (Example Input)")
    input = aoc_example
else:
    print(f"----- Day {day:02} ----- (Actual Input)")
    input = aoc_input

aoc.run(lambda: part_1(input), part=1)
aoc.run(lambda: part_2(input), part=2)
