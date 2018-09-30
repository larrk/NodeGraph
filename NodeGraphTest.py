''' NodeGraphTest.py
    Ryan Stenmark <ryanpstenmark@gmail.com
    October 9th, 2018
'''


def test_dist():
    ''' NodeGraph.dist unit test '''
    # Build list of random points
    xy = []
    for _ in range(1, 10):
        xy.append((rand.randint(-10, 10), rand.randint(-10, 10)))

    # Compute distances between each point
    for this_xy in xy:
        for other_xy in xy:
            # Test
            print(this_xy, other_xy, dist(this_xy, other_xy))

def test_find_neighbors():
    ''' NodeGraph.Graph.find_neighbors unit test '''
    # Build graph
    ng = nodeg.Graph(build_nodes(10, 8))
    
    for this_node in ng.nodes:
        # Test
        edges = this_node.find_neighbors(ng)
        neighbor_count = len(this_node.neighbors)

        print("{0} has {1} neighbors:".format(
            str(this_node)[25:-1], neighbor_count)
        )

        for edge in edges:
            print("\t:{0}, {1} units away".format(
                str(edge[0])[25:-1], str(edge[1]))
            )
