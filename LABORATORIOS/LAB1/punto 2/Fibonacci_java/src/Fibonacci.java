
import java.util.Scanner;
public class Fibonacci {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Fibonacci objFibo = new Fibonacci();
		System.out.println("ingrese el numero: ");
		int num = sc.nextInt();
		System.out.println("La sucecion fibonacci de " + num + " mediante recursividad es: " + objFibo.fibRecursivo(num));
		System.out.println("La sucecion fibonacci de " + num + " mediante iteración es: " + objFibo.fibIterativo(num));
	}
			
	//Metodo recursivo para la sucesión Fibonacci
	public int fibRecursivo(int n){
		
		if(n==1 || n==2) {
			//caso base
			return 1;
		}else {
			return fibRecursivo(n-1)+ fibRecursivo(n-2);
		}
	} 
	
	//Metodo iterativo para la sucesión Fibonacci
	public int fibIterativo(int n){
		int F = 0, first=1, second = 0;
		
		while(n>0) {
			F = first + second;
			first = second;
			second = F;
			n--;			
		}
		
		return F;
		
	}

}
