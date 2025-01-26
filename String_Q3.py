#Python program to check a String is palindrome or not.

n=input("Enter a string:")
n1=n.lower()
if(n1==n1[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")