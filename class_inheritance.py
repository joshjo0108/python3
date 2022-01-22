class Animal:
    fur_color = "Orange",
    
    #  ACTIONS
    def speak(self):
        print("Raaaawwwwrrrr")
    def eat(self):
        pass
    def chase(self):
        pass

class Tiger(Animal):
    #  OVERWRITES ANIMAL CLASS
    # Animal IS BEING SET AS A DEFAULT
    fur_colour = "Black"
    
    def speak(self):
        print("THey're GREATTTTTT!!!")

class HouseCat(Animal):
    #  OVERWRITES ANIMAL CLASS
    # Animal IS BEING SET AS A DEFAULT
    fur_colour = "Pink"

    def speak(self):
        print("MEOOOOOWWWWWWW")

tiger = Tiger()
tiger.speak()

cat = HouseCat()
print(cat.fur_color)