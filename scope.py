name = "Jae Won Jo"         # THIS IS LIKE A GLOBAL

def myfunc():
    name = "Nathan Jo"     # THIS WILL UPDATE name
    return name            # THIS IS ACCESSED FROM OUTSIDE OF THIS FUNCTION!!!!

outside_of_function = myfunc()

print(outside_of_function)
print(name)                 # DOES NOT CHANGE name, ORIGINAL name

