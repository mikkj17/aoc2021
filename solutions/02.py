import utils

test = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def _1(inp: str) -> int:
    horizontal = depth = 0
    for line in inp.splitlines():
        command, x = line.split()
        x = int(x)
        if command == 'forward':
            horizontal += x
        elif command == 'down':
            depth += x
        else:
            depth -= x
    return horizontal * depth


def _2(inp: str) -> int:
    horizontal = depth = aim = 0
    for line in inp.splitlines():
        command, x = line.split()
        x = int(x)
        if command == 'down':
            aim += x
        elif command == 'up':
            aim -= x
        else:
            horizontal += x
            depth += aim * x
    return horizontal * depth


if __name__ == '__main__':
    print(utils.main([_1, _2], [test]))

