# Create a function to accept a number & return its factorial

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

no=int(input("Enter a number:"))
x=fact(no)
print(f"The factorial of num{no} is: {x}")


        
    