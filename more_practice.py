class computer(object):
   age = 0;
   name = "";
   programs = [];
   def __init__(self, x,y,*z):
     self.age = x;
     self.name = y;
     for i in range(len(z)):
         self.programs.append(z[i]);
   def update_age(self, int1):
      self.age += int1;
   def change_name(self, y):
      self.name = y;
   def get_programs(self):
      print(self.programs);
c2 = computer(3,"HP", "windows", "skype", "google", "firefox");
c2.get_programs();
a = [];
for i in range(8):
   a.append(int(input("Enter a number:")));
print(a);

def decorator1(func):
   def wrapper():
       func();
   return wrapper;

def print_something():
   print("Im printing something");
decorated_func = decorator1(print_something);
decorated_func();
