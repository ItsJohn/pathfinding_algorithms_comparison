from networkx.readwrite import json_graph
import csv
import matplotlib.pyplot as plt
import networkx as nx
import timeit


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


def create_graph(filename, max_nodes):
    graph = open_file(filename)
    layout = nx.circular_layout(graph)
    astar_elapsed_time, dijkstra_elapsed_time = calculate(graph, max_nodes)
    print("\nA* execution time:", astar_elapsed_time)
    print("Dijkstra execution time:", dijkstra_elapsed_time)


def calculate(graph, max_nodes):
    source, destination = choose_nodes(max_nodes)

    astar_start_time = timeit.default_timer()
    nodes = nx.astar_path(graph, source, destination)
    astar_elapsed_time = timeit.default_timer() - astar_start_time

    dijkstra_start_time = timeit.default_timer()
    nodes = nx.dijkstra_path(graph, source, destination)
    dijkstra_elapsed_time = timeit.default_timer() - dijkstra_start_time

    return astar_elapsed_time, dijkstra_elapsed_time
