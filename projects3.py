class sequences(object):
   def __init__(self,x):
      self.x = x;
      self.y = [];
      self.j = 1;
   def fibonacci1(self):
      for i in range(self.x):
          self.y.append(self.j);
          self.j += self.y[i-1];
          print(self.j);
class power_series(sequences):
   def __init__(self,x,inp):
      self.x = x;
      self.y = [];
      self.j = x;
      self.inp = inp;
   def zeno(self):
       for i in range(100):
           self.j /= 2.0;
           self.x += self.j;
       print(self.x);
   def geometric_sum(self):
       initial1 = self.j;
       for i in range(1,100):
           self.x = self.inp ** i;
           self.j += initial1/(self.x);
       print(self.j);
   def fibonacci1(self):
      print(3);
fib1 = int(input("enter the number of terms you want for the fibonacci sequence: "));
s1 = sequences(fib1);
s1.fibonacci1();
print("welcome to the zenos paradox");
starting1 = float(input("Enter the starting number here:"));
s2 = power_series(starting1, 4);
s2.zeno();

s1 = s2;
s1.fibonacci1();
print("Welcome to the infinite sum calculator");
starting = float(input("Enter the first term here: "));
divisor = float(input("Enter a common ratio here: 1/"));

s3 = power_series(starting,divisor);
s3.geometric_sum();
