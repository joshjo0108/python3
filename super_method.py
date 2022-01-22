class Animal:
    fur_color = "Orange",
    
    #  ACTIONS
    def speak(self):
        raise NotImplementedError       # IT REQUIRES ANOTHER CLASS TO IMPLEMENT THIS

    def eat(self):
        print("I'm eating!!!")

    def chase(self, animal="gazell"):
        print("I am chaing", animal)

class HouseCat(Animal):
    fur_color = "Pink"

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


cat = HouseCat()
cat.eat()     # IF YOU WANT TO USE IT YOU HAVE TO IMPLEMENTED!
cat.chase("Mouse")

# OVERWRITE fur_color
cat.fur_color = "Grey"
print(cat.fur_color)