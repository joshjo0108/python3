# NEW FILE WILL APPEAR
# WRITE FILES USING USER INPUTS!

with open('writing_files.txt', 'w') as file:
    # IF IT IS RUN 2 TIMES IT WILL OVERWRITE THE WHOLE FILE
    file.write("\n\tHello from python 201")

# APPENDS THE FILE!
with open('writing_files.txt', 'a') as file:
    # IF IT IS RUN 2 TIMES IT WILL OVERWRITE THE WHOLE FILE
    file.write("\n\tHello from python 201!!!")
    file.write("\n\tTHIS IS A TABBED")