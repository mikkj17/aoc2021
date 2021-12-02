import utils

test = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def _1(inp: str):
    horizontal = depth = 0
    for line in inp.splitlines():
        p, x = line.split()
        x = int(x)
        if p == 'forward':
            horizontal += x
        elif p == 'down':
            depth += x
        else:
            depth -= x
    return horizontal * depth


def _2(inp: str):
    horizontal = depth = aim = 0
    for line in inp.splitlines():
        p, x = line.split()
        x = int(x)
        if p == 'forward':
            horizontal += x
            depth += aim * x
        elif p == 'down':
            aim += x
        else:
            aim -= x
    return horizontal * depth


if __name__ == '__main__':
    print(utils.main([_1, _2], [test]))

