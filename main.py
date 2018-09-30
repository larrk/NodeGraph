#!/usr/bin/python3

''' main.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 12th, 2018
'''

import NodeGraph as nodeg
import NodeGraphVis as nodegv

import random as rand

import pyglet as pyg
from pyglet.gl import *

def build_nodes(num_nodes=3, max_weight=3):
    ''' Build a random node graph '''
    nodes = []
    for _ in range(0, num_nodes):
        xy = (rand.randint(-10, 10), rand.randint(-10, 10))
        nodes.append(nodeg.Node(xy, rand.randint(1, max_weight)))
    
    return nodes

def pyglet_init(graph):
    window = pyg.window.Window()
    batch = nodegv.build_gl_batch_nodes(graph.nodes)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyg.app.run()

if __name__ == '__main__':
    # Generate a set of random nodes
    ng = nodeg.Graph(build_nodes(20, 6))
    # Find their neigbors
    ng.find_all_neighbors()
    # Visualize graph
    pyglet_init(ng)