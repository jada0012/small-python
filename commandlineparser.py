import argparse

parser = argparse.ArgumentParser(description="testing the limits of this formidable module!!")
parser.add_argument("--verbosity", "-v", help="increase verbosity", action="store_true")
parser.add_argument("square", type=int, help="displays value of number")
args = parser.parse_args()
answer = args.square**2

if args.verbosity:
    print(f"the square of {args.square} is equal to {answer}")
else:
    print(answer)
