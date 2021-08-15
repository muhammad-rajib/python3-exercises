"""
File: 
    1->Open
    2->Read or Write
    3->Close

** First: Create a test.txt file in your working directory
"""

# Normal way to work with file
f = open("test.txt", "r")
content = f.read()
print(content)
f.close()

# Safe way to work with file
try:
    f = open("test.txt")
    print(f.read())
finally:
    f.close()

# Open file using 'with' keyword
with open("test.txt") as f:
    print(f.read())
    
    # f.seek(0)
    for line in f:
        print(line, end='')
    
    # f.seek(0)
    print(f.readline())

    f.seek(0)
    print(f.readlines())

    # Returns the current file object location.
    # f.seek(10)
    print(f.tell())


# Write in text.txt file
with open("test.txt", "w") as f:
    f.write("Hello Python!")

# Write in append mode
with open("test.txt", "a") as f:
    f.write("Hello Bangladesh!\n")

    # write line by line
    contents = ["This is 1th line\n", "This is 2nd line"]
    f.writelines(contents)
