import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

import javax.swing.JFrame;

import org.jgrapht.UndirectedGraph;
import org.jgrapht.alg.DijkstraShortestPath;
import org.jgrapht.alg.BellmanFordShortestPath;
import org.jgrapht.alg.util.*;

import org.jgrapht.ext.JGraphModelAdapter;
import org.jgrapht.graph.AsWeightedGraph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.*;
import org.jgrapht.*;
import org.jgrapht.alg.*;
import org.jgraph.JGraph;

import org.jgraph.JGraph;
import org.jgrapht.ext.JGraphModelAdapter;



public class dijkstras_alg_java 
{
	String filename;

	public dijkstras_alg_java(String filename2) throws IOException {
		this.filename = filename2;
		start(filename2);
	}
	public static void start(String filename) throws IOException
	{
		Scanner reader = new Scanner(System.in);
		
		String node1 = null;
		String node2 = null;
		String weight = null;
		int startNode = 0;
		int endNode = 0;
		
		
		while(startNode == 0 | endNode == 0)
		{
			System.out.println("Enter a start node");
			startNode = reader.nextInt();
			System.out.println("Enter a destination node");
			endNode = reader.nextInt();
		}
		
		
		String startSearch = String.valueOf(startNode);
		String destinationSearch = String.valueOf(endNode);

		
		Graph G = create_graph(filename);
		
		long startDijkstra = System.nanoTime();
		List<DefaultEdge> list = (List) DijkstraShortestPath.findPathBetween(G, startSearch, destinationSearch);
		long endDijkstra = System.nanoTime();
		
		
		long startBellman = System.nanoTime();
		List<DefaultEdge> list2 = (List) BellmanFordShortestPath.findPathBetween(G, startSearch,destinationSearch);
		long endBellman = System.nanoTime();
		
		
		System.out.println("Dijkstra's Duration (ms) " + (endDijkstra - startDijkstra));
		System.out.println(list);
		System.out.println("");
		System.out.println("BellmanFord Duration (ms) " + (endBellman - startBellman));
		System.out.println(list2);
		
		Set<String> dijkstra_set = getNodes( list, G);
		Set<String> bellman_set = getNodes( list, G);
		
		String fileName = "Path.csv";
		writeToFile( dijkstra_set, fileName);
		writeToFile(bellman_set, fileName);
		
		
		
	}
	
	public static Graph create_graph(String filename) throws IOException
	{
		String node1 = null;
		String node2 = null;
		String weight = null;
		
		String[] words;
		 SimpleDirectedWeightedGraph<String, DefaultWeightedEdge>  G = 
		            new SimpleDirectedWeightedGraph<String, DefaultWeightedEdge>
		            (DefaultWeightedEdge.class);
		
		
		try {
			File file = new File(filename);
			FileReader fileReader = new FileReader(file);//enables you to read from a file
			BufferedReader bufferedReader = new BufferedReader(fileReader);//buffered reader allows you read a line at a time
			StringBuffer stringBuffer = new StringBuffer();
			String line;
			String theLine;
			while ((line = bufferedReader.readLine()) != null) {
				words = line.split(",");
				for (int a = 0; a < words.length; a++) 	//for every line in the graph thats an array of words				
				{
					if(a == 0)
					{
						node1 = words[a];
						G.addVertex(node1);
					}
					for (int b = 0; b < words.length; b++) 					
					{
						if(b == 1)
						{
							node2 = words[b];
							G.addVertex(node2);
						}
	
					}
					for (int c = 0; c < words.length; c++) 					
					{
						if(c == 2)
						{
							weight = words[c];
						}
						
					}
					double value = Double.parseDouble(weight);
					DefaultWeightedEdge e1 = G.addEdge(node1, node2); 
		            G.setEdgeWeight(e1, value); 
					break;
				}
				
				
				stringBuffer.append(line);
				stringBuffer.append("\n");
			}
			fileReader.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return G;
	}
	
	public static void writeToFile(Set<String> set, String fileName) throws IOException
	{
		Object[] set_to_list = set.toArray();
		BufferedWriter writer = null;
		writer = new BufferedWriter(new FileWriter(fileName));
		for (int i =0; i< set_to_list.length;i++)
		{
			String temp = (String) set_to_list[i];
			
			
			try {
				writer.write(temp + ",");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		 
		}

		writer.close();
		
	}
	
	
	public static Set getNodes(List<DefaultEdge> list, Graph G) throws IOException
	{
		
		Set<String> set = new LinkedHashSet<String>();//had to use LinkedHashSet as HashSet does not maintain input order 
				
				for (int i =0; i < list.size();i++)
				{
					String v1 = (String) G.getEdgeSource((DefaultWeightedEdge) list.get(i));
					   
					String v2 = (String) G.getEdgeTarget((DefaultWeightedEdge) list.get(i));
					
					set.add(v1);
					set.add(v2);
				}
		return set;
	}
	
}
