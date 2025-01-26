#Python Program to find Smallest number among three.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a<b and a<c):
    print(f"{a} is smaller than {b},{c}")
elif(b<a and b<c):
    print(f"{b} is smaller than {a},{c}")
else:
    print(f"{c} is smaller than {a},{b}")


    