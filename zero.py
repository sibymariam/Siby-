import java.util.Scanner;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in= new Scanner(System.in);
		int a=in.nextInt();
		if(a==0)
	   {
	   	System.out.println("Zero");
	   }
	   else if(a<0)
	   {
	   	System.out.println("Negative");
	   }
	   else
	   {
	   	System.out.println("Positive");
	   }
	}
}
