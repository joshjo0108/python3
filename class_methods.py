#  METHOD: FUNCTION INSIDE A CLASS

class Animal:
    # LIKE A DICTIONARY
    this_is_a_property = {
        'key_1': 'Value_1'
    }
    this_list = ['Kane','Josh','Nathan', 'Aaron']

    # DON'T ACCESS OUTSIDE OF THIS CLASS
    _this_is_private_property = "CANNOT ACCESS OUTSIDE OF THIS CLASS"

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    # self INCLUDES this_list + this_is_a_property AND etc.
    # self REFERS TO THE animal CLASS THAT WE ARE WORKING IN
    def this_is_a_method(self):     
        print(self.this_list)

    @property   # DECORATOR
    # WE CAN DITCH () WHEN WE CALL THE FUNCTION
    def get_Josh(self):
        return self.this_list[1]

# ACTIVATE THE CLASS
the_animal = Animal()
the_animal.this_is_a_method()

# get_Josh IS BEING USED AS @property, DON'T REQUIRE get_Josh"()""
josh = the_animal.get_Josh  
print(f"The cutest dog is {josh}")

the_animal2 = Animal()
the_animal2.add_name("Kelly")
print(the_animal.this_list)