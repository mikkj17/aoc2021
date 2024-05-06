from tqdm import tqdm

test_str = """\
16,1,2,0,4,2,7,1,2,14\
"""


def part_one(inp: str) -> int:
    positions = list(map(int, inp.split(",")))
    return min(
        sum(abs(crab - position) for crab in positions)
        for position in range(min(positions), max(positions) + 1)
    )


def part_two(inp: str) -> int:
    positions = list(map(int, inp.split(",")))
    return min(
        sum(sum(range(1, abs(crab - position) + 1)) for crab in positions)
        for position in tqdm(range(min(positions), max(positions) + 1))
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
