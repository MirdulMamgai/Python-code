# WAP to check given no is automorphic or not
#    input n=25
#   output Automorphic
# as 25*25=625
n=int(input("Enter a number"))
temp=n
count=0
sq=n*n
while n!=0:         #
    n=n//10         # for counting digits
    count=count+1   #
div=10*count
if(sq%div==temp):
    print("Automorphic")
else:
    print("Not automorphic")
    
    
