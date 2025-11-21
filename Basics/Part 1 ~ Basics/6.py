'''
Expand the previous program so the real quotient is also printed using two decimal places. 
Example: Input: 10 3 
         integer quotient: 3 
         quotient: 3.3333333333333335 
         remainder: 1 
         quotient (2decimal places): 3.33
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

# % will calculate the quotient but round it to 2 decimals
print(f"Quotiënt rounded:{round(a/b,2)}")

# You can use :.2f instead of the round() function
print(f"Quotiënt rounded:{a/b:.2f}")