# Global variables are created outside of the context of a function

from re import X


x = 'good morning'


def myFunc():
    print('I hope everyone has a', x)


myFunc()


def myFuncLocal():
    x = 'bad morning'
    print('I hope everyone has a', x)

# The concept of local and global variables also applies to python.


myFuncLocal()

# If you use global keyword, the variable belongs to a global scope
# The global keyword can change a global variable inside a function


def myFunc2():
    global x
    x = "fantastic"
    myFunc()


myFunc2()
