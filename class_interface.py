class Animal:
    fur_color = "Orange",
    
    #  ACTIONS
    def speak(self):
        raise NotImplementedError       # IT REQUIRES ANOTHER CLASS TO IMPLEMENT THIS

    def eat(self):
        raise NotImplementedError

    def chase(self):
        raise NotImplementedError

class HouseCat(Animal):
    def speak(self):
        print("MEOOOOOOOWWWWW")

    def eat(self):
        print("YUMMMMMMMMM")

    def chase(self):
        print("GOOOOOOOOOOO")

cat = HouseCat()
cat.speak()     # IF YOU WANT TO USE IT YOU HAVE TO IMPLEMENTED!