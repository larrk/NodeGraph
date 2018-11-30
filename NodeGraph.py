''' NodeGraph.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 12th, 2018
'''

from math import sqrt
from operator import itemgetter
from random import randint


def dist(xy1, xy2):
    ''' Return the distance between a pair of xy coordinates '''
    return sqrt(abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1]))


class Graph(object):
    def __init__(self, nodes=[], count=10, weightiness=3, find_neighbors=True):

        if nodes == []:
            for _ in range(0, count):
                xy = (randint(-10, 10), randint(-10, 10))
                nodes.append(Node(xy, randint(1, weightiness)))

            self.nodes = nodes
        else:
            self.nodes = nodes

        def find_all_neighbors(self):
            for node in self.nodes:
                node.find_neighbors(self)

        if find_neighbors is True: self.find_all_neighbors()

    def find_all_neighbors(self):
        for node in self.nodes:
            node.find_neighbors(self)

    def batch(self, glPointSize=4, glLineWidth=2):
        batch = pyg.graphics.Batch()
        pyg.gl.glPointSize


class Node(object):
    def __init__(self, xy=(0, 0), weight=3):
        # Position data.
        self.xy = xy
        # Weight defines the maximum number of neighbors this node can have.
        self.weight = weight
        # References to this node's neighbors sorted by distance.
        self.neighbors = {}

    def find_neighbors(self, graph):
        ''' Find this node's closest neighbors in the specified graph '''
        neighbors = []

        # for each node in the graph
        for other_node in graph.nodes:
            # other than the focus
            if other_node != self:
                # calculate the distance of an edge between the focus
                # and the other node
                neighbors.append((other_node, dist(self.xy, other_node.xy)))

        # sort edge lengths
        neighbors = sorted(neighbors, key=lambda node: node[1])

        # prune neighbors this node cannot support
        # starting with the furthest
        while len(neighbors) > self.weight:
            neighbors.pop()

        self.neighbors = neighbors
        return neighbors
