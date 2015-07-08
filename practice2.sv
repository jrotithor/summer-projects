module Top2(input A, B, C, D, 
input [1:0] E,
input [1:0] F,
output op3, op_4, 
output [1:0] op_5
);
adder a1(.A(A), .B(B), .out(op1));
adder a2(.A(C), .B(D), .out(op2));

bits b1(.A(A), .B(B), .C(C), .D(D), .G(op4));
//assign op3 = op1 ^ op2;
new_practice(.in_1(E), .in_2(F), .out1(op5));
endmodule
 module adder(input A, B,
output out
);
assign out = A + B;


endmodule

module new_practice(input [1:0] in_1, input [1:0] in_2, 
output [1:0] out1);
  typedef struct{
  logic [1:0] A;
  logic [1:0] B;
  
  }obj_1;
  typedef enum{
  
  x,
  y,    
  z
  
  
  
  }enum1; 
  enum1 e1 = x;
  
   obj_1 o_1;
   assign o_1.A = in_1; 
   assign o_1.B = in_2;
   assign out1 = o_1.A & o_1.B;     
    

endmodule

 module bits(input  A, input B, input C, input D,
output G);
logic E;
logic F; 

assign E = A & B;
assign F = C & D;
assign G = E | F;


endmodule

