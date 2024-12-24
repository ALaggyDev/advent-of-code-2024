import aoc

day = 24
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def part_1(input: str):
    # Parsing

    wires = {}
    conns = []

    lines = iter(input.splitlines())

    for line in lines:
        if not line:
            break

        wires[line[:3]] = int(line[5])

    for line in lines:
        (a, b) = line.split(" -> ")
        (a1, a2, a3) = a.split(" ")
        conns.append((a1, a2, a3, b))

    # Executing

    while conns:
        new_conns = []
        for conn in conns:
            if (conn[0] in wires) and (conn[2] in wires):
                if conn[1] == "AND":
                    wires[conn[3]] = wires[conn[0]] & wires[conn[2]]
                elif conn[1] == "OR":
                    wires[conn[3]] = wires[conn[0]] | wires[conn[2]]
                elif conn[1] == "XOR":
                    wires[conn[3]] = wires[conn[0]] ^ wires[conn[2]]
            else:
                new_conns.append(conn)
        conns = new_conns

    # Fetching answer

    out = ""
    for i in range(100):
        key = f"z{i:02}"
        if key in wires:
            out = str(wires[key]) + out
        else:
            break

    return int(out, 2)


def part_2(input: str):
    # Parsing

    wires = {}
    conns = {}

    lines = iter(input.splitlines())

    for line in lines:
        if not line:
            break

        wires[line[:3]] = int(line[5])

    for line in lines:
        (a, b) = line.split(" -> ")
        a = tuple(a.split(" "))
        conns[a] = b

    # Swapping

    print("This code requires manual solving! Input your findings into the swaps variable.")

    swaps = [("z10", "vcf"), ("z17", "fhg"), ("fsq", "dvb"), ("z39", "tnc")]

    for (a, b) in swaps:
        for gate, out in conns.items():
            if out == a:
                conns[gate] = b
            elif out == b:
                conns[gate] = a

    # Checking

    def find_comp(A: str, gate: str, B: str):
        if (A, gate, B) in conns:
            return conns[(A, gate, B)]
        elif (B, gate, A) in conns:
            return conns[(B, gate, A)]

        raise Exception(f"CAN NOT FIND GATE ({A}, {gate}, {B})")

    C_in = find_comp("x00", "AND", "y00")

    for i in range(1, 100):
        A = f"x{i:02}"
        B = f"y{i:02}"

        if A not in wires:
            break

        print(f"Iteration: {i}")

        comp_1 = find_comp(A, "XOR", B)
        comp_2 = find_comp(comp_1, "AND", C_in)
        comp_3 = find_comp(A, "AND", B)
        S = find_comp(comp_1, "XOR", C_in)
        C_out = find_comp(comp_2, "OR", comp_3)

        if S != f"z{i:02}":
            raise Exception(f"WRONG OUTPUT GATE ({S}, z{i:02})")

        C_in = C_out

    # Outputting

    out = [val for pair in swaps for val in pair]
    out.sort()
    return ",".join(out)

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
