# Python Function

"""
Syntax of Python Function:
--------------------------
def function_name(parameters):
    statements
    return
"""

def print_my_name(my_name):
    print('My name is', my_name)
    return

name = 'Mohammad Rajib'
print_my_name(name)

# Simple Calculator
def add(a, b, c):
    result = a + b + c
    return result

output = add(10, 20, 20)
print(output)

""" 
FUNCTION PARAMETER OR ARGUMENTS: 
--------------------------------
1. Required Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-length Arguments
"""

# 1. Required Arguments
# Simple Calculator
def add(a, b, c):
    result = a + b + c
    return result

# output = add(1, 2) # Invalid calling
output = add(1, 2, 3) # Valid calling
print(output)


# 2. Keyword Arguments
# Simple Calculator
def add(a, b, c):
    result = a + b + c
    return result

output = add(c=1, a=2, b=3)
print(output)


# 3. Default Arguments
# Simple Calculator
def add(a, b, c=0):
    result = a + b + c
    return result

output = add(1, 2, 7)
print(output)


# 4. Variable-length Arguments
"""
Types:
1. Non-keyword variable-length argument
2. Keyword variable-length argument
"""
# 1. Non-keyword varibale-length argument
# Simple Calculator
def add(*number_list):
    # number_list = (1, 2, 3, 4, 5)
    print(type(number_list))
    result = 0
    for number in number_list:
        # number = 3
        # result = 3 + 3 = 6
        result = result + number
        # result = 6
    return result

output = add(1, 2, 3, 4, 5)
print(output)


# 2. keyword varibale-length argument
# Simple Calculator
def add(**number_list):
    # number_list = {'a':1, 'b':2, ....'e':5}
    print(type(number_list))
    result = 0
    for key in number_list:
        # key = 'a'
        result = result + number_list[key]  # number_list['a']

    return result

output = add(a=1, b=2, c=3, d=4, e=5)
print(output)