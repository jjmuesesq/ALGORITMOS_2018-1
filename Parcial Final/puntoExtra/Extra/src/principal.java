import java.util.Arrays;
import java.util.Scanner;

public class principal {

	public static void imprimir_mtx(double[][] mtx) {
		
		for (int i = 0; i < mtx.length; i++) {
			String s = "";
			for (int j = 0; j < mtx.length; j++) {
				s += ((int)mtx[i][j] + "   ");
			}
			System.out.println(s);
		}
	}
	
	public static class FloydWarshall {

	    // graph represented by an adjacency matrix
	    private double[][] graph;

	    private boolean negativeCycle;

	    public FloydWarshall(int n) {
	        this.graph = new double[n][n];
	        initGraph();
	    }

	    private void initGraph() {
	        for (int i = 0; i < graph.length; i++) {
	            for (int j = 0; j < graph.length; j++) {
	                if (i == j) {
	                    graph[i][j] = 0;
	                } else {
	                    graph[i][j] = Double.POSITIVE_INFINITY;
	                }
	            }
	        }
	    }

	    public boolean hasNegativeCycle() {
	        return this.negativeCycle;
	    }

	    // utility function to add edges to the adjacencyList
	    public void addEdge(int from, int to, double weight) {
	        graph[from][to] = weight;
	    }

	    // all-pairs shortest path
	    public double[][] floydWarshall() {
	        double[][] distances;
	        int n = this.graph.length;
	        distances = Arrays.copyOf(this.graph, n);

	        for (int k = 0; k < n; k++) {
	            for (int i = 0; i < n; i++) {
	                for (int j = 0; j < n; j++) {
	                    distances[i][j] = Math.min(distances[i][j], distances[i][k] + distances[k][j]);
	                }
	            }

	            if (distances[k][k] < 0.0) {
	                this.negativeCycle = true;
	            }
	        }

	        return distances;
	    }

	}
	
	public static double maxyMatriz(double[][] entrada) {
		double tmp=Double.NEGATIVE_INFINITY;
		
		for (int i = 0; i < entrada.length; i++) {
			for (int j = 0; j < entrada.length; j++) {
				if (tmp <= entrada[i][j]){
					tmp=entrada[i][j];
				}
			}
		}
		return tmp;
	}
	public static void main(String[] args) {
		
		FloydWarshall mi_grafo = new FloydWarshall(10);
		
		mi_grafo.addEdge(0, 1, (double)40);
		mi_grafo.addEdge(0, 2, (double)8);
		mi_grafo.addEdge(0, 3, (double)10);
		mi_grafo.addEdge(1, 6, (double)10);
		mi_grafo.addEdge(1, 4, (double)6);
		mi_grafo.addEdge(2, 1, (double)4);
		mi_grafo.addEdge(2, 5, (double)2);
		mi_grafo.addEdge(2, 3, (double)12);
		mi_grafo.addEdge(3, 5, (double)1);
		mi_grafo.addEdge(4, 6, (double)4);
		mi_grafo.addEdge(4, 5, (double)2);
		mi_grafo.addEdge(4, 2, (double)2);
		mi_grafo.addEdge(5, 7, (double)4);
		mi_grafo.addEdge(5, 8, (double)3);
		mi_grafo.addEdge(6, 7, (double)20);
		mi_grafo.addEdge(6, 9, (double)1);
		mi_grafo.addEdge(7, 4, (double)0);
		mi_grafo.addEdge(7, 9, (double)20);
		mi_grafo.addEdge(8, 3, (double)6);
		mi_grafo.addEdge(8, 7, (double)10);
		mi_grafo.addEdge(8, 9, (double)2);
		
		imprimir_mtx(mi_grafo.floydWarshall());
		//System.out.println(maxyMatriz(mi_grafo.floydWarshall()));
		
		/***
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int peso= sc.nextInt();
		//System.out.println(N);
		//System.out.println(peso);
		
		int matriz[][] = new int[N][N]; 
		for (int x=0; x < matriz.length; x++) {
			  for (int y=0; y < matriz[x].length; y++) {
			     matriz[x][y] = sc.nextInt();
			  }
		}
		
		for (int x=0; x < matriz.length; x++) {
			  for (int y=0; y < matriz[x].length; y++) {
			    System.out.println(matriz[x][y]);
			  }
		}	**/
		
		
	}

}

//funcion recorrer matriz
