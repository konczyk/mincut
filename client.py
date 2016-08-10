#!/usr/bin/env python3

import argparse
import random
import sys
from graph import Graph
from mincut import MinCut

parser = argparse.ArgumentParser(description='MinCut client.')

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin,
                    help='Input file with graph data (default stdin)')

args = parser.parse_args()
graph = Graph(args.infile)

print(MinCut(graph).mincut())
