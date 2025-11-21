'''
Write a program that reads two integers and prints the integer quotient, the real quotient and the 
remainder  
Example: Input: 11 4 
         Integer quotient: 2 
         Quotient: 2.75 
         Remainder: 3
'''

# a,b are two variables that will be declared
# We use map() to apply the int() function on a collection of variables (in this case a,b that get their value from the input) 
# .split() will split the input with a space as devider (you can change this to other deviders like ,.@#)

a,b = map(int, input("Give two integers: ").split())

# We use print(f"") to display a cobination of string and variables
# We do calculations in the print statement between {}

# // will calculate the integer quotient 
print(f"Integer quotient: {a // b}")

# / will calculate the quotient 
print(f"Quotient: {a / b}")

# % will calculate the remainder
print(f"Remainder: {a % b}")