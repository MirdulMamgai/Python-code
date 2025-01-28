#Write a program in Python to multiply two integers without using multiply operators?

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a
for i in range(1,b):
    sum=sum+a
print(sum)
    
