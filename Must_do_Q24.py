#Python Program to calculate the power without using POW function
#.(using for loop).

n=int(input("Enter a number:"))
for i in range(n+1):
    c=n**i
print(c)