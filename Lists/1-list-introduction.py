# Can store multiple items in one variable
# Together with Tuples, Sets and Dictionaries, they are the 4 build in data types in Python.

# Example
toBuy = ["water", "milk", "eggs"]
print(toBuy)

# List items are ordered, changable and allow duplicate!
# They are also indexed starting from [0]

print('Items to buy are', str(len(toBuy)))

# A list can contain different types
toDoList = ["water the plants", 3, True, "this list makes no sense :)"]
print(toDoList)

# Lists are of type list, who would have thought!
print("Tyoe of list is", str(type(toDoList)))

# The contstructor is list()
toSellList = list(("desk", "bike", "chair"))
print(toSellList)
