#Write a program in Python to print the Fibonacci series using recursive method.

def fibo(n,a=0,b=1,sum=0):  #n is for the number of time you want to iterate recursive calls
    if n<=0:
        return "" 
    else:
        sum=a+b
        print(sum,end="," if(n>1) else "")
        a=b
        b=sum
        return(fibo(n-1,a,b,sum))
a=0
b=1
print(a,end=",")
print(b,end=",")
a=fibo(5)
print(a)