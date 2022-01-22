def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper      # RETURN INTERNAL FUNCTION

@my_decorator
def myfunc():
    print("My name is JaeWon")

myfunc()
