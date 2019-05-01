#!/usr/bin/python3

''' main.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 12th, 2018
'''

import NodeGraph as nodeg
import NodeGraphVis as nodegv
import random as rand
import pyglet as pyg

xy = (640, 640)
window = pyg.window.Window(width=xy[0], height=xy[1])



if __name__ == '__main__':

    # Generate a set of random nodes
    ng = nodeg.Graph([], 50, 3)

    @window.event
    def on_draw():
        window.clear()
        batch = nodegv.build_gl_batch_nodes(ng.nodes,
                                point_size=4,
                                line_width=1,
                                scaling=1)
        batch.draw()

    @window.event
    def on_mouse_release(x, y, button, modifiers):
        x -= int(xy[0]/2)
        y -= int(xy[1]/2)
        if button == 1:
            ng.pushNode(xy=(x, y))
        elif button == 4:
            if(len(ng.nodes) > 1):
                ng.popNode()

    @window.event
    def on_mouse_scroll(x, y, scroll_x, scroll_y):
        ng.on_mouse_scroll(x, y, scroll_x, scroll_y)

    pyg.app.run()