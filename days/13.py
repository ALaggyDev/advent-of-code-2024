import itertools
import aoc

day = 13
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def solve_2_unknowns(a, b, c, d, e, f):
    # Solve:
    # ax + by = e
    # cx + dy = f

    delta = a * d - b * c

    return ((d * e - b * f) / delta, (a * f - c * e) / delta)


def part_1(input: str):
    out = 0

    for tmp, lines in itertools.groupby(input.splitlines(), lambda a: a == ""):
        if tmp:
            continue

        (a, c) = map(int, next(lines)[12:].split(", Y+"))
        (b, d) = map(int, next(lines)[12:].split(", Y+"))
        (e, f) = map(int, next(lines)[9:].split(", Y="))

        (x, y) = solve_2_unknowns(a, b, c, d, e, f)

        if x.is_integer() and y.is_integer():
            out += 3 * int(x) + int(y)

    return out


def part_2(input: str):
    out = 0

    for tmp, lines in itertools.groupby(input.splitlines(), lambda a: a == ""):
        if tmp:
            continue

        (a, c) = map(int, next(lines)[12:].split(", Y+"))
        (b, d) = map(int, next(lines)[12:].split(", Y+"))
        (e, f) = map(lambda val: int(val) + 10000000000000,
                     next(lines)[9:].split(", Y="))

        (x, y) = solve_2_unknowns(a, b, c, d, e, f)

        if x.is_integer() and y.is_integer():
            out += 3 * int(x) + int(y)

    return out

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
