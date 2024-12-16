from collections import defaultdict
import heapq
import aoc

day = 16
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------

# This is a horrible implementation of Dijkstra's algorithm


def get_neighbors(grid, state):
    (x, y, facing) = state

    neighbors = []

    if facing == 0:
        pos = (x + 1, y)
    elif facing == 1:
        pos = (x, y + 1)
    elif facing == 2:
        pos = (x - 1, y)
    elif facing == 3:
        pos = (x, y - 1)
    if grid[pos[1]][pos[0]] != "#":
        neighbors.append((1, (pos[0], pos[1], facing)))

    neighbors.append((1000, (x, y, (facing - 1) % 4)))
    neighbors.append((1000, (x, y, (facing + 1) % 4)))

    return neighbors


class Node:
    def __init__(self):
        self.d = float('inf')
        self.parents = []
        self.visited = False


def dijkstra(grid, start, ends):
    nodes = defaultdict(lambda: Node())
    nodes[start].d = 0

    queue = [(0, start)]  # priority queue (heap)

    while queue:
        d, node = heapq.heappop(queue)
        if node in ends:
            break

        if nodes[node].visited:
            continue
        nodes[node].visited = True

        for (edge_d, neighbor) in get_neighbors(grid, node):
            if nodes[neighbor].visited:
                continue

            new_d = d + edge_d
            if new_d < nodes[neighbor].d:
                nodes[neighbor].d = new_d
                nodes[neighbor].parents = [node]
                heapq.heappush(queue, (new_d, neighbor))
            elif new_d == nodes[neighbor].d:
                nodes[neighbor].parents.append(node)

    return nodes


def find_end_nodes(nodes, ends: list):
    return min(ends, key=lambda end: nodes[end].d)


def part_1(input: str):
    grid = [list(line) for line in input.splitlines()]

    for (y, line) in enumerate(grid):
        for (x, char) in enumerate(line):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)

    ends = [(end[0], end[1], 0),
            (end[0], end[1], 1),
            (end[0], end[1], 2),
            (end[0], end[1], 3)]
    nodes = dijkstra(grid, (start[0], start[1], 0), ends)

    end_node = find_end_nodes(nodes, ends)

    return nodes[end_node].d


def part_2(input: str):
    grid = [list(line) for line in input.splitlines()]

    for (y, line) in enumerate(grid):
        for (x, char) in enumerate(line):
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)

    ends = [(end[0], end[1], 0),
            (end[0], end[1], 1),
            (end[0], end[1], 2),
            (end[0], end[1], 3)]
    nodes = dijkstra(grid, (start[0], start[1], 0), ends)

    end_node = find_end_nodes(nodes, ends)

    queue = set([end_node])

    best_nodes = set()
    while queue:
        node = queue.pop()
        best_nodes.add((node[0], node[1]))

        queue.update(nodes[node].parents)

    return len(best_nodes)

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
