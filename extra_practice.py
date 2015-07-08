y = [i ** 4 for i in range(16) if i % 4 != 0];
print(y);
class append_to_x(object):
    x = [];
    a = 0;
    def __init__(self, a):
        self.a = a;
        self.x.append(self.a);
    def add_on(self,b):
        self.x.append(b);
 
x1 = append_to_x(5);
x1.add_on(5);
print(x1.x);
list1 = [1,2,3,4,5,6];
list2 = list1[::-3];
print(list2);
s = "I have finally learned to program in python";
t = s[::-1];
print(t);
print([i for i in y if i %2 == 0]);
print([i ** 2 for i in y]);
print([i for i in y if(i**2) % 2  == 0]);
a1 = {"first": 1, "second": 2, "third": 3, "fourth": 4};
print(a1["first"]);
print(filter(lambda x:x % 2, list1 ));






