# Write a program to create function calculation() such that 
# it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call

def calculation(x,y):
    sum=x+y
    sub=x-y
    return sum,sub

cal1,cal2=calculation(4,2)
print(f'Addition of two numbers:{cal1}')
print(f'subtraction of two numbers:{cal2}')
      