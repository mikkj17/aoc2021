from collections import deque

test_str = """\
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


def neighbours(node: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = node
    ret = []
    for offset in (-1, 1):
        ret.append((x + offset, y))
        ret.append((x, y + offset))
    return ret


def search(risk_levels: dict[tuple[int, int], int], size: int) -> int:
    start = (0, 0)
    queue = deque([start])
    seen = set()
    costs = {start: 0}
    while queue:
        node = min(queue, key=lambda p: costs[(p[0], p[1])])
        queue.remove(node)
        seen.add(node)
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

    return 0


def part_one(inp: str) -> int:
    lines = inp.splitlines()
    risk_levels = {
        (i, j): int(val) for i, row in enumerate(lines) for j, val in enumerate(row)
    }
    return search(risk_levels, len(lines))


def part_two(inp: str) -> int:
    lines = inp.splitlines()
    risk_levels = {
        (i, j): int(val) for i, row in enumerate(lines) for j, val in enumerate(row)
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
                risk_levels[(i, idx_j)] = ((original_value + j_mul) - start) % (
                    end - start + 1
                ) + start
                risk_levels[(idx_i, j)] = ((original_value + i_mul) - start) % (
                    end - start + 1
                ) + start
                risk_levels[(idx_i, idx_j)] = (
                    (original_value + i_mul + j_mul) - start
                ) % (end - start + 1) + start

    return search(risk_levels, len(lines) * 5)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
