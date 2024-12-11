import aoc

day = 9
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def build_disk(input: str):
    # Build disk map
    nums = [int(num) for num in input]

    disk = []
    id = 0
    is_file = True
    for num in nums:
        if is_file:
            disk.extend([id] * num)
            id += 1
        else:
            disk.extend([None] * num)

        is_file = not is_file

    return disk


def calculate_checksum(disk: list):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != None:
            checksum += i * disk[i]

    return checksum


def part_1(input: str):
    disk = build_disk(input)

    # Two-pointers
    (a, b) = (0, len(disk) - 1)
    while True:
        while a < b and disk[a] != None:
            a += 1

        while a < b and disk[b] == None:
            b -= 1

        if a >= b:
            break

        disk[a] = disk[b]
        disk[b] = None

    return calculate_checksum(disk)


# This is not the most pretty code I have to admit, but it gets the job done :)
def part_2(input: str):
    disk = build_disk(input)

    lowest_filled = 0
    b = len(disk) - 1
    while True:
        while 0 < b and disk[b] == None:
            b -= 1

        cur_file = disk[b]
        size_b = 0
        while 0 < b and disk[b] == cur_file:
            b -= 1
            size_b += 1

        # Optimization
        for i in range(lowest_filled, len(disk)):
            if disk[i] != None:
                lowest_filled = i
            else:
                break

        a = lowest_filled

        found = False
        while a < b and not found:
            size_a = 0
            while a <= b and disk[a] != None:
                a += 1
            while a <= b and disk[a] == None:
                a += 1
                size_a += 1
                if size_a >= size_b:
                    found = True
                    break

        if b <= 0:
            break

        if not found:
            continue

        disk[b+1:b+1+size_a] = [None] * size_a
        disk[a-size_a:a] = [cur_file] * size_a

    return calculate_checksum(disk)


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
