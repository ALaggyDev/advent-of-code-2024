import aoc
import re

day = 3
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    d = 0
    for (a, b) in re.findall(r"mul\((\d+),(\d+)\)", input):
        d += int(a) * int(b)

    return d


def part_2(input: str):
    d = 0
    enabled = True
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", input):
        if m.group() == "do()":
            enabled = True
        elif m.group() == "don't()":
            enabled = False
        elif enabled:
            d += int(m.group(1)) * int(m.group(2))

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
