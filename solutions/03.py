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


def _1(inp: str) -> int:
    g = ''
    e = ''
    lines = inp.splitlines()
    size = len(lines[0])
    for i in range(size):
        zeros = 0
        ones = 0
        for line in lines:
            bit = line[i]
            if bit == '0':
                zeros += 1
            else:
                ones += 1
        if zeros >= ones:
            g += '0'
            e += '1'
        else:
            g += '1'
            e += '0'
    return int(g, 2) * int(e, 2)

def ox(considered: List[str], idx: int) -> str:
    zeros = 0
    ones = 0
    for line in considered:
        bit = line[idx]
        if bit == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        mst = '1'
    else:
        mst = '0'

    considered = [line for line in considered if line[idx] == mst]
    if len(considered) == 1:
        return considered[0]
    else:
        return ox(considered, idx+1)

def co(considered: List[str], idx: int) -> str:
    zeros = 0
    ones = 0
    for line in considered:
        bit = line[idx]
        if bit == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        lst = '0'
    else:
        lst = '1'

    considered = [line for line in considered if line[idx] == lst]
    if len(considered) == 1:
        return considered[0]
    else:
        return co(considered, idx+1)


def _2(inp: str) -> int:
    oxy = ox(inp.splitlines(), 0)  
    co2 = co(inp.splitlines(), 0)
    return int(oxy, 2) * int(co2, 2)


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

