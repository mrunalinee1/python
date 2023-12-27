'''Sometimes - we have to accept multiple inputs in a single line.
The way to accept multiple integers in a single line is to use the split and map function.

split function breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
map function converts each input into the defined datatype
The syntax for the same is as follows -'''
a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c
print(a,b,c);