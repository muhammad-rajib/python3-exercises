# Python while Loop
"""

"""

# Task
"""
User will give you a number as an input. Your task is 
to print the square design of this number. (Using while loop)

Input: 5

Output:
-------
    *****
    *****
    *****
    *****
    *****
"""
num = int(input('Enter Your Number: '))
temp = num

while num > 0:
    cnt = temp
    while cnt > 0:
        print('*', end='')
        cnt = cnt - 1
    print()
    num = num - 1