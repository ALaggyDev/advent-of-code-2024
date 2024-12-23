from collections import defaultdict
import itertools
import aoc

day = 23
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def parse_conns(input: str):
    conns = defaultdict(list)

    for line in input.splitlines():
        a = line[:2]
        b = line[3:]

        conns[a].append(b)
        conns[b].append(a)

    return conns


def part_1(input: str):
    conns = parse_conns(input)

    sets = set()

    for (a, conns_a) in conns.items():
        for b in conns_a:
            for c in conns_a:
                if b == c:
                    continue

                if c in conns[b]:
                    out = [a, b, c]
                    out.sort()
                    sets.add(tuple(out))

    d = 0

    for set_of_three in sets:
        if any(a.startswith("t") for a in set_of_three):
            d += 1

    return d


def part_2(input: str):
    conns = parse_conns(input)

    biggest_size = 0
    biggest = None

    for (a, conns_a) in conns.items():
        for temp in itertools.product(range(2), repeat=len(conns_a)):
            conns_list = [conns_a[i] for i in range(len(conns_a)) if temp[i]]

            good = all([c in conns[b]
                        for b, c in itertools.combinations(conns_list, 2)])

            if good and len(conns_list) + 1 > biggest_size:
                biggest_size = len(conns_list) + 1
                biggest = conns_list + [a]

    biggest.sort()
    return ",".join(biggest)


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
