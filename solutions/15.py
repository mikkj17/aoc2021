from collections import deque
from typing import Tuple, List, Dict

import utils

test = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581\
"""


def neighbours(node: Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = node
    ret = []
    for offset in (-1, 1):
        ret.append((x + offset, y))
        ret.append((x, y + offset))
    return ret


def search(risk_levels: Dict[Tuple[int, int], int], size: int) -> int:
    start = (0, 0)
    queue = deque([start])
    seen = {start}
    costs = {start: 0}
    while queue:
        node = queue.popleft()
        if node == (size - 1, size - 1):
            return costs[node]
        for neighbour in neighbours(node):
            if neighbour not in risk_levels:
                continue
            new_cost = costs[node] + risk_levels[neighbour]
            if neighbour in costs:
                costs[neighbour] = min(costs[neighbour], new_cost)
            else:
                costs[neighbour] = new_cost
            if neighbour not in seen and neighbour not in queue:
                queue.append(neighbour)
        seen.add(node)

    return 0


def _1(inp: str) -> int:
    lines = inp.splitlines()
    risk_levels = {
        (i, j): int(val)
        for i, row in enumerate(lines)
        for j, val in enumerate(row)
    }
    return search(risk_levels, len(lines))

    
def _2(inp: str) -> int:
    lines = inp.splitlines()
    risk_levels = {
        (i, j): int(val)
        for i, row in enumerate(lines)
        for j, val in enumerate(row)
    }
    offset = len(lines)
    start = 1
    end = 9
    for i, j in list(risk_levels):
        original_value = risk_levels[(i, j)]
        for i_mul in range(1, 5):
            for j_mul in range(1, 5):
                idx_i = i + offset * i_mul
                idx_j = j + offset * j_mul
                risk_levels[(i, idx_j)] = ((original_value + j_mul) - start) % (end - start + 1) + start
                risk_levels[(idx_i, j)] = ((original_value + i_mul) - start) % (end - start + 1) + start
                risk_levels[(idx_i, idx_j)] = ((original_value + i_mul + j_mul) - start) % (end - start + 1) + start

    return search(risk_levels, len(lines) * 5)


if __name__ == '__main__':
    with open('inputs/15.txt') as f:
        input_s = f.read()
    print(_2(input_s))
    exit()
    print(utils.runner([_1, _2], [test]))

