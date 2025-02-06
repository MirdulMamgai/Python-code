# Write a Python function that takes two lists and returns True if they have at least one
#common member.

def common():
    a=[10,20,30,40]
    b=[50,60,70,10]
    k=0
    for i in a:
        for j in b:
            if i==j:
                k=1
                break
        continue
    if k==1:
        return True
    else:
        return False
    
a=common()
print(a)
                
                
    