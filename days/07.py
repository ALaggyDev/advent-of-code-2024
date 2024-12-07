import aoc

day = 7
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    d = 0

    for line in input.splitlines():
        [start, end] = line.split(": ")

        value = int(start)
        nums = [int(num) for num in end.split(" ")]

        possibles = [nums[0]]
        for i in range(1, len(nums)):
            possibles = [possible + nums[i] for possible in possibles] + \
                [possible * nums[i] for possible in possibles]

        if value in possibles:
            d += value

    return d


def part_2(input: str):
    d = 0

    for line in input.splitlines():
        [start, end] = line.split(": ")

        value = int(start)
        nums = [int(num) for num in end.split(" ")]

        possibles = [nums[0]]
        for i in range(1, len(nums)):
            possibles = [possible + nums[i] for possible in possibles] + \
                [possible * nums[i] for possible in possibles] + \
                [int(str(possible) + str(nums[i])) for possible in possibles]

        if value in possibles:
            d += value

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
