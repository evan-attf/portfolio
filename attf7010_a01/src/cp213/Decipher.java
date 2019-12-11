package cp213;
import java.util.Scanner;

public class Decipher 
{
	public static final String ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	public static final int ALPHA_LENGTH = ALPHA.length();

	public static String shift(String s, int n)
	{
		s = s.toUpperCase(); //converts letters to upper case so that they can be compared to ALPHA
		String shifted = "";
		char temp;
		int index;
		
		for (int i = 0; i < s.length(); i++)
		{
			if (Character.isLetter(s.charAt(i))) //checks if a character is a letter
			{
				temp = s.charAt(i);
				index = ALPHA.indexOf(temp); //checks the index of the character in ALPHA
				
				index -= n; //shifts the index
				if (index < 0) //and adds 26 if the index goes below 0
					index += 26;
				
				shifted += Character.toString(ALPHA.charAt(index));
			}
			else //if not, simply adds the character to the shifted string
				shifted += Character.toString(s.charAt(i));
		}
		return shifted;
	}
	
	public static String substitute(String s, String ciphertext)
	{
		s = s.toUpperCase(); //converts letters to upper case so that they can be compared to ALPHA
		String sub = "";
		char temp;
		int index;
		
		for (int i = 0; i < s.length(); i++)
		{
			if (Character.isLetter(s.charAt(i))) 
			{
				temp = s.charAt(i);
				index = ciphertext.indexOf(temp); //checks the index of the character in ciphertext
				
				temp = ALPHA.charAt(index); //subs it out with its corresponding letter in ALPHA
				sub += Character.toString(ALPHA.charAt(index));
			}
			else 
				sub += Character.toString(s.charAt(i));
		}
		return sub;
	}
	
	public static void main(String[] args)
	{
		final String CIPHERTEXT = "AVIBROWNZCEFGHJKLMPQSTUXYD";
		Scanner keyboard = new Scanner(System.in);
		
		String input;
		int shift_value;
		
		System.out.print("Enter a cipher string: ");
		input = keyboard.nextLine();
		System.out.print("Enter a shift length: ");
		shift_value = keyboard.nextInt();
		
		System.out.println("Plain text for shift: " + shift(input, shift_value));
		System.out.println("Plain text for substitute: " + substitute(input, CIPHERTEXT));
		
		keyboard.close();
	}

}
