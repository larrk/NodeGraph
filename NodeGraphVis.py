''' NodeGraphVis.py
    Ryan Stenmark <ryanpstenmark@gmail.com>
    July 14th, 2018
'''

import pyglet as pyg

def build_gl_batch_nodes(nodes, point_size=4, line_width=2, scaling=15):
    ''' Batch a list of nodes to render in one draw call '''

    # Instantiate batch
    batch = pyg.graphics.Batch()

    # Configure render options
    pyg.gl.glPointSize(point_size)
    pyg.gl.glLineWidth(line_width)
    offset = (300, 300)
    scale = scaling

    def transform(xy):
        ''' Transform coordinates according to render options '''
        x = xy[0] * scale + offset[0]
        y = xy[1] * scale + offset[1]
        return [x, y]

    # For every node
    for node in nodes:
        # Get this node's coordinates and transform
        xy1 = [
            node.xy[0],
            node.xy[1]
        ]

        # Transform node coordinates
        xy1 = transform(xy1)

        # Unpack this node's coordinates
        x1, y1 = xy1[0], xy1[1]

        # Add point to batch
        batch.add(1, pyg.gl.GL_POINTS, None,
                  ('v2i', (x1, y1)))

        # For every neighbor to this node
        for neighbor in node.neighbors:

            # Get the neighbor's coordinates
            xy2 = [
                neighbor[0].xy[0],
                neighbor[0].xy[1]
            ]
            
            # Transform neighbor coordinates
            xy2 = transform(xy2)

            # Determine line color
            cost_r = neighbor[1]/20
            cost_g = 1-cost_r

            # Unpack neighbor's coordinates
            x2, y2 = xy2[0], xy2[1]
            
            # Add line to batch
            batch.add(2, pyg.gl.GL_LINES, None,
                      ('v2i', (x1, y1, x2, y2)),
                      ('c3f', (cost_r, cost_g, 0, cost_r, cost_g, 0)))

    return batch
