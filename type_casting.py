age = input("What is your age? ")           # AS A STRING
print(type(age))

age = int(age)          # CASTING TO INTEGER FROM STRING
print(type(age))

grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
# CASTING LISTS TO SETS
grocery_list = set(grocery_list)        # UNIQUE + IN ANY ORDER
print(grocery_list)