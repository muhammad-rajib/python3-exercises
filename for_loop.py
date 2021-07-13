# for loop

"""
for i in range(1, 11):
    print(i, end=' --> ')
"""

lst = ['onion', 'potato', 'cucumber', 'ginger']
size = len(lst)
for i in range(size):
    print(lst[i])

lst = ['onion', 'potato', 'cucumber', 'ginger']
for item in lst:
    print(item)

string = "Bangladesh"
for letter in string:
    print(letter)


for number in range(1, 11):
    if number == 7:
        break
    print(number)

print('\n-------\n')

for number in range(1, 11):
    if number == 7:
        continue
    print(number)

if True:
    pass

# Task 02:
"""
User will give you a number as an input. Your task is 
to print the multiplication of this number from 1 to 10.
(Using for loop).

Input: 2

Output:
----------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""