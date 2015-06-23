import java.util.*;
import java.io.*;
import java.lang.Math;
class sequences{
   double start = 0;
   double start2 = 0;
   double start3 = 0;
   sequences(double x,double y){
    start = x;

   start2 = x;
   start3 = y;
   }
   double doubler(){
    for(int i = 0; i < 100; i++)
	this.start +=(this.start2/Math.pow(2,(i+1)));
    return this.start;
   }
   double expander(){

    for(int i = 0; i < 100; i++)
	this.start +=(this.start2/Math.pow(this.start3,(i+1)));
    return this.start;
   }


public static void main(String [] args){        
   System.out.println("Enter a number here to infinitly halved and summed:");
   Scanner s = new Scanner(System.in);
   int x = s.nextInt();
   int y = s.nextInt();
   sequences s1 = new sequences(x,y);
   System.out.println(s1.doubler());
   sequences s2 = new sequences(x,y);
   System.out.println(s2.expander());
  series s3 = new series(3.0, 2.0);
  s3.set_ratio(5.0);
  System.out.println(s3.doubler());

}

}

class series{
 double start = 0;
 double start2 = 0;
 double ratio = 0;
 
series(double a, double b){
 start = a;
 start2 = b;

 }
void set_ratio(double c){
ratio = c;
}
double doubler(){
  for(int i = 0; i < 150; i++){
     this.start += this.start2/Math.pow(ratio, (i+1));
  }
 return this.start;
}


}



