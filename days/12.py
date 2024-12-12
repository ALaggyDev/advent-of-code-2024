import aoc

day = 12
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def within_bounds(grid, pos):
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])


def part_1(input: str):
    grid = [list(line) for line in input.splitlines()]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    d = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if visited[y][x]:
                continue
            visited[y][x] = True

            area = 0
            perimeter = 0

            # Flood fill

            plant = grid[y][x]
            queue = [(x, y)]

            while len(queue) > 0:
                cur = queue.pop()

                area += 1

                offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for offset in offsets:
                    other = (cur[0] + offset[0], cur[1] + offset[1])

                    same_region = within_bounds(
                        grid, other) and grid[other[1]][other[0]] == plant
                    if not same_region:
                        perimeter += 1

                    if same_region and not visited[other[1]][other[0]]:
                        queue.append(other)
                        visited[other[1]][other[0]] = True

            d += area * perimeter

    return d


def part_2(input: str):
    grid = [list(line) for line in input.splitlines()]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    d = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if visited[y][x]:
                continue
            visited[y][x] = True

            area = 0
            corners = 0

            plant = grid[y][x]
            queue = [(x, y)]

            # Flood fill

            while len(queue) > 0:
                cur = queue.pop()

                area += 1

                offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for offset in offsets:
                    other = (cur[0] + offset[0], cur[1] + offset[1])

                    same_region = within_bounds(
                        grid, other) and grid[other[1]][other[0]] == plant

                    if same_region and not visited[other[1]][other[0]]:
                        queue.append(other)
                        visited[other[1]][other[0]] = True

                # Count corners

                offsets = [((-1, 0), (0, -1)),
                           ((-1, 0), (0, 1)),
                           ((1, 0), (0, -1)),
                           ((1, 0), (0, 1))]

                for offset_1, offset_2 in offsets:
                    other_1 = (cur[0] + offset_1[0], cur[1] + offset_1[1])
                    other_2 = (cur[0] + offset_2[0], cur[1] + offset_2[1])
                    other_3 = (cur[0] + offset_1[0] + offset_2[0],
                               cur[1] + offset_1[1] + offset_2[1])

                    same_region_1 = within_bounds(
                        grid, other_1) and grid[other_1[1]][other_1[0]] == plant
                    same_region_2 = within_bounds(
                        grid, other_2) and grid[other_2[1]][other_2[0]] == plant
                    same_region_3 = within_bounds(
                        grid, other_3) and grid[other_3[1]][other_3[0]] == plant
                    if same_region_1 == same_region_2 and not (same_region_1 and same_region_3):
                        corners += 1

            # By V - E + F = 2, sides == corners
            d += area * corners

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
