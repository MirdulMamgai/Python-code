#Write a program in Python to check whether a number is palindrome 
#or not using a recursive method.

def ispalind(temp,rev):
    if temp==0:
        return rev
    rev=(rev*10)+(temp%10)
    return ispalind(temp//10,rev)

temp=int(input("Enter a number:"))
n=temp
a=ispalind(temp,0)
if(a==n):
    print("Palindrome")
else:
    print("Not a palindrome")
