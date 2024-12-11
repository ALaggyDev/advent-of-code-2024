from collections import defaultdict
import itertools
import aoc

day = 8
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    lines = input.splitlines()

    antennas_freq: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    # Find all antennas
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(list(line)):
            if char == ".":
                continue

            antennas_freq[char].append((x, y))

    antinodes = set()

    # Loop through all pairs of antennas
    for antennas in antennas_freq.values():
        for (ant_1, ant_2) in itertools.permutations(antennas, 2):
            pos = (2 * ant_1[0] - ant_2[0], 2 * ant_1[1] - ant_2[1])

            if 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
                antinodes.add(pos)

    return len(antinodes)


def part_2(input: str):
    lines = input.splitlines()

    antennas_freq: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    # Find all antennas
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(list(line)):
            if char == ".":
                continue

            antennas_freq[char].append((x, y))

    antinodes = set()

    # Loop through all pairs of antennas
    for antennas in antennas_freq.values():
        for (ant_1, ant_2) in itertools.permutations(antennas, 2):
            antinodes.add(ant_1)

            for i in itertools.count(1):
                pos = (i * (ant_1[0] - ant_2[0]) + ant_1[0],
                       i * (ant_1[1] - ant_2[1]) + ant_1[1])

                if 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0]):
                    antinodes.add(pos)
                else:
                    break

    return len(antinodes)

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
