import argparse

parser = argparse.ArgumentParser()

# Without adding the type the math wont function because the parser
# will give back a string
parser.add_argument(
    'square',
    help = 'Display the square of a given number',
    type = int
)

args = parser.parse_args()

print(args.square**2)
