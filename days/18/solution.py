import math
from functools import reduce
from itertools import permutations

test_str = """\
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

small_test_str = """\
[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]\
"""

another_test_str = """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]\
"""


def explode(snailfish_number: str) -> tuple[str, bool]:
    nested_level = -1
    sn = list(snailfish_number)
    for i, char in enumerate(sn):
        if char == "[":
            nested_level += 1
        elif char == "]":
            nested_level -= 1

        if nested_level == 4 and char == "[":
            left_start = i + 1
            next_comma = sn[left_start:].index(",")
            left_end = left_start + next_comma

            right_start = left_end + 1
            next_end_bracket = sn[right_start:].index("]")
            right_end = right_start + next_end_bracket
            left = int(snailfish_number[left_start:left_end])
            right = int(snailfish_number[right_start:right_end])
            break
    else:
        return snailfish_number, False

    for j in range(i, 0, -1):
        if sn[j].isdigit():
            start_range = j
            while sn[start_range].isdigit():
                start_range -= 1
            left_num = int(snailfish_number[start_range + 1 : j + 1])
            for k in range(start_range + 1, j + 1):
                sn[k] = ""
            sn[j] = str(left_num + int(left))
            break

    for j in range(right_end + 1, len(sn)):
        if sn[j].isdigit():
            end_range = j
            while sn[end_range].isdigit():
                end_range += 1
            right_num = int(snailfish_number[j:end_range])
            for k in range(j, end_range):
                sn[k] = ""
            sn[j] = str(right_num + int(right))
            break

    sn = sn[: left_start - 1] + ["0"] + sn[right_end + 1 :]

    return "".join(sn), True


def split(snailfish_number: str) -> tuple[str, bool]:
    sn = list(snailfish_number)
    for i, char in enumerate(sn[:-1]):
        if char.isdigit() and sn[i + 1].isdigit():
            large_number = int(char + sn[i + 1])
            break
    else:
        return snailfish_number, False

    left = math.floor(large_number / 2)
    right = math.ceil(large_number / 2)
    sn = sn[:i] + ["[", str(left), ",", str(right), "]"] + sn[i + 2 :]

    return "".join(sn), True


def reduction(sn1: str, sn2: str) -> str:
    sn = f"[{sn1},{sn2}]"
    while True:
        sn, nested_pair = explode(sn)
        if not nested_pair:
            sn, large_number = split(sn)
            if not large_number:
                return sn


def magnitude(final_sum: list) -> int:
    ret = 0
    left, right = final_sum
    if isinstance(left, list):
        ret += 3 * magnitude(left)
    else:
        ret += 3 * left

    if isinstance(right, list):
        ret += 2 * magnitude(right)
    else:
        ret += 2 * right

    return ret


def part_one(inp: str) -> int:
    return magnitude(eval(reduce(reduction, inp.splitlines())))


def part_two(inp: str) -> int:
    return max(
        magnitude(eval(reduce(reduction, sn)))
        for sn in permutations(inp.splitlines(), 2)
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
