# WAP to show the use of break statement ( in for loop)

n=int(input("Enter the range for first even number:"))
for i in range(n):
    if(i%2==0 and i>0):
        print(f"{i} is the first event number")
        break
print("Loop terminated")
    