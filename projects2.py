x =set([1,2,3,4,5,6,7,9]);
y = set([1,2,3,4,5,6,7,8]);
list2 = [1,2,3,4];
list5 = list2[::3];
list6 = list2[::-2];
list7 = list2[1:4:2];
print(list5);
print(list6);
print(list7);
print(filter(lambda x: x % 3 == 0,list2));
print(x.symmetric_difference(y));
print(x.difference(y));
print(y.difference(x));
print(x.union(y));
print(x.intersection(y));
list1 = [x**5 for x in range(1,10)];
list3 = [x**3 for x in range(1,10) if x %2 != 0];
print(list1);
print(list3);
names = {"Vista": "bad", "7": "good", "8": "best"};
print(names["Vista"]);
def exception_practice(y):

    print(y);  
   
for i in range(15):
    try:
       exception_practice(list2[i]);
    except IndexError:
       print("this is 4");

#print(exception_practice(y));
def printf(first, second, *all_else):
   print(first);
   print(second);
   print(all_else);
printf(2,4,5,6,7,8,9,9,0); 
"""#@decorator
def times(x,y):
   return x**y;
print(times(3,4));
@times(int,int)
def times_again(x,y):
   return x**2*y;
"""
class practice(object):
   __x = 0;
   _y = 1;
   def __init__(self,a):
      self.a = a;
   def get_x(self):
      return self.__x;

class1 = practice(5);
print(class1._y);
print(class1.get_x());
new_list1 = [2,4,5,6,7,1];
new_list1.sort();
print(new_list1);
print(8|9);
print(7^15);
print(8&5);
print(~(8|5));
print(8 << 2);
print(24 >> 2);
print(23 >> 2);

