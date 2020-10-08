import java.io.*;
import java.util.*;

class Fibonaci_With_java
{
    public static void main(String[] args) 
    {
        int n;
        Scanner x=new Scanner(System.in);
        System.out.print("Enter a number..:");
        int a=x.nextInt();
        int n1=0;
        int n2=1;
        System.out.print(n1+" "+n2);
        for(int i=0;i<a;i++)
        {
            n=n1+n2;
            System.out.print(""+n);
            n1=n2;
            n2=n;    
        }   
    }
}