# They represent true or false values

from operator import truediv


print(10 > 9)
print(10 == 9)
print(10 < 9)

# Evaluating variables and values
print('bool("Hello") is ' + str(bool("Hello")))
print('bool(3) is ' + str(bool(3)))
print('bool(0) is ' + str(bool(0)))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# The following values will return false
print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

# Another example of a false is when an object is made of a class with a __len__ function that returns 0 or just false


class myClass():
    def __len__(self):
        return 0


myObj = myClass()
print(bool(myObj))

# Functions can also return a boolean:


def myCorrectIncorrectBoolean():
    return True


print(myCorrectIncorrectBoolean())

# One useful built in function is isInstance(), which helps determine if an object has a certain data type
toCheck = 200
print('Is 200 of type int?', str(isinstance(toCheck, int)))
