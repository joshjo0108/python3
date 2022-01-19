person = {
    "key": "value",
    "name": "Jae WOn Jo",
    "age": 12
}
# PRINTING SPECIFIC VALUE FOR THAT CERTAIN KEY
print(person['name'])

# ADDING KEY AND VALUE TO THE DICTIONARY
person['instagram'] = "@Jae Won Jo"
print(person)

# DELETING A KEY & VALUE
del person['key']
print(person)