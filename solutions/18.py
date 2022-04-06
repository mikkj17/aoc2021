from __future__ import annotations

import math
from copy import deepcopy
from functools import reduce

import utils


test = """\
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]\
"""
small_test = """\
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]\
"""


def explode(snailfish_number: str):
    print('explode called...')
    nested_level = -1
    sn = list(snailfish_number)
    for i, char in enumerate(sn):
        if char == '[':
            nested_level += 1
        elif char == ']':
            nested_level -= 1

        if nested_level == 4 and char == '[':
            left_start = i + 1
            next_comma = sn[left_start:].index(',')
            left_end = left_start + next_comma

            right_start = left_end + 1
            next_end_bracket = sn[right_start:].index(']')
            right_end = right_start + next_end_bracket
            left = int(snailfish_number[left_start:left_end])
            right = int(snailfish_number[right_start:right_end])
            pair = left, right
            break
    else:
        return snailfish_number, False

    print('exploding', pair)

    for j in range(i, 0, -1):
        if sn[j].isdigit():
            start_range = j
            while sn[start_range].isdigit():
                start_range -= 1
            left_num = int(snailfish_number[start_range + 1:j + 1])
            print(f'adding left side of pair ({left}) to', left_num)
            for k in range(start_range + 1, j + 1):
                sn[k] = ''
            sn[j] = str(left_num + int(left))
            break

    for j in range(right_end + 1, len(sn)):
        if sn[j].isdigit():
            end_range = j
            while sn[end_range].isdigit():
                end_range += 1
            right_num = int(snailfish_number[j:end_range])
            print(f'adding right side of pair ({right}) to', right_num)
            for k in range(j, end_range):
                sn[k] = ''
            sn[j] = str(right_num + int(right))
            break

    sn = sn[:left_start - 1] + ['0'] + sn[right_end + 1:]

    return ''.join(sn), True


def split(snailfish_number: str):
    print('split called...')
    sn = list(snailfish_number)
    large_number = None
    for i, char in enumerate(sn[:-1]):
        if char.isdigit() and sn[i+1].isdigit():
            large_number = int(char + sn[i+1])
            break
    else:
        return snailfish_number, False

    print('splitting', large_number)
    left = math.floor(large_number/2)
    right = math.ceil(large_number/2)
    sn = sn[:i] + ['[', str(left), ',', str(right), ']'] + sn[i+2:]

    return ''.join(sn), True


def reduction(sn1: str, sn2: str) -> str:
    sn = f'[{sn1},{sn2}]'
    while True:
        print(sn)
        sn, nested_pair = explode(sn)
        if not nested_pair:
            sn, large_number = split(sn)
            if not large_number:
                return sn


def magnitude(final_sum: list) -> int:
    left, right = final_sum
    if isinstance(left, list):
        return 3 * magnitude(left) + 2 * magnitude(right)
    return 3 * left + 2 * right


def _1(inp: str) -> int:
    snailfish_numbers = inp.splitlines()
    final_sum = reduce(reduction, snailfish_numbers)
    final_list = eval(final_sum)
    return magnitude(final_list)


def _2(inp: str) -> int:
    return 0


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

