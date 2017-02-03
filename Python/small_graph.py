from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import networkx as nx
import json
import timeit


def get_path(nodes):
    path = []
    for i, node in enumerate(nodes):
        if i is not 0:
            path.append((nodes[i - 1], node))
    return path


with open('small_graph.json') as fh:
    data = json.load(fh)

graph = json_graph.node_link_graph(data)
layout = nx.circular_layout(graph)

astar_start_time = timeit.default_timer()
nodes = nx.astar_path(graph, 2, 99)
astar_elapsed_time = timeit.default_timer() - astar_start_time

dijkstra_start_time = timeit.default_timer()
nodes = nx.dijkstra_path(graph, 2, 99)
dijkstra_elapsed_time = timeit.default_timer() - dijkstra_start_time

path = get_path(nodes)

nx.draw(graph, layout, node_color='k')
nx.draw_networkx_edges(graph, layout, edgelist=path, edge_color='r', width=10)

print("A* execution time:", astar_elapsed_time)
print("Dijkstra execution time:", dijkstra_elapsed_time)

plt.show()
