package cp213;
import java.util.Scanner;
import java.util.Arrays;

public class ValidDeclaration 
{
	public static String[] DATA_TYPES = {"byte", "short", "char", "int", "long", "float", "double", "boolean"};

	public static boolean isValid(String statement)
	{
		boolean valid = false; //if the method is unable to determine if the String is valid, returns false by default
		
		statement = statement.trim(); //gets rid of surrounding whitespace
		if (statement.indexOf(";") == statement.length() - 1) //checks if the string ends with a semicolon
		{
			statement = statement.replace(";", "").trim(); //if it does, gets rids of semicolon and strips again
			String[] s_array = statement.split(" +"); //splits the string using the space(s) in between the dataType and variableName
			
			if (s_array.length == 2)
			{
				s_array[0] = s_array[0].trim();
				s_array[1] = s_array[1].trim();
				
				if (Arrays.asList(DATA_TYPES).contains(s_array[0]) == true) //checks if the dataType is valid
				{
					if ((s_array[1].charAt(0) == '_' && s_array[1].length() != 1) || Character.isLetter(s_array[1].charAt(0)))
					//checks if the variableName is valid
					{
						valid = true; //if all is valid, returns true
					}
				}
			}	
		}
		return valid;
	}
	
	public static void main(String[] args) 
	{
		Scanner keyboard = new Scanner(System.in);
		String statement = "";
		
		System.out.print("Enter a string: ");
		statement = keyboard.nextLine();
		
		if (isValid(statement) == true)
		{
			System.out.println("'" + statement + "' is a valid Java variable definition.");
		}
		else 
		{
			System.out.println("'" + statement + "' is not a valid Java variable definition.");
		}
		
		keyboard.close();
	}
}
