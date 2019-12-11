package cp213;
import java.util.Scanner;

public class Lab01 
{

	public static int gcd(int a, int b) 
	{
		while (a != b)
		{
			if(a > b)
				a = a - b;
			else
				b = b - a;
		}
		return b;
    }
	
	public static void main(String[] args) 
	{
		Scanner keyboard = new Scanner(System.in);
        int a = 0;
        int b = 0;
        int c = 0;

        // Read an integer from the keyboard.
        System.out.print("Enter a (0 to quit): ");
        a = keyboard.nextInt();
        while (a != 0)
        {
        	System.out.print("Enter b: ");
            b = keyboard.nextInt();
            c = Lab01.gcd( a, b );
            
            System.out.println("The GCD of " + a + " and " + b + " is " + c);
            
            System.out.print("Enter a (0 to quit): ");
            a = keyboard.nextInt();
        }
        
        keyboard.close();
	}

}
