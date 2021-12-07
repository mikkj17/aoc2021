from tqdm import tqdm

import utils

test = """\
16,1,2,0,4,2,7,1,2,14\
"""


def _1(inp: str) -> int:
    positions = list(map(int, inp.split(',')))
    return min(
        sum(abs(crab - position) for crab in positions)
        for position in range(min(positions), max(positions) + 1)
    )


def _2(inp: str) -> int:
    positions = list(map(int, inp.split(',')))
    return min(
        sum(sum(range(1, abs(crab - position) + 1)) for crab in positions)
        for position in tqdm(range(min(positions), max(positions) + 1))
    )


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

