test_str = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def part_one(inp: str) -> int:
    horizontal = depth = 0
    for line in inp.splitlines():
        command, a = line.split()
        x = int(a)
        if command == "forward":
            horizontal += x
        elif command == "down":
            depth += x
        else:
            depth -= x
    return horizontal * depth


def part_two(inp: str) -> int:
    horizontal = depth = aim = 0
    for line in inp.splitlines():
        command, a = line.split()
        x = int(a)
        if command == "down":
            aim += x
        elif command == "up":
            aim -= x
        else:
            horizontal += x
            depth += aim * x
    return horizontal * depth


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
