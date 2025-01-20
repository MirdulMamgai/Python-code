# Create a login function, that accept username & password, 
# if username is ‘admin’ & password is ‘admin@123’ then return true, 
# else return false

def login(name,password):
    if (name=="admin" and password=="admin@123"):
        return True
    else:
        return False
    
n=input("Enter your name:")
p=input("Enter your password:")
c=login(n,p)
print(c)

    
    