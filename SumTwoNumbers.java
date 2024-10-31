import java.util.Scanner;

public class SumTwoNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el primer número:");
        double num1 = scanner.nextDouble();
        System.out.println("Ingrese el segundo número:");
        double num2 = scanner.nextDouble();
        double suma = num1 + num2;
        System.out.println("La suma es: " + suma);
        scanner.close();
    }
}
