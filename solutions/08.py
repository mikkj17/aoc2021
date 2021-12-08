import utils

test = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\
"""


def _1(inp: str) -> int:
    lines = [line.split(' | ') for line in inp.splitlines()]
    return sum(len(digits) in {2, 3, 4, 7} 
               for _, output in lines for digits in output.split()
              )


def _2(inp: str) -> int:
    lines = [line.split(' | ') for line in inp.splitlines()]
    values = []
    for input_, output in lines:
        signals = [set(signal) for signal in sorted(input_.split(), key=len)]
        one = signals[0]
        seven = signals[1]
        four = signals[2]
        eight = signals[-1]
        two_three_five = list(filter(lambda s: len(s) == 5, signals))
        zero_six_nine = list(filter(lambda s: len(s) == 6, signals))
        three, = list(filter(lambda s: one <= s, two_three_five))
        two_five = list(filter(lambda s: s != three, two_three_five))
        bot = three - four - seven
        mid = three - seven - bot
        zero = eight - mid
        six_nine = list(filter(lambda s: s != zero, zero_six_nine))
        nine, = list(filter(lambda s: one <= s, six_nine))
        six, = list(filter(lambda s: s != nine, six_nine))
        top_right = one - six
        two, = list(filter(lambda s: top_right <= s, two_five))
        five, = list(filter(lambda s: s != two, two_five))
        
        mapping = {
            ''.join(sorted(zero)): '0',
            ''.join(sorted(one)): '1',
            ''.join(sorted(two)): '2',
            ''.join(sorted(three)): '3',
            ''.join(sorted(four)): '4',
            ''.join(sorted(five)): '5',
            ''.join(sorted(six)): '6',
            ''.join(sorted(seven)): '7',
            ''.join(sorted(eight)): '8',
            ''.join(sorted(nine)): '9'
        }
        value = ''.join(mapping[''.join(sorted(out))] for out in output.split())
        values.append(value)

    return sum(map(int, values))


if __name__ == '__main__':
    print(utils.runner([_1, _2], [test]))

