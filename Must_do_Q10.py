#Write a program in Python to find the sum of digits of a number using recursion?


def sum(n):
 if(n==0):
     return 0
 else:
     return (n%10+sum(n//10))
     
a=sum(51)
print(a)
        
        