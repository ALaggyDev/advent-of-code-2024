from collections import defaultdict
import aoc

day = 11
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    stones = [int(stone) for stone in input.split(" ")]

    for _ in range(25):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                new_stones.append(int(string[:len(string)//2]))
                new_stones.append(int(string[len(string)//2:]))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


def part_2(input: str):
    stones = dict.fromkeys((int(stone) for stone in input.split(" ")), 1)
    stones = defaultdict(int, stones)

    for _ in range(75):
        new_stones = defaultdict(int)

        for (stone, freq) in stones.items():
            if stone == 0:
                new_stones[1] += freq
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                new_stones[int(string[:len(string)//2])] += freq
                new_stones[int(string[len(string)//2:])] += freq
            else:
                new_stones[stone * 2024] += freq

        stones = new_stones

    return sum(stones.values())

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
