''' NodeGraphVis.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 14th, 2018
'''

import NodeGraph
import pyglet as pyg

def build_gl_render_batch(nodes):
    batch = pyg.graphics.Batch()
    pyg.gl.glPointSize(6)
    pyg.gl.glLineWidth(2)
    offset = (300, 250)
    magnif = 15

    for node in nodes:
        x1 = node.xy[0]*magnif + offset[0]
        y1 = node.xy[1]*magnif + offset[1]
        print("{0}, {1}".format(x1, y1))


        for neighbor in node.neighbors:
            x2 = neighbor[0].xy[0]*magnif + offset[0]
            y2 = neighbor[0].xy[1]*magnif + offset[1]
            cost = 255 - (255/neighbor[1])
            print("\t{0}, {1}, cost: {2}".format(x2, y2, cost))
            batch.add(2, pyg.gl.GL_LINES, None,
                ('v2i', (x1, y1, x2, y2)),
                ('c3f', (cost, 0, 0, cost, 0, 0)))

        batch.add(1, pyg.gl.GL_POINTS, None,
            ('v2i', (x1, y1)))


    return batch