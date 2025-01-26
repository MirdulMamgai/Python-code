#Write a program in Python to check whether a number is palindrome or not 
#using an iterative method.

n=int(input("Enter a number:"))
temp=n
rev=0
d=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("Number is palindrome")
else:
    print("Not a palindrome number")
        