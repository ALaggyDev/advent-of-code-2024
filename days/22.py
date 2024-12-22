from collections import Counter
import aoc

day = 22
aoc_input = aoc.read_input(day)
aoc_example = aoc.read_example(day)

# ----------


def gen_next_secret(secret: int):
    secret = (secret ^ (secret << 6)) & 0xffffff
    secret = (secret ^ (secret >> 5)) & 0xffffff
    secret = (secret ^ (secret << 11)) & 0xffffff

    return secret


def part_1(input: str):
    d = 0
    for line in input.splitlines():
        secret = int(line)

        for _ in range(2000):
            secret = gen_next_secret(secret)

        d += secret

    return d


def part_2(input: str):
    counter = Counter()

    for line in input.splitlines():
        secret = int(line)

        prices = [secret % 10]
        for _ in range(2000):
            secret = gen_next_secret(secret)
            prices.append(secret % 10)

        changes = [b-a for (a, b) in zip(prices, prices[1:])]

        memos = dict()
        for i in range(len(changes) - 3):
            window = tuple(changes[i:i+4])
            if window not in memos:
                memos[window] = prices[i+4]

        counter += memos

    return max(counter.values())


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
