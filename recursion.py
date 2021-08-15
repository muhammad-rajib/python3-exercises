# Recursion in Python

"""
def function1():
    <statements>
         .
         .
    <statements>

    function1()
"""

# factorial(3) --> 3x2x1 = 6
def factorial(num):

    if num == 1:
        return 1
    
    return num * factorial(num-1)

output = factorial(3)
print(output)
