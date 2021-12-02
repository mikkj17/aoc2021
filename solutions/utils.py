import argparse
import os
import requests
import sys
from dotenv import load_dotenv
from typing import Callable, List


def download_input(day: int, path: str) -> None:
    load_dotenv()
    url = f'https://adventofcode.com/2021/day/{day}/input'
    session = os.getenv('SESSION')
    print('downloading personal input from', url)
    response = requests.get(url, cookies={'session': session})
    with open(path, 'w') as f:
        f.write(response.text)


def load() -> str:
    day = sys.argv[0].split('.')[0]
    path = f'../inputs/{day}.txt'
    if not os.path.exists(path):
        download_input(int(day), path)
    with open(path) as f:
        return f.read()


def main(funcs: List[Callable[[str], int]], test_inputs: List[str]) -> List[List[int]]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--test',
        action='store_true',
        help='whether to run on test input or my personal input'
    )
    parser.add_argument(
        '-p', '--parts',
        nargs='+',
        type=int,
        help='which parts of the problem to solve (1, 2 or both)'
    )
    args = parser.parse_args()

    if args.test:
        inputs = test_inputs
    else:
        inputs = [load()]
    
    run_funcs = [funcs[part-1] for part in args.parts]
    return [[func(inp) for inp in inputs] for func in run_funcs]

