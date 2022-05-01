import argparse

parser = argparse.ArgumentParser()
parser.add_argument("c1", metavar="c1", type=float, help="Concentration 1")
parser.add_argument("c2", metavar="c2", type=float, help="Concentration 2")
parser.add_argument("v1", metavar="v1", type=float, help="Volume 1")
parser.add_argument("v2", metavar="v2", type=float, help="Volume 2")
args = parser.parse_args()

c1 = args.c1

print(c1)

