'''
Write a program that prints the variable type of three variables.  
Example: a=2  b=3.0  c=’myName’ 
    Output: 2 is of type <class 'int'>   
            3.0 is of type <class 'float'>   
            myName is of type <class 'str'>
'''

# Declare variables
a = 2
b = 3.0
c = "Hello"

# We use print to display content
# We use print(f"") to combine strings and variables to be displayed together in one print statement
# We use type() to display the variable type instead of the value

print(f"{a} is a variable with the type {type(a)}")
print(f"{b} is a variable with the type {type(b)}")
print(f"{c} is a variable with the type {type(c)}")