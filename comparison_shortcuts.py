something = "Hello"

# IF something A STRING
if something:           # IF something IS NOT NONE (EMPTY)
    print(f"THIS IS NOT NONE, IT IS {type(something)}")
else:                   # IF something = None
    print("This is a empty string!")