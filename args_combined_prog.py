'''
Up until recently, we hav been executing one command
with one option at a time.  This section will cover
how to design a program that can take a positional arg
and an optional
'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '-v',
    '--verbose',
    help = 'Helps to increase verbosity',
    action = 'store_true'
)

parser.add_argument(
    'square',
    type = int,
    help = 'Display a square of a given number'
)

args = parser.parse_args()

answer = args.square**2

if args.verbose:
    print(f'the square of {args.square} equals {answer}')
else:
    print(answer)

#Something else to note is that the order of the args dont matter
