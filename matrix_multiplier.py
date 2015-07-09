import sys
def matrix_multiplier(list_1, list_2,cols,rows,cols2,rows2):
 sum = 0;
 final_list = [[0 for i in range(rows)]for j in range(cols2)];
 for i in range(rows):
   for j in range(cols2):
     for k in range(cols):
      sum += list_1[i][k] * list_2[k][j];
      #sum += 5;
      print(sum);
     k = 0;
     final_list[j][i] = sum;
     sum = 0;
   j = 0;
 return final_list;



cols = int(input("How many columns do you want in your first matrix?"));
rows = int(input("How many rows do you want in your first matrix?"));
cols2 = int(input("How many columns do you want in your second matrix?"));
rows2 = int(input("How many rows do you want in your second matrix?"));
list1 = [[0 for i in range(cols)] for j in range(rows)]
list2 = [[0 for i in range(cols2)] for j in range(rows2)]
if(cols != rows2):
   print("matrices cannot be muliplied");
   sys.exit(); 
print(list1);
print(list2);
#for(i in range(x*y)):
for i in range(rows):
   for j in range(cols):
      print(i);
      list1[i][j] = int(input("Enter a number here"));

for i in range(rows2):
   for j in range (cols2):
      print(cols2);
      print(rows2);
      list2[i][j] = int(input("Enter a number here:"));
else:
    print(matrix_multiplier(list1, list2, cols,rows,cols2,rows2));



      
