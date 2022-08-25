loginScreen = """
Welcome to the system!

Please enter your credentials:
Username:__________
Password:__________
"""

# Slicing strings can be done with the : sign
print(loginScreen[0:23])

# Slice from the start
print(loginScreen[:23])

# Slice until the end
print(loginScreen[24:])

# Indexes when slicing can be negative
str = 'ello WorldH'
print(str[-6:-1])
