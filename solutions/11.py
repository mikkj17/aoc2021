from typing import List
import utils

test = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526\
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Octopus:

    def __init__(self, i: int, j: int, energy: int):
        self.i = i
        self.j = j
        self.energy = energy
        self.flashed = False

    def __repr__(self):
        return f'{self.i=}, {self.j=}, {self.energy=}, {self.flashed=}'


class Grid:
    def __init__(self, grid: List[List[Octopus]]) -> None:
        self.grid = grid
        self.flash_count = 0

    def print(self) -> None:
        for row in self.grid:
            for octopus in row:
                color = bcolors.OKBLUE if octopus.energy == 0 else ''
                print(f'{color}{octopus.energy}{bcolors.ENDC}', end=' ')
            print()

    def increase_energy(self) -> None:
        for row in self.grid:
            for octopus in row:
                octopus.energy += 1

    def flash(self) -> None:
        for row in self.grid:
            for octopus in row:
                if octopus.energy > 9:
                    if not octopus.flashed:
                        flash(octopus, self)

    def reset(self) -> None:
        for row in self.grid:
            for octopus in row:
                if octopus.flashed:
                    octopus.energy = 0
                    octopus.flashed = False

    def step(self) -> None:
        self.increase_energy()
        self.flash()
        self.reset()


def flash(octopus: Octopus, grid: Grid) -> None:
    octopus.flashed = True
    grid.flash_count += 1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            idx_i = octopus.i + i
            idx_j = octopus.j + j
            if 0 <= idx_i < len(grid.grid) and 0 <= idx_j < len(grid.grid[0]):
                adj_octo = grid.grid[idx_i][idx_j]
                if not adj_octo.flashed:
                    adj_octo.energy += 1
                    if adj_octo.energy > 9:
                        flash(adj_octo, grid)


def _1(inp: str) -> int:
    octopuses = [
        [Octopus(i, j, int(x)) for j, x in enumerate(row)]
        for i, row in enumerate(inp.splitlines())
    ]
    grid = Grid(octopuses)
    for step in range(100):
        grid.step()
    return grid.flash_count


def _2(inp: str) -> int:
    octopuses = [
        [Octopus(i, j, int(x)) for j, x in enumerate(row)]
        for i, row in enumerate(inp.splitlines())
    ]
    grid = Grid(octopuses)
    step_count = 0
    while True:
        grid.step()
        step_count += 1
        if sum(octopus.energy for row in grid.grid for octopus in row) == 0:
            return step_count


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

