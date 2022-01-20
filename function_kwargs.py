# KEY WORD ARGS
# COMES BACK AS DICTIONARY LIKE FORM
'''
def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("Your age is ", kwargs.get("age"))

# THROW IT INTO A DICTIONARY FORM!!!
person(name="Jacob", age=27, brain="Huge")
'''

def order_pizza(name, address, **topppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 18.00
    for key, value in topppings.items():
        print(key, value)       # ex) key = jalapenos , value = True
        if value == True:
            price = price + 2.00
    print(f"The total price is {price} dollars")
    return price

order_pizza("Amanda", "Canada", jalapenos=False, extra_cheese=True, ham=True, jam=False)