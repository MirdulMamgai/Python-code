#Python Program to find the Average of numbers with explanations.

n=int(input("Enter the range"))
sum=0
for i in range(1,n+1):
    sum=sum+i
avg=sum/n
print(avg)