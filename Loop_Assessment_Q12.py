#WAP to check given no is palindrome or not. Original =Reverse
#Eg 1221

n=int(input("Enter a number"))
temp=n
rev=0
d=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not a palindrome")
