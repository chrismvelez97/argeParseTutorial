import argparse

parser = argparse.ArgumentParser()

# Adds the argument
parser.add_argument("--verbosity", help = "increase output verbosity")

# Instead of printing result of parsed args, saves into a variable
args = parser.parse_args()

# Checks to see if variable matches args verbosity method
if args.verbosity:
    print("Verbosity turned on")

# If you run without ANY commands it actually will still run, it just won't
# return anything, which goes to show the argument is actually optional
