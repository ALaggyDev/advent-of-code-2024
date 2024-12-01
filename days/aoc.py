from typing import Callable
from pathlib import Path
import time


def read_input(day: int):
    with open(Path(__file__).parent / f"../inputs/{day:02}.txt", "r") as f:
        return f.read()


def read_example(day: int):
    with open(Path(__file__).parent / f"../examples/{day:02}.txt", "r") as f:
        return f.read()


def run(func: Callable, part: int, n: int = 1):
    start = time.perf_counter()
    for _ in range(n):
        out = func()
    end = time.perf_counter()

    print(f"Part {part} solution: ({format_time((end - start) / n)})")
    print(out)


def format_time(num: float):
    if num >= 1:
        return f"{num:.2f} s"
    elif num >= 1e-3:
        return f"{num*1e3:.2f} ms"
    elif num >= 1e-6:
        return f"{num*1e6:.2f} µs"
    else:
        return f"{num*1e9:.2f} ns"
