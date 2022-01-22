# try:
#     print("Trying 1/0")
#     total = 1 / 0       # IF THIS FAILS
#                         # IT WILL "NOT" EXECUTE!
#     print("This will not show up")
# except Exception:
#     print("Exception was caught")
#     total = 0

# print(total)

# ERROR HANDLING
num = input("What is number? ")
try:
    num = int(num)      
# GRACEFULLY CATCHING THE ERROR
except Exception:
    num = "Unknown, Please give me a number"     # IF THE INPUT IS NOT A NUMBER!

print(num)
