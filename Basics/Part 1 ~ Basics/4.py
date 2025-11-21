'''
Write a program that reads two integers on one line from the console and prints the sum and 
product on the next line
'''

# a,b are two variables that will be declared
# We use map() to apply the int() function on a collection of variables (in this case a,b that get their value from the input) 
# .split() will split the input with a space as devider (you can change this to other deviders like ,.@#)

a,b = map(int, input("Give two integers: ").split())

# We use print(f"") to display a cobination of string and variables
# We do the product and sum in the print statement between {}

print(f"Sum: {a + b}")
print(f"Product: {a * b}")