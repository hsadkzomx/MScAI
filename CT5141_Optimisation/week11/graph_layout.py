import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


"""A module to demonstrate a force-directed graph layout algorithm.

There are better implementations in Graphviz (fdp), NetworkX, etc.
But this is intended to be more readable.

"""

def graph_layout(G,
                 edge_length_name=None,
                 alpha=0.0001,
                 repulse_lower_bound=10**-2,
                 repulse_upper_bound=np.inf,
                 maxits=20000,
                 tol=0.0001,
                 plot_every=100):

    """A simple approach to force-directed graph layout.

    G: an nx graph, optionally with edge length values
    edge_length_name: string giving the key in the edge dict whose value is the desired edge length. if None (default), then all edges are assumed to be of length 1
    alpha: learning rate
    repulse_lower_bound: nodes nearer than this will be treated as if at this distance, to avoid dividing by small numbers in repulsive force
    repulse_upper_bound=np.inf: nodes more distant than this will be ignored in repulsive force
    maxits: maximum iterations of the algorithm
    tol: algorithm may stop early if nodes move by a small amount
    plot_every: save images every few steps to visualise progress, but use plot_every=None to avoid saving anything

    """

    n = G.order() # number of nodes
    node_order = sorted(G.nodes()) # need a fixed ordering of nodes

    # output position, a 2D array, randomly initialised
    x = np.random.random((n, 2))

    # if we want to hard-code initial positions for some experimental
    # purposes, we could do that here, eg:
    # x = np.array([
    #     [0, 0],
    #     [2.5, 2],
    #     [0.5, 2],
    #     [2, 0.]])

    for it in range(maxits):

        # an array representing the sum of forces on each node.  it
        # consists of one force-vector for each node, so it is the
        # same shape as x.
        dx = np.zeros_like(x)

        for i in range(n):
            for j in range(n):

                # for this pair, get the current distance
                xi_less_xj = (x[i] - x[j]) # the vector from xj to xi
                C = np.linalg.norm(x[i] - x[j]) # current distance between xi and xj: a number. norm means length of vector

                ni, nj = node_order[i], node_order[j]
                if (ni, nj) in G.edges:

                    edge = G.edges[ni, nj]
                    if edge_length_name:
                        D = edge[edge_length_name]
                    else:
                        D = 1

                    # Spring-like force on each pair of nodes: spring
                    # expands or contracts to try to become the right
                    # length, so this may be attractive or
                    # repulsive. eg for dx[i], if the current distance
                    # is too short, then C < D, so the
                    # middle term is positive, so it is a positive
                    # force in the direction of xi_less_xj, that is
                    # from xi *away* from xj; and vice versa if the
                    # current distance is too long. 
                    dx[i] += alpha * (D - C) * xi_less_xj
                    
                else:

                    # Coulomb-like repulsive force on nodes that get
                    # too near
                    if C < repulse_upper_bound:
                        if C < repulse_lower_bound:
                            # avoid divide-by-zero but still give a nudge
                            C = repulse_lower_bound
                        dx[i] += alpha * xi_less_xj / (C ** 2)
                    

        # the key line: move x according to the summed forces dx
        x += dx

        # calculate size of this step. norm means length of the vector
        step_mag = np.linalg.norm(dx) 

        # outputs
        print("%s %.3f" % (str(it).zfill(6), step_mag))
        if plot_every:
            if (step_mag < tol or it % plot_every == 0):
                # if plotting is allowed, then plot according to plot_every AND
                # plot just before quitting.
                plot(G, x, node_order,
                     os.path.join(dirname, "graph_layout_iteration_" + str(it).zfill(6) + ".png"),
                     edge_length_name=edge_length_name
                )

        if step_mag < tol:
            # if we have made a very small movement we can quit
            break
    return x


def plot(G, x, node_order, filename, edge_length_name=None):
    # pos must be a dict in node: position format
    pos = {n: x[node_order.index(n)] for n in node_order}
    fig, ax = plt.subplots(figsize=(9, 9))
    # draw the nodes (with their names) and edges
    nx.draw_networkx(G, pos=pos, ax=ax)
    if edge_length_name:
        # plot the intended edge length values as well
        # if they exist
        lbls = {(n1, n2): G.edges[(n1, n2)][edge_length_name]
                for n1, n2 in G.edges()}
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=lbls)
    plt.savefig(filename)
    plt.close()

def test_weighted():
    import random
    G = nx.Graph()
    n = 10
    for i in range(n):
        G.add_edge(i, i+1 % n, length=10)
        G.add_edge(i, random.randrange(10), length=random.randrange(1, 10))
    graph_layout(G, alpha=0.01, edge_length_name="length")

def make_diagram():
    np.random.seed(2)
    G = nx.Graph()
    G.add_edge(0, 1, length=3)
    G.add_edge(1, 2, length=4)
    G.add_edge(2, 0, length=5)
    graph_layout(G, alpha=0.05, maxits=50, plot_every=1, edge_length_name="length")
    
    


if __name__ == "__main__":
    import shutil
    import os
    import sys
    
    dirname = "graph_layout_saves"
    try:
        # if the save directory exists, delete it
        shutil.rmtree(dirname)
    except Exception as e:
        # if not, don't worry
        print(e)
        pass
    # make the save directory again
    os.mkdir(dirname)

    if len(sys.argv) > 1:
        np.random.seed(int(sys.argv[1]))

    # graph_layout(nx.cycle_graph(10), alpha=0.01)
    graph_layout(nx.grid_graph(dim=[7, 7]), alpha=0.01)
    # graph_layout(nx.cycle_graph(4), alpha=0.01, plot_every=5, maxits=200)
    # graph_layout(nx.grid_graph(dim=[3, 3, 3]), alpha=0.01)
    # graph_layout(nx.barbell_graph(5, 5), alpha=0.01)
    # graph_layout(nx.barabasi_albert_graph(10, 5), alpha=0.01)
    # test_weighted()
    # make_diagram()
