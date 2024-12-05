import aoc

day = 5
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def parse_rules(lines):
    rules: dict[int, set[int]] = {}

    for line in lines:
        if not line:
            break

        a, b = int(line[:2]), int(line[3:5])
        if a not in rules:
            rules[a] = set()
        rules[a].add(b)

    return rules


def is_bad_update(rules: dict[int, set[int]], pages: list[int]):
    for i in range(len(pages)):
        if pages[i] not in rules:
            continue

        for j in range(i):
            if pages[j] in rules[pages[i]]:
                return (i, j)

    return False


def part_1(input: str):
    lines = iter(input.splitlines())
    rules = parse_rules(lines)

    d = 0

    # Updates
    for line in lines:
        pages = [int(page) for page in line.split(",")]

        if not is_bad_update(rules, pages):
            d += pages[len(pages) // 2]

    return d


def part_2(input: str):
    lines = iter(input.splitlines())
    rules = parse_rules(lines)

    d = 0

    # Updates
    for line in lines:
        pages = [int(num) for num in line.split(",")]

        if not is_bad_update(rules, pages):
            continue

        while True:
            res = is_bad_update(rules, pages)
            if res:
                (i, j) = res
                (pages[i], pages[j]) = (pages[j], pages[i])
            else:
                break

        d += pages[len(pages) // 2]

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
