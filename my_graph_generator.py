import networkx as nx
from networkx.readwrite import json_graph
import json
import random
import matplotlib.pyplot as plt

def createGraph(x):
	shuffle_list =[]
	G = nx.Graph()
	for i in range(1,x+1):
		G.add_node(i)

	if file_size == 100:
		name = 'small_graph.txt'
	if file_size == 1000:
		name = 'medium_graph.txt'
	if file_size == 10000:
		name = 'large_graph.txt'


	node_list = G.nodes()
	with open(name, 'a') as outfile:
			weight = random.uniform(0.0, 1.0)
			G.add_edge(node_list[0],node_list[len(node_list) -1],weight= weight)
			outfile.write(str(node_list[0]) + ',' + str(node_list[len(node_list) -1]) + ',' + str(weight) +'\n')

	for i,node in enumerate(node_list):
		if i is not 0 :
			with open(name, 'a') as outfile:
				node2 = node_list[i-1]
				
				weight = random.uniform(0.0, 1.0)
				G.add_edge(node,node2,weight= weight)
				outfile.write(str(node) + ',' + str(node2) + ',' + str(weight) +'\n')
				
	shuffle_list =[]
	for n in node_list:
		shuffle_list.append(n)
	random.shuffle(shuffle_list)

	index = 0
	while index <= len(node_list) /2:
		if index is not 0:
			with open(name, 'a') as outfile:
				node1 = node_list[index]
				node3 = shuffle_list[index]
				temporary = [node1,node3]
				s = tuple(sorted(temporary))
				if s not in G.edges() and s[0] is not s[1]:
					G.add_edge(node1,node3,weight= weight)
					outfile.write(str(node1) + ',' + str(node3) + ',' + str(weight) +'\n')
		index = index +1

file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))

if file_size == 100 or file_size == 1000 or file_size ==10000:
	createGraph(file_size)
else:
	file_size = int(input('Enter the size of the graph (100, 1000 or 10,000): '))
	createGraph(file_size)






