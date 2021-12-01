import sys

def load() -> str:
    day = sys.argv[0].split('.')[0]
    with open(f'../inputs/{day}.txt') as f:
        return f.read()

