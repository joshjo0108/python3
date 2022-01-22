num = input("Enter a first number: ")
num2 = input("Enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print(f"{num} & {num2} are not a vaild number")
except ZeroDivisionError:
    print("Numbers could not be divided by ZERO")
except Exception as e:
    print("Exception was caught")
    print(type(e))

print(total)
