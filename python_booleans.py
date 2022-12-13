# Often you will need to know if something is logically true or false (is my variable x equivalent to my variable y)
# You'll generally use these logical evaluations in combination with if statements or other similar operators
# try/catch statements or switcher may also be useful here but we'll avoid these concepts for now

x = 3
y = 4
z = 'not_a_number'
j = "3" # a number but it's a string..

if x < y:
    print(f'the variable x is less than the variable y')
elif x > y:
    print(f'the variable x is greater than the variable y')
else:
    print(f'the variables x and y are equal to one another')

# what if we try to use a comparison operator with an integer and a string?
# if x == z:
#     print(f'x and z are equivalent')

# will this work? why or why not?
# how does python handle type conversion?
if x == int(j):
    print(f'x and j are equivalent')
else:
    print('x and j are NOT equivalent')

print(type(j))

# how can we make the above statement work?
