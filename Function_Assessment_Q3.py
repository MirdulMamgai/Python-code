# Write a program to create a function show_employee() using the following 
# conditions.
#     It should accept the employee’s name and salary and display both.
#     If the salary is missing in the function call
#      then assign default value 9000 to salary

def show_employee(name,sal=9000):
    print(f"name+:{name}")
    print(f"salary:{sal}")
    
show_employee("Mirdul","2000000")
show_employee("Mirdul")