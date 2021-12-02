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


def _1(inp: str):
    lines = [int(x) for x in inp.splitlines()]
    count = 0
    for idx, current in enumerate(lines[:-1]):
        next = lines[idx+1]
        if next > current:
            count += 1

    return count


def _2(inp: str):
    lines = [int(x) for x in inp.splitlines()]
    count = 0
    for idx, current in enumerate(lines[:-3]):
        next = lines[idx+3]
        if next > current:
            count += 1

    return count


if __name__ == '__main__':
    print(utils.main([_1, _2], [test]))

