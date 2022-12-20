# Operators

# Standard arithmetic operators (+, -, /, *, %, **, //)

a = 33
b = 4
c = "7"

# Add a and b together, print the output
add1 = a + b
print(add1)

# Add a and c together - what do you need to do to make this work? print the output
add2 = a + int(c)
print(add2)

# Subtract a from b, print the output
sub = b - a
print(sub)

# create a new variable z that is the modulus of a and b - print the result
z = a % b
print(z)

# Print the result of raising a to the power of b
exp = a**b
print(exp)

# What is the difference between the standard divide arithmetic operator and the floor division operator (//)?
# Print both and determine the difference
div = a / b
div2 = a // b


print(div,div2)
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
print('subtracting 4 from a')
a -= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a - 4')


# *=
print('multiplying 4 and a')
a *= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a * 4')
# /=
print('dividing a and 4')
a /= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a / 4')
# %=
print('getting modulus of a and 4')
a %= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a % 4')
# //=
print('dividing a and 4 and getting only integer')
a //= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a / 4')
# **=
print('taking a to the power of 4')
a **= 4
print(f'the new value for a is {a}')
print(f'the equivalent long form would have been a = a ** 4')
# other operators include &=, |=, ^=, >>= and <<=
# try them out later

# ----------------------------------------------------------------------------------------------------------------------
# Comparison operators

# how do we compare values?

if a == b:
    print(f'variable a which is set to {a} is equivalent to b which is set to {b}')

# try printing the statement a == b what result would you expect to receive? False Boolean
# can you add equivalent if statements to evaluate if a is greater than or less than b, printing the result?
if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a and b are equivalent')
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

if (h == i) or (j == k):
    print('One of these are true')

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

if z not in my_list:
    print(f'my_list does not contain the number {z}')
else:
    print(f'my_list contains the number {z}')

# ----------------------------------------------------------------------------------------------------------------------
# Bitwise operators

# you can compare binary numbers in python using the bitwise operators
