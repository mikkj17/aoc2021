from collections import defaultdict, Counter
from pprint import pprint
from tqdm import tqdm
from typing import Dict, Tuple

import utils

test = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C\
"""


def _1(inp: str) -> int:
    state, pair_insertion = inp.split('\n\n')
    rules = {}
    for line in pair_insertion.splitlines():
        pair, insertion = line.split(' -> ')
        rules[pair] = insertion

    for step in range(10):
        new_state = ''
        for p1, p2 in zip(state[:-1], state[1:]):
            new_state += p1
            new_state += rules[p1+p2]
        new_state += p2
        state = new_state

    freq = Counter(state)
    return freq.most_common()[0][1] - freq.most_common()[-1][1]


def _2(inp: str) -> int:
    state, pair_insertion = inp.split('\n\n')
    rules = {}
    for line in pair_insertion.splitlines():
        pair, insertion = line.split(' -> ')
        rules[tuple(pair)] = insertion

    pairs = Counter(zip(state[:-1], state[1:]))
    freq = Counter(state)

    for step in range(40):
        new_pairs = Counter()
        for pair, count in pairs.items():
            new_pairs[(pair[0], rules[pair])] += count
            new_pairs[(rules[pair], pair[1])] += count
            freq[rules[pair]] += count
        pairs = new_pairs

    return freq.most_common()[0][1] - freq.most_common()[-1][1]


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

