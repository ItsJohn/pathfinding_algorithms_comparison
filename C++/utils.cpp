#include "utils.h"


typedef property<edge_weight_t, double> EdgeWeight;
typedef adjacency_list<listS, vecS, undirectedS, no_property, EdgeWeight> UndirectedGraph;
typedef graph_traits<UndirectedGraph>::vertex_descriptor vertex_descriptor;

void writeToFile(vector<graph_traits<UndirectedGraph>::vertex_descriptor > path, int destination) {
      // Prints the path obtained in reverse
      vector<graph_traits<UndirectedGraph>::vertex_descriptor >::reverse_iterator it;

      ofstream myfile;
      myfile.open ("../paths.txt");
      for (it = path.rbegin(); it != path.rend(); ++it) {
            if(destination != *it) {
                  myfile << *it << ',';
            } else {
                  myfile << *it;
            }
      }
      myfile.close();
}

void findPath(UndirectedGraph g, int source, int destination) {
      property_map<UndirectedGraph, edge_weight_t>::type EdgeWeightMap = get(edge_weight_t(), g);
      vector<vertex_descriptor> p(num_vertices(g));
      vector<int> d(num_vertices(g));

      vertex_descriptor s = vertex(source, g);
      vertex_descriptor goal = vertex(destination, g);

      clock_t tStart = clock();
      bool r = bellman_ford_shortest_paths(g, s, weight_map(EdgeWeightMap).distance_map(&d[0]).predecessor_map(&p[0]));
      cout << "Bellman Ford time: " << (double)(clock() - tStart)/CLOCKS_PER_SEC << endl;

      tStart = clock();
      dijkstra_shortest_paths(g, s, predecessor_map(&p[0]).distance_map(&d[0]));
      cout << "Dijkstra time: " << (double)(clock() - tStart)/CLOCKS_PER_SEC << endl;

      // p[] is the predecessor map obtained through dijkstra
      // name[] is a vector with the names of the vertices
      // s and goal are vertex descriptors
      vector<graph_traits<UndirectedGraph>::vertex_descriptor > path;
      graph_traits<UndirectedGraph>::vertex_descriptor current = goal;

      while(current != s) {
            path.push_back(current);
            current = p[current];
      }
      path.push_back(s);
      writeToFile(path, destination);
}


void Utils::openfile(string filename) {
      ifstream file(filename);
      UndirectedGraph g;
      string node1;
      string node2;
      string weight;

      while (file.good()) {
            getline(file, node1, ',' );
            getline(file, node2, ',' );
            getline(file, weight, '\n' );
            add_edge(atoi(node1.c_str()), atoi(node2.c_str()), atof(weight.c_str()), g);
      }
      int source;
      int destination;
      cout << "Enter the start node: ";
      cin >> source;
      cout << "Enter the destination node: ";
      cin >> destination;
      findPath(g, source, destination);
}
