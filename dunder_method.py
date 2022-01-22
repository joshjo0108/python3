# DUNDER = DOUBLE UNDERSCORE

class Animal:   
    # DEFAULT VALUE
    animal_type = "Unknown"

    # WHEN YOU ACTIVATE YOUR CLASS, WE NOW NEED TO PASS SOMETHING IN...<PARAMETER> 
    # __init__ IS THE FIRST THING THAT IS RUN
    def __init__(self, fur_color):
        print(f"Fur color is {fur_color}")
    # PASSED IN PARAMETER IS SET IN THIS Animal CLASS
        self.fur_color = fur_color

    #  DEFAULT ACTIONS
    def speak(self):
        raise NotImplementedError       # IT REQUIRES ANOTHER CLASS TO IMPLEMENT THIS

    def eat(self):
        print("I'm eating!!!")

    def chase(self, animal="gazell"):
        print("I am chaing", animal)

    def get_fur_color(self):
        # THIS IS SET FROM __init__ OF THIS CLASS
        print(self.fur_color)

class HouseCat(Animal):
    def __init__(self, fur_color):
        # OVERWRITE DEFAULT VALUE
        super().__init__(fur_color)     # THIS WILL PRINT SOMETHING FROM Animal CLASS
        print("fur color was saved to the class Object")
        # self.animal_type IS CALLED OUTSIDE OF __init__ IN Animal CLASS
        self.animal_type = "House Cat"
        print(self.animal_type)

    def speak(self):
        print("MEOOOOOOOWWWWW")

    def eat(self):
        # GO UP THE HIGHER LEVEL HIERARCHY CLASS <Animal>
        super().eat()
        # PRINT CURRENT CLASS
        print("I'm eating salmon")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")


cat = HouseCat("Pink")
cat.get_fur_color()     # IF HouseCat DOESN'T HAVE def get_fur_color(self),
                        # IT WILL USE Animal CLASS'S def get_fur_color(self) DEFAULT VALUE

