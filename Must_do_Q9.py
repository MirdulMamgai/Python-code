#Write a program in Python to check if a number is binary?

n=int(input("Enter any number"))
d=2
while(n>0):
    d=n%10    
    n=n//10   
    if(d!=0 and d!=1):  
        break
if(d==0 or d==1):
    print("Binary")
else:
    print("Not a binary")
    
    