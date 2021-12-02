import utils

test = """\
"""


def _1(inp: str) -> int:
    return 0


def _2(inp: str) -> int:
    return 0


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

