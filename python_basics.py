"""
Python Basics:
    1. Statements
    2. Comments
    3. Variables
    4. Keywords & Identifiers
    5. Datatypes
    6. Type Conversion
    7. I/O and Import
    8. Operators
    9. Namespaces
   10. Indentation
"""

# 1. STATEMENTS IN PYTHON
print('I am learning Python Programming Language.')
print("You are welcome in Python.")


# 2. COMMENTS IN PYTHON
# Inline Comment
print('Hello Python.')  # Inline comment

# Block/Multiline Comment
# First comment
# Second comment
# Third comment

"""
Docstring:
----------
Details about your project or class or function
or something else.
* Note: Docstring also a String in Python.
"""
print(__doc__)


# 3. VARIABLES IN PYTHON
a = 10
b = 15
c = a + b
print(a+b)

name = 'Raiyan'
num = 10
num = 12.50
var = True


# 4. KEYWORDS IN PYTHON
"""
Keywords are the reserved words in Python. They are used 
to define the syntax and structure of the python language.
In python, keywords are case sensitive.

Keywords List:
--------------
False	await	    else	    import	    pass
None	break	    except	    in	        raise
True	class	    finally	    is	        return
and	    continue	for	        lambda	    try
as	    def	        from	    nonlocal	while
assert	del	        global	    not	        with
async	elif	    if	        or	        yield
"""


# 5. IDENTIFIERS IN PYTHON
""" 
An identifier is a name given to entities like class, functions, variables, etc. 
It helps to differentiate one entity from another.
"""


# 6. DATA TYPES
"""
1. integer, float, string, boolean - Included in Python 
2. list, tuple, set, dictionary 
- But these are basically included in python data structure.
So we will these in Data Structure Section.
"""
num1 = 10  # int
num2 = 12.50  # float
name = 'Bangladesh'  # str
var = True  # bool
var2 = 2+5j  # Complex

print('Type of', num1, 'is', type(num1))
print('Type of', num2, 'is', type(num2))
print('Type of', name, 'is', type(name))
print('Type of', var, 'is', type(var))
print('Type of', var2, 'is', type(var2))


# 7. TYPE CONVERSION
"""
The process of converting the value of one data type (integer, string, float, etc.)
to another data type is called type conversion. Python has two types of type conversion.

1. Implicit Type Conversion:
----------------------------
=> Python automatically converts one data type to another data type.
   This process doesn't need any user involvement.

2. Explicit Type Conversion:
----------------------------
=> This type of conversion is called typecasting because the user changes the data type of the objects.
   users convert the data type of an object to required data type. 
   We use the predefined functions, like:
   1.int() 2.float() 3.str() etc to perform explicit type conversion.

Additional Type Casting Functions:
--> tuple(), list(), set(), dict()
"""
# Implicit
num1 = 10
num2 = 10.50
print(type(num1))
print(type(num2))

# Explicit
num1 = 10
num2 = "10"
#print(num1+num2)
num2 = int(num2)
print(num1+num2)


# 8. I/O & IMPORT
"""
1. In Python, we have input() function for taking 
inputs from users. 
2. And we use the print() function to output data 
to the standard output device (screen). 
We can also output data to a file
"""
# OUTPUT
print('I love Bangladesh.')
a = 'Python'
print(a)
print('I love %s' % a)
a = 10
print('Integer Number %d' % a)

food1 = 'Biriany'
food2 = 'Kacchi'
print('I love {0} and {1}'.format(food1, food2))
print('I love %s and %s' % (food1, food2))
print(1, 2, 3, sep='*')
print(1, 2, 3, end='#')
print('\n')

# INPUTS IN PYTHON
num = input('Enter a number: ')
print(num)
print(type(num))

# IMPORTS
import math
print(math.pi)

from math import pi
print(pi)

import sys
print(sys.path)


# 9. OPERATORS
"""
1. Arithmetic operators
=> +, -, *, /, %, **, //

2. Comparison operators
=> ==, !=, >, <, >=, <=

3. Logical operators
=> and, or, not

4. Assignment operators
=> =, +=, -=, *=, /=

5. Membership operators
=> in, not in

6. Identity operators
=> is, is not

7. Bitwise Operator
=> AND &, OR |, NOT ~
   XOR ^, left shift <<
   right shift >>
"""
a = 5
b = 5
result = a*b
print(result)


# 10. NAMESPACES
"""
A namespace is a collection of names. A namespace containing all the built-in names is created 
when we start the Python interpreter and exists as long as the interpreter runs.
"""
a = 10  # global namespace

def outer_function():
    b = 20  # b is local namespace of outer_function()
    def inner_func():
        c = 30  # c is the nested local namespace of inner_function()


# 11. INDENTATION
"""
Python does not have any curly braces for defining a block of codes.
Instead of curly braces Python use indentation concept for defining block of codes.
For indentation in python we use Tab or Spaces But not both.
"""

if (a==b):
    print('Hello')  # under if condition 
    print('Hello')  # under if condition
print('Hi')