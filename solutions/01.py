import utils

test = """\
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


def _1(inp: str) -> int:
    lines = [int(x) for x in inp.splitlines()]
    return sum(nxt > current for nxt, current in zip(lines[1:], lines))


def _2(inp: str) -> int:
    lines = [int(x) for x in inp.splitlines()]
    return sum(nxt > current for nxt, current in zip(lines[3:], lines))


if __name__ == '__main__':
    print(utils.main([_1, _2], [test]))

