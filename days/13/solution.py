import re

test_str = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5\
"""


def print_state(state: set[tuple[int, int]], size_x: int, size_y: int) -> None:
    for i in range(size_y + 1):
        for j in range(size_x + 1):
            print("#" if (j, i) in state else ".", end=" ")
        print()


def part_one(inp: str) -> int:
    p1, p2 = inp.split("\n\n")
    dots = set()
    size_x = size_y = 0
    for line in p1.splitlines():
        x, y = line.split(",")
        if int(x) > size_x:
            size_x = int(x)
        if int(y) > size_y:
            size_y = int(y)
        dots.add((int(x), int(y)))

    folds = []
    for line in p2.splitlines():
        axis, amount = re.match(r"^fold along (x|y)=(\d+)", line).groups()
        folds.append((axis, int(amount)))

    for idx, (axis, amount) in enumerate(folds[:1]):
        new_state = set()
        if axis == "x":
            for x, y in dots:
                if x > amount:
                    x_pos = x - 2 * (x - amount)
                    new_state.add((x_pos, y))
                else:
                    new_state.add((x, y))
            size_x = amount - 1
        else:
            for x, y in dots:
                if y > amount:
                    y_pos = y - 2 * (y - amount)
                    new_state.add((x, y_pos))
                else:
                    new_state.add((x, y))
            size_y = amount - 1
        dots = new_state
    return len(dots)


def part_two(inp: str) -> int:
    p1, p2 = inp.split("\n\n")
    dots = set()
    size_x = size_y = 0
    for line in p1.splitlines():
        x, y = line.split(",")
        if int(x) > size_x:
            size_x = int(x)
        if int(y) > size_y:
            size_y = int(y)
        dots.add((int(x), int(y)))

    folds = []
    for line in p2.splitlines():
        axis, amount = re.match(r"^fold along (x|y)=(\d+)", line).groups()
        folds.append((axis, int(amount)))

    for idx, (axis, amount) in enumerate(folds):
        new_state = set()
        if axis == "x":
            for x, y in dots:
                if x > amount:
                    x_pos = x - 2 * (x - amount)
                    new_state.add((x_pos, y))
                else:
                    new_state.add((x, y))
            size_x = amount - 1
        else:
            for x, y in dots:
                if y > amount:
                    y_pos = y - 2 * (y - amount)
                    new_state.add((x, y_pos))
                else:
                    new_state.add((x, y))
            size_y = amount - 1
        dots = new_state
    print_state(dots, size_x, size_y)
    return len(dots)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
