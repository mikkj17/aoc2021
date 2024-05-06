test_str = """\
199
200
208
210
200
207
240
269
260
263"""


def part_one(inp: str) -> int:
    lines = [int(x) for x in inp.splitlines()]
    return sum(nxt > current for nxt, current in zip(lines[1:], lines))


def part_two(inp: str) -> int:
    lines = [int(x) for x in inp.splitlines()]
    return sum(nxt > current for nxt, current in zip(lines[3:], lines))


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
