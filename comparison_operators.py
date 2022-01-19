can_code = True

if can_code == True:
    #code
    print("You can code!")
else:
    # do something else
    print("You don't know how to code! yet")



name = input("What is your name? ")
if name.lower() == "jae won jo":
    print("You are Jae Won Jo!!")
    bring_food = "Pizza"
elif name.lower() == "aaron":
    print(f"Welcome {name}")
    bring_food = "Cheese"
else:
    print("You are not Jae Won Jo!")
    bring_food = "Salmon"

print(f"You are eating {bring_food}")

age = input("What is your age? ")
age = int(age)
if age >= 18:
    print("You can vote")
elif age > 8:
    print("You have to go to the school")
else:
    print("You are a baby")