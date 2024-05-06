import re

test_str = "target area: x=20..30, y=-10..-5"


def step(pos: tuple[int, int], velocity: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    x_vel, y_vel = velocity

    x += x_vel
    y += y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    y_vel -= 1

    return [(x, y), (x_vel, y_vel)]


def fire(initial_vel: tuple[int, int], limits: list[int]) -> tuple[bool, int]:
    low_x, high_x, low_y, high_y = limits
    pos = (0, 0)
    vel = initial_vel
    initial_x, _ = initial_vel
    y_positions = []
    while True:
        pos, vel = step(pos, vel)
        x, y = pos
        y_positions.append(y)
        if low_x <= x <= high_x and low_y <= y <= high_y:
            return True, max(y_positions)
        if y < low_y:
            return False, 0
        if initial_x < 0:
            if x < low_x:
                return False, 0
        elif initial_x > 0:
            if x > high_x:
                return False, 0


def part_one(inp: str) -> int:
    nums = re.match(
        r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", inp
    ).groups()
    limits = [int(x) for x in nums]
    return max(
        (fire((x, y), limits) for x in range(100) for y in range(100)),
        key=lambda x: x[1],
    )[1]


def part_two(inp: str) -> int:
    nums = re.match(
        r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", inp
    ).groups()
    limits = [int(x) for x in nums]
    attempts = [
        ((x, y), fire((x, y), limits))
        for x in range(-1000, 1000)
        for y in range(-1000, 1000)
    ]
    return len([(vel, height) for vel, (success, height) in attempts if success])


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
