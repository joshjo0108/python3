my_answer = input("What is the option? ")
options = ["Rock", "Paper", "Scissor"]

if my_answer in options:
    print(f"The answer is {my_answer}")
else:
    print("Wrong")

key = "name"
person = {
    "name": "Jae Won Jo",
    "profession": "Programmer"
}

if key in person:
    print(f"key is in that person is {person[key]}")