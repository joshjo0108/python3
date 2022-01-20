names = [('name','kalob'),('occupation', 'Coder')]
d = {}
for key, value in names:        # DOES NOT REQUIRE names.items()
    d[key] = value

print(d)

# LIST COMPREHENSION IS STILL MORE POPULAR
# DICTIONARY COMPREHENSIONS
d1 = {key:value for key,value in names}
print(d1)

# THIRD WAY
d3 = dict(names)
print(d3)

