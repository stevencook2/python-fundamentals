# Operators

# Standard arithmetic operators (+, -, /, *, %, **, //)

a = 33
b = 4
c = "7"

# Add a and b together, print the output


# Add a and c together - what do you need to do to make this work? print the output


# Subtract a from b, print the output


# create a new variable z that is the modulus of a and b - print the result


# Print the result of raising a to the power of b


# What is the difference between the standard divide arithmetic operator and the floor division operator (//)?
# Print both and determine the difference

# ----------------------------------------------------------------------------------------------------------------------
# Assignment operators

# by now you know how to use the standard = operator to assign a variable a value
# can you determine the logical operation of the following operators? What is the equivalent long form?

print(f'the original value for a is {a}')

# +=
print('adding 4 to a')
a += 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a + 4')

# -=

# *=

# /=

# %=

# //=

# **=

# other operators include &=, |=, ^=, >>= and <<=
# try them out later

# ----------------------------------------------------------------------------------------------------------------------
# Comparison operators

# how do we compare values?

if a == b:
    print(f'variable a which is set to {a} is equivalent to b which is set to {b}')

# try printing the statement a == b what result would you expect to receive?
# can you add equivalent if statements to evaluate if a is greater than or less than b, printing the result?

# ----------------------------------------------------------------------------------------------------------------------
# Logical operators

# how do we add a logical function to take an action only if two statements are both true?

h = 1
i = 1
j = 2
k = 2

if (h == i) and (j == k):
    print(f'both statements are true')
else:
    print(f'both statements are not true')

# can you write a similar statement to take action if either of the statements are true?

# ----------------------------------------------------------------------------------------------------------------------
# Membership

# We can determine if an element exists in an iterable by using the 'in' operator

my_list = [2, 5, 7, 8, 9]
print(my_list)
z = 5
if z in my_list:
    print(f'my_list contains the number {z}')
else:
    print(f'my_list does not contain the number {z}')

# write a similar if / else statement to determine if a number does NOT exist within the list, printing the
# appropriate messages

# ----------------------------------------------------------------------------------------------------------------------
# Bitwise operators

# you can compare binary numbers in python using the bitwise operators
