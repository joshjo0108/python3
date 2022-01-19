fav_foods = ['Pizza', 'Tacos', 'Salmon']
for food in fav_foods:
    if food == 'Pizza':
        size = input("What size would you like? ")
        print(f"You have ordered {food}, with the size of {size}")
    

food = "Pizza!"
for letter in food:
    print(letter)


person = {
    "name": "Jae WOn Jo",
    "Instagram": "@Coding.for.everybody"
}
for key,value in person.items():
    print(f"{key} : {value}")