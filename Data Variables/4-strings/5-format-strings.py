# We will need to format strings if we want to do certain operations
# For example..

num = 4
mark = "My mark on the final exam was {}"

# We cannot do print(num + str)
# For that we will have to...
print(mark.format(num))

# We can do an unlimited number of arguments
mark1 = 5
mark2 = 6
mark3 = 7
performanceYear1 = "My mark for course 1 was {0}, for course 2 was {1}, for course 3 was {2}"
print(performanceYear1.format(mark1, mark2, mark3))

# We can also select the order of the arguments to be printed
performanceYear2 = "My mark for course 1 was {1}, for course 2 was {2}, for course 3 was {0}"
print(performanceYear2.format(mark1, mark2, mark3))
