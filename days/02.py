import aoc

day = 2
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def is_safe(levels: list[int]):
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    for i in range(1, len(levels)):
        if not 1 <= abs(levels[i] - levels[i - 1]) <= 3:
            return False

    return True


def part_1(input: str):
    n = 0

    for report in input.splitlines():
        levels = [int(level) for level in report.split(" ")]

        n += is_safe(levels)

    return n


def part_2(input: str):
    n = 0

    for report in input.splitlines():
        levels = [int(level) for level in report.split(" ")]

        safe = False
        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i+1:]):
                safe = True
                break

        n += safe

    return n

# ----------


input = aoc_input
# input = aoc_example

aoc.run(lambda: part_1(input), part=1)
aoc.run(lambda: part_2(input), part=2)
