# Student name: Jiarong Li
# Student ID: 20230033

import sys
import networkx as nx

def txt_to_dict(txt):
    """
    Convert txt file to dictionary.
    param txt: fine name
    return: a dictionary
    """

    dict_f = eval(open(txt).read())
    return dict_f

def build_graph(dict_f):
    """
    Build a graph with *networkx*
    """

    G = nx.Graph()
    
    for society in dict_f:
        for i in range(0, len(dict_f[society])-1):
            for j in range(i+1, len(dict_f[society])):
                G.add_edge(dict_f[society][i],dict_f[society][j],attr=society)
    
    return G

def find_path(G, start="Dracula", end="Pumpkin", cutoff=5):
    """
    Find all paths and shortest path between start node and end node.
    If there is no path between the start node and end node, print "no path".
    """

    # find all paths which length <= 4
    paths = nx.all_simple_paths(G, source=start, target=end, cutoff=cutoff)
    
    if list(paths) == []:
        # if there's no path between the start node and end node
        print(f"======= No path between {start} and {end}! =======")
        
    else:
        paths = nx.all_simple_paths(G, source=start, target=end, cutoff=cutoff)
        print(f"""\n======= All the paths from {start} to {end} with the paths of length <= {cutoff} =======
        {list(paths)}""")
       
        # find the shortest path
        shortest_path = nx.shortest_path(G, start, end)
        print(f"\n======= The shortest path from {start} to {end} is {shortest_path}=======\n\n")


dict_f = txt_to_dict(sys.argv[1])
G = build_graph(dict_f)
find_path(G)
