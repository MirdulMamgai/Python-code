# Create menu driven calculation (add,sub,multiply, divide, mod) using function

def add(x,y):
    sum=x+y
    return sum
def sub(x,y):
    sub=x-y
    return sub
def multiply(x,y):
    mul=x*y
    return mul
def divide(x,y):
    div=x/y
    return div
def mod(x,y):
    mod=x%y
    return mod

print(f"1.To call add function:")
print(f"2.To call subtraction function:")
print(f"3.To call multiplication function:")
print(f"4.To call division function:")
print(f"5.To call mod function:")
ch=int(input("Enter your choice:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
match ch:
    case 1:
        a1=add(a,b)
        print(a1)
    case 2:
        a2=sub(a,b)
        print(a2)
    case 3:
        a3=multiply(a,b)
        print(a3)
    case 4:
        a4=divide(a,b)
        print(a4)
    case 5:
        a5=mod(a,b)
        print(a5)
    case default: print(f"Wrong choice")
