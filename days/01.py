import aoc

day = 1
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def parse(input: str):
    left = []
    right = []
    for line in input.splitlines():
        (a, b) = map(int, line.split("   "))
        left.append(a)
        right.append(b)

    return (left, right)


def part_1(input: str):
    (left, right) = parse(input)

    left.sort()
    right.sort()

    return sum(abs(a - b) for (a, b) in zip(left, right))


def part_2(input: str):
    (left, right) = parse(input)

    return sum(a * right.count(a) for a in left)

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
