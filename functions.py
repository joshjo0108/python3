# IN JAVASCRIPT
# function somename() {

# }

# IN PYTHON3
def somename(name=None, food="Pizza"):       # Pizza IS GOING TO BE DEFAULT VALUE
    if name == None:
        name = "Jae Won Jo"

    
    if name != "Dog":
        person_type = "Human"
    else:
        person_type = "Dog"
        return person_type

    print(f"Hello World, {name}, Let's eat some {food}!!")

something = somename("Dog")     # THIS WILL SET something AS "Dog"
print(something)                # Dog
somename("Jae Won Jo", "Oranges")      # DON'T REPEAT YOURSELF (DRY)



def exp(num1, num2):
    total = num1 ** num2
    return total


big_number = exp(33,6)
print(big_number)