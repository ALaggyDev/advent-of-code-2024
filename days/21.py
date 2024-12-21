import aoc

day = 21
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------

numeric_coords = {
    'A': (2, 3),
    '0': (1, 3),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0)
}


direction_coords = {
    'A': (2, 0),
    '^': (1, 0),
    '>': (2, 1),
    'v': (1, 1),
    '<': (0, 1)
}

numeric_empty = (0, 3)
direction_empty = (0, 0)


def move(pos, new_pos, numeric):
    empty = numeric_empty if numeric else direction_empty

    dx = new_pos[0] - pos[0]
    dy = new_pos[1] - pos[1]

    if dx >= 0:
        move_x = '>' * dx
    else:
        move_x = '<' * -dx

    if dy >= 0:
        move_y = 'v' * dy
    else:
        move_y = '^' * -dy

    if dx == 0:
        return [move_y + 'A']
    elif dy == 0:
        return [move_x + 'A']

    result = []

    if (new_pos[0], pos[1]) != empty:
        result.append(move_x + move_y + 'A')
    if (pos[0], new_pos[1]) != empty:
        result.append(move_y + move_x + 'A')

    return result


def find_layer(input: str, memos: dict, i: int, numeric: bool):
    if i == 0:
        return len(input)

    coords = numeric_coords if numeric else direction_coords

    pos = coords["A"]

    count = 0

    for char in list(input):
        new_pos = coords[char]

        key = (i, pos[0], pos[1], new_pos[0], new_pos[1])

        if key not in memos:
            outputs = move(pos, new_pos, numeric)

            memos[key] = min(find_layer(output, memos, i-1, False)
                             for output in outputs)

        count += memos[key]
        pos = new_pos

    return count


def part_1(input: str):
    memos = {}  # (depth, x1, y1, x2, y2) -> count

    d = 0

    for line in input.splitlines():
        output = find_layer(line, memos, 3, True)

        d += int(line[:3]) * output

    return d


def part_2(input: str):
    memos = {}  # (depth, x1, y1, x2, y2) -> count

    d = 0

    for line in input.splitlines():
        output = find_layer(line, memos, 26, True)

        d += int(line[:3]) * output

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
