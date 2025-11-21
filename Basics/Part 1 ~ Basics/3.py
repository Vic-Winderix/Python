'''
Write a program that reads two integers on one line from the console and prints these on the next 
line using a phrase such as demonstrated below. 

Example: Enter two integers: 17 7
         The integers are 17 and 7
'''

# a,b are two variables that will be declared
# We use map() to apply the int() function on a collection of variables (in this case a,b that get their value from the input) 
# .split() will split the input with a space as devider (you can change this to other deviders like ,.@#)

a,b = map(int, input("Give to integers: ").split())

print(f"The integers are {a} and {b}")

# We can use the type() function to check the variable types
print(f"The integers are {type(a)} and {type(b)}")