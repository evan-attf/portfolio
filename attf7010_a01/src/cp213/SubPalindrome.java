package cp213;
import java.util.Scanner;
import java.lang.StringBuilder;

public class SubPalindrome 
{
	
	public static boolean isPalindrome(String s)
	{
		boolean pali = false;
		
		if (s.length() > 1)
		{
			StringBuilder subStringB = new StringBuilder();
			subStringB.append(s);
			
			String sub_left = "";
			String sub_right = "";
			
			sub_left = subStringB.substring(0, (subStringB.length() / 2));
			
			subStringB.reverse();
			sub_right = subStringB.substring(0, (subStringB.length() / 2));
			
			if (sub_left.equalsIgnoreCase(sub_right) == true)
				pali = true;
		}
		
		return pali;
	}
	
	public static void testSubPalindromes(final String s, final String alt_s)
	{
		StringBuilder stringB = new StringBuilder();
		//this program makes use of a StringBuilder object, which functions similarly to a string in Python
		stringB.append(alt_s); //adds the variable to the StringBuilder object
		
		System.out.print("Following substring(s) of the string '" + s + "' are palindrome(s): ");
		
		for (int i = 0; i < stringB.length() - 1; i++)
		{
			for (int j = i + 1; j < stringB.length(); j++)
			{
				String sub = stringB.substring(i, j + 1);
				
				if(isPalindrome(sub))
					System.out.print("'" + sub + "', ");
			}
		}
	}
	
	public static void main(String[] args) 
	{
		Scanner keyboard = new Scanner(System.in);
		
		System.out.print("Enter a string of size 1-10 characters: ");
		String string_variable = keyboard.nextLine();
		
		if (string_variable.length() < 1)
			System.out.println("'" + string_variable + "' is not a valid input, size less than 1");
		else if (string_variable.length() > 10)
			System.out.println("'" + string_variable + "' is not a valid input, size more than 10");
		else
		{
			String alt_string_variable = string_variable.replaceAll("[^a-zA-Z ]", "").replaceAll(" ", ""); //gets all non-letter characters and white space
			testSubPalindromes(string_variable, alt_string_variable);
		}
		keyboard.close();
	}

}
