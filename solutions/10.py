import utils

test = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]\
"""


def _1(inp: str) -> int:
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    illegal_chars = []
    for line in inp.splitlines():
        stack = []
        for c in line:
            if c in mapping:
                stack.append(c)
            else:
                open_char = stack.pop()
                if mapping[open_char] != c:
                    illegal_chars.append(c)
                    break
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return sum(map(lambda x: score_map[x], illegal_chars))


def _2(inp: str) -> int:
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    lines = inp.splitlines()
    corrupted_lines = []
    for line in lines:
        stack = []
        for c in line:
            if c in mapping:
                stack.append(c)
            else:
                open_char = stack.pop()
                if mapping[open_char] != c:
                    corrupted_lines.append(line)
                    break
 
    remaining_lines = list(set(lines) - set(corrupted_lines))
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in remaining_lines:
        stack = []
        for c in line:
            if c in mapping.keys():
                stack.append(c)
            else:
                open_char = stack.pop()
        remaining_chars = reversed(list(map(lambda c: mapping[c], stack)))
        total_score = 0
        for char in remaining_chars:
            total_score *= 5
            total_score += score_map[char]
        scores.append(total_score)

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

