# Python lambda function
"""
Syntax of Lambda Function in Python:
------------------------------------
lambda arguments: expressions
"""

# lambda function
sum = lambda a, b: a + b
print(sum(10, 20))

# Similar of 'sum' lambda function
def sum(a, b):
    return a+b

print((lambda a, b: a-b)(20, 10))


def my_function(func, a, b):
    res = func(a, b)
    print(res)

my_function(lambda a, b: a+b, 100, 50)