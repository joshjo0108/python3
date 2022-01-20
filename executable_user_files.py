filename = input("what is the filename?")
content = input("Enter the content: ")

with open('filename', 'w') as file:
    file.write(content)

open_file = input("Would you like to open the file?(y/n): ")
open_file = open_file.lower()
if open_file in ['y','n']:
    if open_file == 'y':
        with open('filename', 'r') as file:
            file_content = file.read()

print(file_content)