import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'hours_passed',
    help='number of hours passed',
    type=float
)
parser.add_argument(
    '-f',
    '--funny-face',
    help='Enter a funny face',
    type=str,
)

args = parser.parse_args()
print(args.hours_passed)
print(args.funny_face)