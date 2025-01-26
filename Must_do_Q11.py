#Write a program in Python to swap two numbers without using a third variable?

def swap (a,b):
  a=a+b
  b=a-b
  a=a-b
  print(f"Value of a is {a} and value of b is {b}")
  
swap(10,20)