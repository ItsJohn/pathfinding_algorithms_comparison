import networkx as nx
from networkx.readwrite import json_graph
import json
import random
import matplotlib.pyplot as plt

def createGraph(x):
	shuffle_list =[]
	G = nx.Graph()
	for i in range(1,x):
		G.add_node(i)

	if file_size == 100:
		name = 'small_graph.txt'
	if file_size == 1000:
		name = 'medium_graph.txt'
	if file_size == 10000:
		name = 'large_graph.txt'


	ii = 1
	node_list = G.nodes()
	for n in node_list:
		shuffle_list.append(n)
	random.shuffle(shuffle_list)

	for i,node in enumerate(reversed(node_list)):
		if i != 0:
			with open(name, 'a') as outfile:
				node2 = node-1
				weight = random.uniform(0.0, 1.0)
				G.add_edge(node,node2,weight= weight)
				outfile.write(str(node) + ',' + str(node2) + ',' + str(weight) +'\n')
		else:
			G = G

	index = 0
	while index <= len(node_list) /2:
		with open(name, 'a') as outfile:
			node = node_list[index]
			node2 = shuffle_list[index]
			weight = random.uniform(0.0, 1.0)
			G.add_edge(node,node2,weight= weight)
			outfile.write(str(node) + ',' + str(node2) + ',' + str(weight) +'\n')
			index = index + 1
		


	nx.draw(G)
	plt.show()



file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))

if file_size == 100 or file_size == 1000 or file_size ==10000:
	createGraph(file_size)
else:
	file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))
	createGraph(file_size)






