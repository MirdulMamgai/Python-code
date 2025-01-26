#Write a program in Python to swap two numbers using a third variable?

def swap (a,b,temp):
  temp=a
  a=b
  b=temp
  print(f"Value of a is {a} and value of b is {b}")
  
swap(10,20,0)