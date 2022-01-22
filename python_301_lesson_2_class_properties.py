class Animal:
    # LIKE A DICTIONARY
    this_is_a_property = {
        'key_1': 'Value_1'
    }
    this_list = ['Kane','Josh','Nathan', 'Aaron']

    # DON'T ACCESS OUTSIDE OF THIS CLASS
    _this_is_private_property = "CANNOT ACCESS OUTSIDE OF THIS CLASS"
# ACTIVATE THE CLASS
the_animal = Animal()

# PRINT THE PROPERTY <DICTIONARY>
print(the_animal.this_is_a_property['key_1'])
# PRINT THE <LIST>
print(the_animal.this_list[0])
print(the_animal._this_is_private_property)