def choose_nb():
    choose_nb.number = input("\nPlease choose a number between 0 et 49:\n> ")
    
    try:
        choose_nb.number = int(choose_nb.number)
        assert choose_nb.number >= 0 and choose_nb.number <= 49
    except ValueError:
        print("You did not enter a number.")
        choose_nb()
    except AssertionError:
        print("The number entered is less than 0 or superior to 49, please retry.")
        choose_nb()

    print("You just choosed to bet on the number " + str(choose_nb.number) + ".\n")

if __name__ == "__choose_nb__":
    choose_nb()