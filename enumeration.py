animals = ["Gully", "Rhubarb", "Zephyr", "Henry"]

# VERY HANDY! <- USED VERY OFTEN
for index, animal in enumerate(animals):
    if index %2 == 0:
        continue
    print(f"{index+1}, \t animal")