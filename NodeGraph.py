''' NodeGraph.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 12th, 2018
'''

#import pyglet
from math import sqrt
from operator import itemgetter

def dist(xy1, xy2):
    ''' Return the distance between a pair of xy coordinates '''
    return sqrt(abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1]))

class Graph(object):
    def __init__(self, nodes=[], complexity=3):
        self.nodes = {}
        # Transfer node references from list to dict
        for n in nodes:
            self.nodes[n] = ()


    def find_neighbors(self, this_node):
        ''' Build and sort dict of neighbors for each node 
            by distance from shortest to longest

            of form:

            {
             node0: (node1, node2, node3),
             node1: (node0, node3, node2),
             node2: (node0, node1, node3),
             node3: (node1, node0, node2)
            }
            
             '''
        neighbors_dict = {}
        sorted_neighbors_tuple = ()

        for other_node in self.nodes:
            if other_node != this_node:
                neighbors_dict[other_node] = dist(other_node.xy, this_node.xy)

        # Sorted returns a tuple whose members are ordered by their value in
        #  unsorted_neighbors_dict.
        sorted_neighbors_tuple = sorted(neighbors_dict, key=neighbors_dict.get)

        print(str(this_node)[35:-1], ":", len(sorted_neighbors_tuple), "neighbors")

        for node in sorted_neighbors_tuple:
            print("\t: ...", str(node)[35:-1], neighbors_dict[node])
            self.nodes[node] = neighbors_dict[node]
            print(self.nodes)


class Node(object):
    def __init__(self, xy=(0, 0), weight=0):
        # Position data
        self.xy = xy
        # Arbitrary weight parameter
        self.weight = weight
        # 
        self.neighbors = []