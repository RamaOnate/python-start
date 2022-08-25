# Strings can be stated with single quotes ' ' or double quotes " "

print('Hello'+" everybody!")

# You can print a string that is assigned as a variable too

greeting = "Hello people :)"
print(greeting)

# Multiline comments can be stated with """ (different lines...) """ or with ''' (different lines...) ''''
# Breaks are inserted according to your formated lines

loginScreen = """
Welcome to the system!

Please enter your credentials:
Username:__________
Password:__________
"""

print(loginScreen)

# Strings are also arrays!

print(loginScreen[1]+'\n')
# loginScreen[1] is not a char! Its just a string with length 1

# You can also loop through a string to print the characters
for i in 'Hola':
    print(i)

# You can obtain the length of a string
print("Length of loginScreen greeting is:", len(loginScreen))

# Additionally you can verify is a substring is incuded in a string
print("Is the word `credentials` located in loginScreen?",
      "credentials" in loginScreen)
print("Is the word `supermarket` not located in loginScreen?",
      "supermarket" not in loginScreen)
