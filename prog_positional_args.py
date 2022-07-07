import argparse

parser = argparse.ArgumentParser()

# Adds a positional argument that is required and gives string to explain
# what it does when using -h
parser.add_argument('echo', help = 'echo the string you use here')

args = parser.parse_args()

print(args.echo)
