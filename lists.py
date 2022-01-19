lst = ["String", 1, 3.14, ["A new item"], "Jae Won Jo"]       # LIST WITHIN LISTS FOR DATA SCIENCE

lst.append("Aaron")
lst.remove("String")

name = lst.pop()
print(name)

for item in lst:
    print("The item is", type(item), ": ", item)
