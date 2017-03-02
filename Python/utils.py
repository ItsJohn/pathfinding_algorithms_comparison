from networkx.readwrite import json_graph
import csv
import matplotlib.pyplot as plt
import networkx as nx
import timeit as time
import bellmanford as bf


def sanitize_input(value, max_node):
    try:
        if value:
            value = int(value)
        else:
            print("You didn't enter a value")
            return False
    except ValueError:
        print("Please enter an integer")
        return False
    if value >= 1 and value <= max_node:
        return True
    else:
        print("Please enter an integer that is within the option range")
        return False


def check_input(choice, max_nodes):
    while not sanitize_input(choice, max_nodes):
        choice = input('Enter option: ')
    return choice


def choose_nodes(max_nodes):
    print("\nChoose a node between 1 and", max_nodes)
    print("This will be the node the algorithm will be starting from")
    choiceA = check_input(input('Enter option: '), max_nodes)

    print("\nChoose another node between 1 and", max_nodes)
    print("This will be the node the algorithm will be finishing on")
    choiceB = check_input(input('Enter option: '), max_nodes)
    return int(choiceA), int(choiceB)


def open_file(filename):
    graph = nx.Graph()
    with open(filename) as fh:
        for data in csv.reader(fh):
            graph.add_edge(int(data[0]), int(data[1]), weight=float(data[2]))
    return graph


def write_to_file(open_file, algorithm):
    for i, node in enumerate(algorithm):
        if i < len(algorithm) - 1:
            open_file.write(str(node) + ',')
        else:
            open_file.write(str(node) + '\n')


def write_paths_to_file(bellman_ford_nodes, dijkstra_nodes):
    with open('paths.txt', 'w') as fh:
        write_to_file(fh, dijkstra_nodes)
        write_to_file(fh, bellman_ford_nodes)


def create_graph(filename, max_nodes):
    graph = open_file(filename)
    bellman_ford_elapsed_time, dijkstra_elapsed_time = calculate(
        graph,
        max_nodes
    )
    print("\nBellman Ford execution time:", bellman_ford_elapsed_time)
    print("Dijkstra execution time:", dijkstra_elapsed_time)


def calculate(graph, max_nodes):
    source, destination = choose_nodes(max_nodes)

    bellman_ford_start_time = time.default_timer()
    bellman_ford_nodes = bf.bellman_ford(
        graph,
        source, destination,
        'distance'
    )
    bellman_ford_elapsed_time = time.default_timer() - bellman_ford_start_time

    dijkstra_start_time = time.default_timer()
    dijkstra_nodes = nx.dijkstra_path(graph, source, destination, 'distance')
    dijkstra_elapsed_time = time.default_timer() - dijkstra_start_time

    write_paths_to_file(bellman_ford_nodes[1], dijkstra_nodes)

    return bellman_ford_elapsed_time, dijkstra_elapsed_time
