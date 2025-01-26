#Write a program in Python to check if a given number is prime or not.

n=int(input("Enter a number:"))
flag=0
for i in range (2,n):
    if(n%i==0):
        flag=1
        break
if(flag==0):
   print("Prime Number")
else:
   print("Not a prime number")