#  Write a Python program to find frequency of each digit in a given integer.

n=int(input("Enter a number"))
freq=int(input("Enter the number whose frequency you want to check"))
count=0
while(n>0):
    d=n%10
    if(d==freq):
        count=count+1
    n=n//10
print(count)
