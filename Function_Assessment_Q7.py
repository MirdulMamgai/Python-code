# Create a function that accept student data, 
# calculate the total & percentage, return total & percentage

def total(a,b,c,d,e):
    sum=a+b+c+d+e
    return sum
def percentage(a,b,c,d,e,total=500):
    sum=a+b+c+d+e
    per=sum/total*100
    return per

a=int(input("Input 1st numbers:"))
b=int(input("Input 2nd numbers:"))
c=int(input("Input 3rd numbers:"))
d=int(input("Input 4th numbers:"))
e=int(input("Input 5th numbers:"))

n1=total(a,b,c,d,e)
print(n1)
n2=percentage(a,b,c,d,e)
print(n2)
    
    
    