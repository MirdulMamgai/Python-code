#Write a program in Python to check whether an integer is an Armstrong number
# or not.

n=int(input("Enter a number:"))
temp=n
dig=0
while(n>0):
    d=n%10
    dig=dig+d**3
    n=n//10
if (dig==temp):
    print("Armstrong number")
else:
    print("Not a armstrong number")