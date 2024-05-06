import numpy as np

test_str = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7\
"""


def check_won(board, seen):
    for row in board:
        if set(row) <= seen:
            return True, list(row)
    for idx in range(board.shape[1]):
        col = board[:, idx]
        if set(col) <= seen:
            return True, list(col)
    return False, []


def part_one(inp: str) -> int:
    parts = inp.split("\n\n")
    nums = list(map(int, parts[0].split(",")))
    boards = parts[1:]

    int_boards = []
    for board in boards:
        int_boards.append([[int(x) for x in row.split()] for row in board.splitlines()])
    seen = set()
    for num in nums:
        seen.add(num)
        for board in int_boards:
            won, numbers = check_won(np.array(board), seen)
            if won:
                return sum(n for row in board for n in row if n not in seen) * num

    return 0


def part_two(inp: str) -> int:
    parts = inp.split("\n\n")
    nums = list(map(int, parts[0].split(",")))
    boards = parts[1:]

    int_boards = []
    for board in boards:
        int_boards.append([[int(x) for x in row.split()] for row in board.splitlines()])
    seen = set()
    wons = set()
    for num in nums:
        seen.add(num)
        for b_idx, board in enumerate(int_boards):
            won, numbers = check_won(np.array(board), seen)
            if won:
                wons.add(b_idx)
                if len(wons) == len(boards):
                    return sum(n for row in board for n in row if n not in seen) * num

    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
