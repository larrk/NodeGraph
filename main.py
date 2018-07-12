#!/usr/bin/python3

import NodeGraph
from NodeGraph import dist
import random as rng


def build_nodes(n=3):
    nodes = []
    for i in range(0, n):
        xy = (rng.randint(-10, 10), rng.randint(-10, 10))
        nodes.append(NodeGraph.Node(xy))
    
    return nodes


def test_dist():
    ''' NodeGraph.dist unit test '''
    coordinates2d = []
    for i in range(1, 10):
        coordinates2d.append((rng.randint(-10, 10), rng.randint(-10, 10)))

    for this_coordinate in coordinates2d:
        for other_coordinate in coordinates2d:
            print(this_coordinate, other_coordinate, dist(this_coordinate, other_coordinate))

def test_find_neighbors():
    ng = NodeGraph.Graph(build_nodes())
    for k in ng.nodes.keys():
        ng.find_neighbors(k)


if __name__ == '__main__':
    test_find_neighbors()