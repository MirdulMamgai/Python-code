#Write a program in Python to find if a given number is perfect or not?
n=int(input("Enter a number:"))
temp=n
count=0
for i in range(1,n):
    if(n%i==0):
        count=count+i
    else:
        pass
print(count)
if(count==n):
    print("Perfect number")
else:
    print("Not a perfect number")
