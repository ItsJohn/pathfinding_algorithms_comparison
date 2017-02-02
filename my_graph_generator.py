import networkx as nx
from networkx.readwrite import json_graph
import json
import random
import matplotlib.pyplot as plt

def createGraph(x):
	G = nx.Graph()
	i =1
	while(i <= x):
		G.add_node(i)
		i = i +1

	ii = 1
	while(ii<=x):
		node_list = G.nodes()
		the_node = random.randint(1,x-1)
		node1 = node_list[the_node]
		the_second_node = random.randint(1,x-1)
		node2 = node_list[the_second_node]
		weight = random.uniform(0.0, 1.0)
		G.add_edge(node1,node2,weight= weight)
		ii = ii + 1
		

	data = json_graph.node_link_data(G)
	result = data['links']
	if file_size == 100:
		name = 'small_graph'
	if file_size == 1000:
		name = 'medium_graph'
	if file_size == 10000:
		name = 'large_graph'

	with open(name, 'w') as outfile:
	    json.dump(result, outfile)

	nx.draw(G)

	plt.show()
	print(result)


file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))

if file_size == 100 or file_size == 1000 or file_size ==10000:
	createGraph(file_size)
else:
	file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))






