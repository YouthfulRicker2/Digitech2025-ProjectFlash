import actions

if __name__ == "__main__":
    first_time = input("Is this your first time using the program (y/n)? ")

    while not first_time.lower() == "y" and not first_time.lower() == "n":
        first_time = input("Please enter 'y' or 'n': ")

    if first_time.lower() == "y":
        cont = actions.tutorial()
        while not cont.lower() == "y" and not cont.lower() == "n":
            cont = input("Please enter 'y' or 'n': ")
        if cont.lower() == "y":
            actions.main()
    elif first_time.lower() == "n":
        actions.main()

    print("Baiii!!")