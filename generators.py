def my_generator():
    for num in range(50):
        yield num ** num        # IF IT IS A MASSIVE AMOUNT OF DATA
                                # yield IS USEFUL
                                # NONE OF THIS IS STORED IN MEMORY
                                # THIS WILL NOT MAKE THE COMPUTER RUN OUT OF RAM

# NOT VERY USEFUL FOR THE BIG NUMBERS :(
my_var_gen = my_generator()
all_numbers = list(my_var_gen)      # IF YOU WANT TO SEE THE NUMBER, CAST IT AS LIST
print(all_numbers)                      # LIST IS SAVING THE DATA

# USEFUL WAY OF SAVING MEMORY
# YOU SHOULDN'T USE my_var_gen HERE... SINCE IT WILL KEEP ITS MEMORY...
for big_num in my_generator():          # THIS DOES NOT SAVE THE DATA
    print(big_num)