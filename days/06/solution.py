test_str = """\
3,4,3,1,2\
"""


def part_one(inp: str) -> int:
    state = list(map(int, inp.split(",")))
    for _ in range(80):
        for i in range(len(state)):
            fish = state[i]
            if fish == 0:
                state.append(8)
                state[i] = 6
            else:
                state[i] -= 1

    return len(state)


def part_two(inp: str) -> int:
    counter = [0] * 9
    for fish in list(map(int, inp.split(","))):
        counter[fish] += 1

    for _ in range(256):
        zero_days = counter[0]
        for i in range(8):
            counter[i] = counter[i + 1]
        counter[6] += zero_days
        counter[8] = zero_days

    return sum(counter)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
