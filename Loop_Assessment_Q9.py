#Find all prime number between 400 to 300;
n=400
count=0
while(n<=400 and n>=300):
    for i in range(2,n):
          if(n%i==0):
            count=1
            break
          else:
              count=0
          # break
            #pass
    if(count==0):        
        print(n)
    n=n-1
       
        
        
