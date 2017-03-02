import matplotlib.pyplot as plt
import networkx as nx
import csv


def draw_paths(graph, layout, path, color, width):
    nx.draw_networkx_edges(
        graph,
        pos=layout,
        edgelist=path,
        edge_color=color,
        width=width
    )


def create_graph(filename):
    graph = nx.Graph()
    with open(filename) as fh:
        for data in csv.reader(fh):
            graph.add_edge(int(data[0]), int(data[1]), weight=float(data[2]))
    paths = get_paths()
    draw(graph, paths)


def get_paths():
    paths = {
        'dijkstra': [],
        'bellman_ford': []
    }
    with open('paths.txt') as fh:
        for row_number, path in enumerate(csv.reader(fh)):
            for i, node in enumerate(path):
                if i is not 0 and node != '':
                    if row_number is 0:
                        paths['dijkstra'].append((int(path[i - 1]), int(node)))
                    else:
                        paths['bellman_ford'].append(
                            (int(path[i - 1]), int(node))
                        )
    return paths


def draw(graph, paths):
    layout = nx.fruchterman_reingold_layout(graph)
    nx.draw(graph, layout)
    draw_paths(graph, layout, paths['dijkstra'], 'c', 10)
    draw_paths(graph, layout, paths['bellman_ford'], 'b', 4)
    nx.draw_networkx_nodes(
        graph,
        pos=layout,
        node_color='y',
        node_size=300
    )
    nx.draw_networkx_labels(graph, pos=layout)

    plt.show()
