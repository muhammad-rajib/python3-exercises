"""
The if…elif…else statement is used in Python for decision making.

"""
# Python if Statement Sytax:
"""
if expressions:
    statements
"""
value = True
if value:
    print("Yes, It's True.")

# Python if..else Statement Syntax:
"""
if expressions:
    statements
else:
    statements
"""
value = False
if value:
    print("Yes, It's True.")
else:
    print("No, It's False.")

# Python if..elif..else Statement Syntax:
"""
if expressions:
    statements of if
elif expressions:
    statements of elif
else:
    statements of else
""" 
number = int(input("Enter Your Number: "))
if number == 0:
    print("It's Zero.")
elif number > 0:
    print("It's Positive Number.")
else:
    print("It's Negative Number.")

# Nested if
number = int(input('Enter Your Number: '))
if number > 0 and number < 50:
    if number % 2 == 0:
        print('Number is less than 50 and YES!')
    else:
        print('Number is less than 50 and NO!')
else:
    if number % 2 == 0:
        print('Number is greater than is 50 and YES!')
    else:
        print('Number is greater than 50 and NO!')


# Task:
"""
User will give you a characte as an input. Your task is to help him/her
to find that the given character is vowel or consonent? If vowel then 
print('Vowel') or for consonent print('Consonent') and if not both then
print('Nothing') 
"""
char = input('Please enter your character: ')
if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
    if char in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('Consonent')
else:
    print('Nothing')
