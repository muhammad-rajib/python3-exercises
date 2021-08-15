"""
        EXCEPTIONS HANDLING
       =====================
       
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. 
In general, when a Python script encounters errors or a situation that it cannot cope with, it raises an exception. 

Important Standard Exceptions:
------------------------------
-> FileNotFoundError
-> ImportError
-> IndentationError
-> IndexError
-> KeyboardInterrupt
-> KeyError
-> NameError
-> OSError
-> RuntimeError
-> StopIteration
-> SyntaxError
-> SystemError
-> TabError
-> TypeError
-> UnboundLocalError
-> ValueError
-> ZeroDivisionError
"""

# Examples of some exceptions
"""
# FileNotFoundError
with open("test.txt") as f:
    print(f.read())

# NameError
with open("test.txt") as f:
    content = f.read()
    print(contents)

# ValueError
with open("test.txt"):
    print(f.read())
"""

# try...except clause example & Exception handling
try:
    with open("test1.txt") as data_file:
        content = data_file.read()
        print(content)
except:
    print('Error.')

# Handle FileNotFoundError Exception
try:
    with open("test1.txt") as data_file:
        content = data_file.read()
        print(content)
except FileNotFoundError:
    print('File does not exist.')

# Handle Exceptions with 'Built in exception messages'
try:
    with open("test1.txt") as data_file:
        content = data_file.read()
        print(content)
except FileNotFoundError as e:
    print(e)
    print('File does not exist.')

# Handle multiple exceptions
try:
    with open("test.txt") as data_file:
        content = data_file.read()
        print(contents)
except FileNotFoundError:
    print('File does not exist.')
except NameError:
    print('Unexcepted error!')

# handle multiple exceptions using a single except clause
try:
    with open("test.txt") as data_file:
        content = data_file.read()
        print(contents)
except (FileNotFoundError, NameError):
    print('Follow Instructions!')

# try...except...else
try:
    a = 10
    b = 15
    print(a+b)
except ValueError as e:
    print(e)
else:
    print('There is no exception.')

# try....except.....finally
try:
    with open("test.txt") as data_file:
        content = data_file.read()
        print(contents)
except FileNotFoundError:
    print('File does not exist.')
except NameError:
    print('Unexcepted error!')
finally:
    print('Completed!')
