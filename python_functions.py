# Getting familiar with functions

# A function is a named block of code that can be called. A function can accept parameters passed to it.

def build_person(first_name, last_name, age='', dob='', death=''):
    """
    Return a dict of info about the person, first name then last name, optional parameters if specified
    :param first_name: str
    :param last_name: str
    :param age: int
    :param dob: date
    :param death: date - should be the date of death if known
    :return: dict - info about the person
    """
    person = {'first': first_name, 'last': last_name, 'age': age, 'date of birth':dob, 'death': death}
    return person

musician = build_person('john', 'lennon', dob='9/10/1940')
print(musician)

# function exercise - create a function to calculate the age of a person based on their date of birth. Take into account
# if that person has a date of death or not - if so, calculate their age at death, otherwise calculate their current age

