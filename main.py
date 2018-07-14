#!/usr/bin/python3

import NodeGraph
from NodeGraph import dist
import random as rng


def build_nodes(num_nodes=3, max_weight=3):
    ''' Build a random node graph '''
    nodes = []
    for i in range(0, num_nodes):
        xy = (rng.randint(-10, 10), rng.randint(-10, 10))
        nodes.append(NodeGraph.Node(xy, rng.randint(1, max_weight)))
    
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
    ''' NodeGraph.Graph.find_neighbors unit test '''
    ng = NodeGraph.Graph(build_nodes(10, 8))
    for this_node in ng.nodes:
        edges = this_node.find_neighbors(ng)
        neighbor_count = len(this_node.neighbors)

        print("{0} has {1} neighbors:".format(
            str(this_node)[25:-1], neighbor_count)
        )

        for edge in edges:
            print("\t:{0}, {1} units away".format(
                str(edge[0])[25:-1], str(edge[1]))
            )

if __name__ == '__main__':
    test_find_neighbors()