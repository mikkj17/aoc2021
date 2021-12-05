import re
from collections import defaultdict
from pprint import pprint
from typing import List, Tuple

import utils

test = """\
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


def parse(inp: str) -> List[Tuple[int, int, int, int]]:
    regex = re.compile(r'^(\d+),(\d+) -> (\d+),(\d+)$')
    return [tuple(map(int, regex.match(line).groups())) for line in inp.splitlines()]


def print_diagram(diagram: List[Tuple[int, int]]) -> None:
    for i in range(10):
        for j in range(10):
            print(diagram[(j, i)], end=' ')
        print()
 

def get_points(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
    ret = [(x1, y1)]
    if abs(x1 - x2) == abs(y1 - y2):

        if x1 == y1 and x2 == y2 :
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


def _1(inp: str) -> int:
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


def _2(inp: str) -> int:
    lines = parse(inp)
    diagram = defaultdict(int)
    for line in lines:
        all_points = get_points(*line)
        for point in all_points:
            diagram[point] += 1

    print_diagram(diagram)

    count = 0
    for counter in diagram.values():
        if counter >= 2:
            count += 1
    return count


if __name__ == '__main__':
    print(get_points(6, 4, 2, 0))
    print(utils.runner([_1, _2], [test]))

