with open('readme.txt', 'r') as file:
    content = file.read()
    # PYTHON CLOSED THIS FILE

# content VARIABLE IS ACCESSED OUTSIDE OF THE VARIABLE
print("The content is ", content)
