 # Write a Python program to count number of digits in any number
count=0
n=int(input("Enter a number"))
while n!=0:
    n=n//10
    count=count+1
print(count)