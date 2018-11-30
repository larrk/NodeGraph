#!/usr/bin/python3

''' main.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 12th, 2018
'''

import NodeGraph as nodeg
import NodeGraphVis as nodegv

import random as rand

import pyglet as pyg

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
    ng = nodeg.Graph([], 40, 4)
    # Visualize graph
    pyglet_init(ng)