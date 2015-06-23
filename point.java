import java.util.*;
import java.lang.*;
class point{
      private double x = 0;
      private double y = 0;
   point(double a, double b){
      x = a;
      y = b;
      }
   double get_x(){
	return x;
   }
   double get_y(){
	return y;
   }
public static void main(String [] args){
     System.out.println("Enter an x and a y coordinate here:");
     Scanner s = new Scanner(System.in);
     float a = s.nextFloat();
     float b = s.nextFloat();
     point p1 = new point(a,b);
     grid g1 = new grid(p1);
     double r = Math.sqrt(Math.pow(p1.get_x(),2) + Math.pow(p1.get_y(),2));
     polar_point p2 = new polar_point(3.0,2.0);
     polar_point.set_r(r);
     System.out.println(g1.p.get_x());
     System.out.println(g1.p.get_y());

     System.out.println(p2.r);
     p1 = p2;
     System.out.println(p1.get_y());
     int [] c = null;
}
}
class grid{
point p;
grid(point point1){
p = point1;
}
}
class polar_point extends point{
static double r;
double theta;
polar_point(double x, double y){
super(x,y);

}
static void set_r(double r1){
   r = r1;
}

double get_r(){
   return r;
 
}

}





