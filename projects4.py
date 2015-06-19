from sys import argv;
def add_1():
   return argv + ["here", "is", "the", "end"];
print(add_1());
print(argv[0]);
outp = open("commands.txt", "w");
outp.write("hello, I an writing to a file using python");
outp.close();
inp = open("commands.txt", "r");
print(inp.readline());

inp.close();
