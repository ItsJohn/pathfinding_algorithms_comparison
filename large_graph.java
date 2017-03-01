import java.io.IOException;

public class large_graph
{
	public static void main(String args[]) throws IOException
	{
		String filename = "large_graph.csv";
		dijkstras_alg_java temp = new dijkstras_alg_java(filename);
		System.out.println("Done");
	}
}
