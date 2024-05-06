from collections import defaultdict

test_str = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end\
"""


class Graph:

    def __init__(self) -> None:
        self.paths: list[list[str]] = []

    def build_graph(self, inp: str) -> None:
        self.edges = defaultdict(list)
        for line in inp.splitlines():
            v1, v2 = line.split("-")
            self.edges[v1].append(v2)
            self.edges[v2].append(v1)

    def search(self, path: list[str]) -> None:
        cave = path[-1]
        for neighbour in self.edges[cave]:
            new_path = [*path, neighbour]
            if neighbour == "end":
                self.paths.append(new_path)
            elif neighbour.isupper() or neighbour not in path:
                self.search(new_path)

    @staticmethod
    def small(cave: str) -> bool:
        return cave.islower() and cave not in {"start", "end"}

    def check_visit(self, cave: str, path: list[str]) -> bool:
        if cave in {"start", "end"}:
            return False
        if (
            any(path.count(c) > 1 for c in self.edges.keys() if self.small(c))
            and cave in path
        ):
            return False
        return True

    def search2(self, path: list[str]) -> None:
        cave = path[-1]
        for neighbour in self.edges[cave]:
            new_path = [*path, neighbour]
            if neighbour == "end":
                self.paths.append(new_path)
            elif neighbour.isupper() or self.check_visit(neighbour, path):
                self.search2(new_path)


def part_one(inp: str) -> int:
    graph = Graph()
    graph.build_graph(inp)
    path = ["start"]
    graph.search(path)
    return len(graph.paths)


def part_two(inp: str) -> int:
    graph = Graph()
    graph.build_graph(inp)
    path = ["start"]
    graph.search2(path)
    return len(graph.paths)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
    print(part_one(input_str))
    print(part_two(input_str))
