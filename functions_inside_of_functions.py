def thing1(name):
    print("Welcome to thing 1", name)

    def thing2():   # DOES NOT REQUIRE A PARAMETER
        print("Welcome to thing 2", name)       # BUT STILL RUNS THIS name FROM def thing1(name)
    thing2()

thing1("Josh")