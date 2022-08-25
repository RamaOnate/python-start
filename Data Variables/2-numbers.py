# There are 3 types of numbers:

import random

x = 1      # int
y = 2.8    # float
z = 1j     # complex

print(type(x))
print(type(y))
print(type(z))

# You can also use the number e to indicate power of 10

a = 2e10

print(a)
print(type(a))

# Complex

b = 3 + 5j
c = 5j
d = -5j

print(type(b), type(c), type(d))

# You can cast or convert different types

print(int(y))
print(complex(y))

# Random numbers

print(random.randrange(0, 10))
