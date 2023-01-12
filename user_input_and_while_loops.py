# User inupt and while loops

# ----------------------------------------------------------------------------------------------------------------------
# input() function
# prompt = "Before proceeding, we must verify your age."
# prompt += "\nPlease enter your age: "
# user_age = input(prompt)
#
# # check to see if user input can be converted to int
# try:
#     int(user_age)
# except:
#     print("You did not enter a numeric value!")
#     exit()
#
#
# if int(user_age) >= 21:
#     print(f"At {user_age} you are over the legal drinking age and may proceed.")
# else:
#     print(f"Sorry, as you are only {user_age} you are not of legal drinking age and cannot proceed.")


# input() function exercise
# write a set of statements that requests a users height and checks to see if they are tall enough to ride a roller coaster
# bonus points if you ask the user to enter their height in the format of 'feet, inches' (IE: 4, 10) and both check to ensure the correct format is followed AND then parse that format for use
# ensure to guard against bogus input



# ----------------------------------------------------------------------------------------------------------------------
# while loops + a list

while_prompt = "Please enter your list of pizza toppings one at a time."
while_prompt += "\nWhen completed, type 'bake' to complete the entry.\n"

toppings_list = []

while True:
    topping = input(while_prompt)

    if topping == 'bake':
        print("Baking your pizza with the following toppings:")
        print(toppings_list)
        break
    else:
        toppings_list.append(topping)


# while loop exercise
# write a series of prompts to mimic a movie theater's pricing schema. If a patron is under the age of 3, the ticket is free
# if the patron is between 3 and 12, the ticket is $10, if 12 or older, the price is $15. Seniors age 70+ get a discounted
# rate of $8.
# The code should ask the user their age, tell them the cost per ticket and then ask how many tickets they would like to
# purchase for that age bracket. The user should be prompted to add tickets until the type a keyword such as 'done' or
# 'pay now'. Once the user indicates they are ready to 'pay now', repeat their order and total cost for all tickets.
# hint: a compound data type may help you here... and / or consider the advantage that dictionaries can provide over lists



