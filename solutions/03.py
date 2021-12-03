import utils
from typing import List

test = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def most_freq(lines: List[str], idx: int) -> str:
    freqs = {'1': 0, '0': 0}
    for line in lines:
        freqs[line[idx]] += 1
    return max(freqs.items(), key=lambda f: f[1])[0]


def _1(inp: str) -> int:
    gamma = ''
    epsilon = ''
    lines = inp.splitlines()
    for i in range(len(lines[0])):
        mst_freq = most_freq(lines, i)
        gamma += mst_freq
        epsilon += str(1 - int(mst_freq))
    return int(gamma, 2) * int(epsilon, 2)


def _2(inp: str) -> int:
    lines = inp.splitlines()
    return int(func(lines, 0, True), 2) * int(func(lines, 0, False), 2)


def func(considered: List[str], idx: int, most_common: bool) -> str:
    mst_freq = most_freq(considered, idx)
    good_bit = mst_freq if most_common else str(1 - int(mst_freq))
    remaining = [line for line in considered if line[idx] == good_bit]
    return remaining[0] if len(remaining) == 1 else func(remaining, idx+1, most_common)


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

