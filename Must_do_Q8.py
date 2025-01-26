#Write a program in Python to find the greatest among three integers.

a=int(input("Enter first number:"))
b=int(input("Enter the second number:"))      
c=int(input("Enter the third number:"))
if(a>b and a>c):
    print(f"{a} is greater then {b},{c}")
elif(b>a and b>c):
    print(f"{b} is greater than {a},{c}")
else:
    print(f"{c} is greater than {a},{b}")