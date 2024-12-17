import aoc
from z3 import *

day = 17
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


class Machine:
    def __init__(self, A: int, B: int, C: int, program: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.ip = 0
        self.out = []

    def run(self):
        while self.ip < len(self.program):
            self.step()

    def step(self):
        # Opcode
        opcode = self.program[self.ip]

        # Literal operand
        l_operand = self.program[self.ip+1]

        # Combo operand
        if l_operand <= 3:
            c_operand = l_operand
        elif l_operand == 4:
            c_operand = self.A
        elif l_operand == 5:
            c_operand = self.B
        elif l_operand == 6:
            c_operand = self.C

        self.ip += 2

        if opcode == 0:
            # adv
            self.A >>= c_operand
        elif opcode == 1:
            # bxl
            self.B ^= l_operand
        elif opcode == 2:
            # bst
            self.B = c_operand & 0b111
        elif opcode == 3:
            # jnz
            if self.A:
                self.ip = l_operand
        elif opcode == 4:
            # bxc
            self.B ^= self.C
        elif opcode == 5:
            # out
            self.out.append(c_operand & 0b111)
        elif opcode == 6:
            # bdv
            self.B = self.A >> c_operand
        elif opcode == 7:
            # cdv
            self.C = self.A >> c_operand

    def get_output(self):
        return ",".join(map(str, self.out))


def part_1(input: str):
    lines = input.splitlines()

    machine = Machine(int(lines[0][12:]),
                      int(lines[1][12:]),
                      int(lines[2][12:]),
                      [int(num) for num in lines[4][9:].split(",")])

    machine.run()

    return machine.get_output()


def part_2(input: str):
    program = [int(num) for num in input.splitlines()[4][9:].split(",")]

    # Program: 2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0

    # self.B = self.A & 0b111            bst 4
    # self.B ^= 1                        bxl 1
    # self.C = self.A >> self.B          cdv 5
    # self.B ^= self.C                   bxc 6
    # self.A >>= 3                       adv 3
    # self.B ^= 0b100                    bxl 4
    # self.out.append(self.B & 0b111)    out 5
    # if self.A:                         jnz 5
    #     self.ip = 0

    # There's no guarantees that this code outputs the lowest value, but it works anyway

    solver = Solver()

    out_A = BitVec("A", len(program) * 3)
    A = out_A

    for i in range(len(program)):
        B = (A & 0b111) ^ 1
        B = (B ^ (LShR(A, B))) ^ 0b100
        A = LShR(A, 3)

        solver.add(B & 0b111 == program[i])
        if i == len(program) - 1:
            solver.add(A == 0)
        else:
            solver.add(A != 0)

    return solver.model().eval(out_A)


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
