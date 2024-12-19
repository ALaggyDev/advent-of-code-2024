import aoc

day = 19
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    lines = input.splitlines()

    patterns = lines[0].split(", ")

    d = 0

    for design in lines[2:]:
        possibles = [False] * (len(design)+1)
        possibles[0] = True

        for i in range(len(design)):
            if not possibles[i]:
                continue

            for pattern in patterns:
                if design.startswith(pattern, i):
                    possibles[i+len(pattern)] = True

        if possibles[-1]:
            d += 1

    return d


def part_2(input: str):
    lines = input.splitlines()

    patterns = lines[0].split(", ")

    d = 0

    for design in lines[2:]:
        possibles = [0] * (len(design)+1)
        possibles[0] = 1

        for i in range(len(design)):
            if not possibles[i]:
                continue

            for pattern in patterns:
                if design.startswith(pattern, i):
                    possibles[i+len(pattern)] += possibles[i]

        d += possibles[-1]

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
