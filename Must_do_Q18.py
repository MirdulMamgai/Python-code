#Python Program to calculate factorial using recursion.

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
a=fact(6)
print(a)