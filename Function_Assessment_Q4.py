# Accept a number from the user, create a function isPrime(), 
# which accepts a number from a parameter & check prime or not. 
# If number is prime return True & number else return false & number

def isPrime():
    n=int(input("Enter a number:"))
    p=0
    i=2
    while(i<n):
        if(n%i==0):
            p=1
            break
        i=i+1
    if(p==1):
        return False
    else: 
        return True
    
a=isPrime()
print(a)