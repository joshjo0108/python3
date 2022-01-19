# tuple vs list : tuple is immutable, where as list is mutable

animals = ["cat", "dog", "Zebra", "aardvaark"]
animals.sort()
animals.append("fish")

# IF YOU NEED A LIST THEY NEVER GETS CHANGED USE TUPLE : RESTRICTED LISTS
foods = ("Pizza", "Orange", "Apple", "Pasta",)      # ENDING WITH ,
# CANNOT DO THIS -> foods.sort()
# TRY foods. <tab>

for food in foods:
    print("The food is ",food)

print(animals)
