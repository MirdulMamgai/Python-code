# Write a Python program to find sum of all odd numbers between 1 to n.

n=int(input("Enter the end limit:"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        sum=sum+i
    i=i+1
print(f"Sum of all odd number from 1 to {n} is: {sum}")