#Print all palindrome numbers from 100 to 500

for i in range(100,500):
    temp=i
    rev=0
    while (temp>0):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if (i==rev):
        print(i)
   