class calculus(object):
    def __init__(self, x):
        self.x = x;
    def differentiate(self):
        new_int = 0.0;
        power = "";
        self.new_x = ""; 
        temp = "";
        if(self.x == "sin(x)"):
            return "cos(x)";
        elif(self.x == "cos(x)"):
            return "-sin(x)";
        elif(self.x == "tan(x)"):
            return "sec^2(x)";
        elif(self.x == "cot(x)"):
            return "-csc^2(x)";
        elif(self.x == "sec(x)"):
            return "-sec(x)tan(x)";
        else:
            for i in range(len(self.x)):
                if(self.x[i] == "^"):
                    i += 1;
                    j = i;
                    k = 0;
                    while(j < len(self.x)):
                        power += self.x[j];
                        j += 1;
                    while(self.x[k] != "x"):
                        temp += self.x[k];
                        k+=1;
                    if(temp != ""):
                        self.new_x += str(float(temp) * float(power));
                    else:		    
                        self.new_x += power;
                    self.new_x += "x";
                    new_int = (float(power) - 1.0);
                    if(new_int != 1.0):
                        self.new_x += "^";
                        self.new_x += str(new_int);
        return self.new_x;
        return 0;

	
list1 = input("Enter a function here: ");
calculus1 = calculus(list1);
print(calculus1.differentiate());
