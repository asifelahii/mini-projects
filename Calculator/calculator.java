// Calculator using conditonal statements (if, else if, else).
import java.util.*;

class calculation{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        double a = sc.nextDouble();
        System.out.println("Enter second number: ");
        double b = sc.nextDouble();

        char operation = sc.next().charAt(0);

        if(operation == '+')
            System.out.println("a + b = " + (a+b));
        else if(operation == '-')
            System.out.println("a - b = " + (a-b));
        else if(operation == '*')
            System.out.println("a * b = " + (a*b));
        else if(operation == '/')
            System.out.println("a / b = " + (a/b));
        else if(operation == '%')
            System.out.println("a % b = " + (a%b));
        else if(operation == '^')
            System.out.println("a ^ b = " + (int)Math.pow(a,b));
        else
            System.out.println("Invalid operation.");

    }
}