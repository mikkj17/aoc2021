from functools import reduce

test_str = """\
2199943210
3987894921
9856789892
8767896789
9899965678\
"""


def low_point(i: int, j: int, height: int, matrix: list[list[int]]) -> bool:
    for offset in [-1, 1]:
        try:
            if height >= matrix[i + offset][j]:
                return False
        except IndexError:
            pass
        try:
            if height >= matrix[i][j + offset]:
                return False
        except IndexError:
            pass
    return True


def part_one(inp: str) -> int:
    matrix = [[int(x) for x in row] for row in inp.splitlines()]
    risk_levels = []
    for i, row in enumerate(matrix):
        for j, height in enumerate(row):
            if low_point(i, j, height, matrix):
                risk_levels.append(1 + height)

    return sum(risk_levels)


def flow(
    i: int,
    j: int,
    height: int,
    matrix: list[list[int]],
    points: set[tuple[int, int, int]],
) -> None:
    points.add((i, j, height))

    for offset in [-1, 1]:
        idx_i = i + offset
        idx_j = j + offset

        if 0 <= idx_i < len(matrix) and 0 <= j < len(matrix[0]):
            entry = matrix[idx_i][j]
            if entry != 9:
                if height < entry:
                    flow(idx_i, j, entry, matrix, points)

        if 0 <= i < len(matrix) and 0 <= idx_j < len(matrix[0]):
            entry = matrix[i][idx_j]
            if entry != 9:
                if height < entry:
                    flow(i, idx_j, entry, matrix, points)


def part_two(inp: str) -> int:
    matrix = [[int(x) for x in row] for row in inp.splitlines()]
    low_points = []
    for i, row in enumerate(matrix):
        for j, height in enumerate(row):
            if low_point(i, j, height, matrix):
                low_points.append((i, j, height))

    basins = []
    for i, j, height in low_points:
        basin = set()
        flow(i, j, height, matrix, basin)
        basins.append(basin)

    top_three = [len(x) for x in sorted(basins, key=len, reverse=True)[:3]]
    return reduce(lambda a, b: a * b, top_three)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
