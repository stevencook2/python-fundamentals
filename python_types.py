# Types in python

# Strings and f-strings

# print('this is a string')

# what are f-strings used for? look this up online before you continue
tt = 34
# print(f'my var tt is {tt}')

# ----------------------------------------------------------------------------------------------------------------------
# Int vs float

x = 2
# print(f'Variable x is {x} and the type of x is {type(x)}')


# to support decimals, use type float

y = 2.44
# print(f'Var y is {y} and is of type {type(y)}')

# multiply an int and a float - what is the result? what is the type of the result?
b = x * y
bb = int(b)
# print(f"the value of the variable b is {b} and it's type is {type(b)}")
# print(f'the val of bb is {bb} and the type is {type(bb)}')

# python also supports complex numbers in the form of (a+bj)
f = 3
h = 8j
i = complex(f+h)
# print(f'var f is {f} and of type {type(f)} \nvar h is {h} and the type is {type(h)}')
# print(i)
# what do you expect the type i to be?
# print(i+"string")
# can you print the conjugate of i using the built in method for a complex type?

# ----------------------------------------------------------------------------------------------------------------------
# List vs tuple
tuple = ("apple", "orange", "mango")

# print(f'the elements in my tuple are {tuple}')
# why does the above statement print all of the elements int the tuple? why not just one?

list_a = ["banana", "grape"]
# print(f'my list is {list_a}')

list_a.append("lemon")

# print(f'my list now contains {list_a}')

# tuple.append("lemon")

# what is the difference between a list and a tuple?
# try appending a new element to the existing tuple as we did with the list - what happens?

# ----------------------------------------------------------------------------------------------------------------------
# Dicts
# when you want to map key value pairs, use a dict

my_fav_things = {}
my_fav_things['fav_fruit'] = 'apple'
print(my_fav_things)
my_fav_things['fav_drink'] = 'wine'
print(f"Ben's fav fruit is: {my_fav_things['fav_fruit']}")
my_fav_things['fav_fruit'] = 'banana'
print(f"Ben's fav fruit is: {my_fav_things['fav_fruit']}")

# my_fav_things.update(fav_song ="jingle bells")
# print(f'my dict is now {my_fav_things}')
# what is the difference between the two options for how to add a new element to a dict?

