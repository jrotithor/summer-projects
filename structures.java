import java.util.*;
class structures{
public static void main(String [] args){
	int [][] a = {{0,0},{0,0},{0,0},{0,0},{0,0}};
  for(int i = 0; i < 5; i++)
     for(int j = 0; j < 2; j++)
     	a[i][j] = (i+1)*(j+1);
  for(int i = 0; i < 5; i++)
     for(int j = 0; j < 2; j++)
     System.out.println(a[i][j]);
  ArrayList <Integer> b = new ArrayList<Integer>();
  b.add(15);
  b.add(25);
  System.out.println(b.indexOf(25));
  System.out.println(b.isEmpty());
  for(int i : b)
     System.out.println(i);
  b.remove(1);
  for(int i = 0; i < 1; i++)
   System.out.println(b.get(i));  
}



}
