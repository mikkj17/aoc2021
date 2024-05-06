import re
from collections import defaultdict

test_str = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
"""


def parse(inp: str) -> list[tuple[int, int, int, int]]:
    regex = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")
    return [tuple(map(int, regex.match(line).groups())) for line in inp.splitlines()]


def get_points(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    ret = [(x1, y1)]
    if abs(x1 - x2) == abs(y1 - y2):

        if x1 == y1 and x2 == y2:
            while x1 < x2:
                x1 += 1
                y1 += 1
                ret.append((x1, y1))
            while x1 > x2:
                x1 -= 1
                y1 -= 1
                ret.append((x1, y1))
            return ret

        elif x1 == y2 and y1 == x2:
            while x1 < x2:
                x1 += 1
                y1 -= 1
                ret.append((x1, y1))
            while x1 > x2:
                x1 -= 1
                y1 += 1
                ret.append((x1, y1))
            return ret

        elif x1 < x2 and y1 > y2 or x1 > x2 and y1 < y2:
            while x1 < x2 and y1 > y2:
                x1 += 1
                y1 -= 1
                ret.append((x1, y1))
            while x1 > x2 and y1 < y2:
                x1 -= 1
                y1 += 1
                ret.append((x1, y1))
            return ret
        elif x1 < x2 and y1 < y2 or x1 > x2 and y1 > y2:
            while x1 < x2 and y1 < y2:
                x1 += 1
                y1 += 1
                ret.append((x1, y1))
            while x1 > x2 and y1 > y2:
                x1 -= 1
                y1 -= 1
                ret.append((x1, y1))
            return ret

    elif x1 == x2:
        while y1 < y2:
            y1 += 1
            ret.append((x1, y1))
        while y1 > y2:
            y1 -= 1
            ret.append((x1, y1))
        return ret
    else:
        while x1 < x2:
            x1 += 1
            ret.append((x1, y1))
        while x1 > x2:
            x1 -= 1
            ret.append((x1, y1))
        return ret


def part_one(inp: str) -> int:
    lines = parse(inp)
    diagram = defaultdict(int)
    considered = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
    for line in considered:
        all_points = get_points(*line)
        for point in all_points:
            diagram[point] += 1

    count = 0
    for counter in diagram.values():
        if counter >= 2:
            count += 1
    return count


def part_two(inp: str) -> int:
    lines = parse(inp)
    diagram = defaultdict(int)
    for line in lines:
        all_points = get_points(*line)
        for point in all_points:
            diagram[point] += 1

    count = 0
    for counter in diagram.values():
        if counter >= 2:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
