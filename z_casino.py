from random import randrange

def welcome():
    welcome = """
    |==============================================================================|
    |============================ Welcome to Z CASINO =============================|
    |==============================================================================|
    |                                                                              |
    | Quick rules:                                                                 |
    |                                                                              |
    | The player bet on a number between 0 and 49 (50 numbers in all).             |
    | By choosing his number, he deposits the amount he wants to bet.              |
    |                                                                              |
    | The roulette consists of 50 boxes naturally ranging from 0 to 49.            |
    | Even numbers are black, odd numbers are red.                                 |
    |                                                                              |
    | The dealer throws the roulette, drops the ball and when the roulette stops,  |
    | note the number of the box in which the ball has stopped.                    |
    | The number on which the ball stopped is, of course, the winning number.      |
    |                                                                              |
    | If the winning number is the one on which the player has bet,                |
    | the dealer gives him 3 times the sum bet.                                    |
    |                                                                              |
    | Otherwise, the dealer looks at whether the number bet by the player          |
    | is the same color as the winning number (if they are both odd or both even). |
    |                                                                              |
    | If so, the dealer gives him 50% of the sum bet.                              |
    | If this is not the case, the player loses his bet.                           |
    |                                                                              |
    |______________________________________________________________________________|
    """
    print(welcome)

def deposit():
    print("Your bank balance is null, you need to make a deposit to be able to play.")
    deposit.bank_deposit = input("How much money do you want to deposit on your account?\n> ")

    try:
        deposit.bank_deposit = int(deposit.bank_deposit)
        assert deposit.bank_deposit >= 2 and deposit.bank_deposit <= 500000
    except ValueError:
        print("Minimum deposit is $2 and maximum is $500 000.\nPlease retry.")
        deposit()
    except AssertionError:
        print("Minimum deposit is $2 and maximum is $500 000.\nPlease retry.")
        deposit()

    print("\nTransaction completed. The balance of your account is now:")
    print("$" + str(deposit.bank_deposit) + ".")

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

def money():
    print("How much money do you want to bet on it?")
    print("Your actual balance of your bank account is: $" + str(deposit.bank_deposit) + ".")
    money.bet = input("(Your bet must be at least $2 and a maximum of $500 000.)\n> ")
    
    try:
        money.bet = float(money.bet)
        assert money.bet >= 2 and money.bet <= deposit.bank_deposit
    except ValueError:
        print("You did not entered any value for your bet.")
        money()
    except AssertionError:
        print("Your bet must be at least $2 and a maximum of $500 000.")
        print("Your actual balance of your bank account is: $" + str(deposit.bank_deposit) + ".\n")
        money()
    
    deposit.bank_deposit = deposit.bank_deposit - money.bet
    print("\nYou bet $" + str(money.bet) + " on the number " + str(choose_nb.number) +".")
    print("Your current balance is now: $" + str(deposit.bank_deposit) + ".\n")
    print("\nThe bets are made. May the best win!\n")

def game():
    winning_nb = randrange(50)
    print("The ball stopped at the number " + str(winning_nb) + ".")
    if winning_nb == choose_nb.number:
        deposit.bank_deposit = deposit.bank_deposit + money.bet * 3
        print("Congratulations! You won $" + str(money.bet) + ".")
    elif (choose_nb.number % 2 == 0) and (winning_nb % 2 == 0):
        deposit.bank_deposit = deposit.bank_deposit + money.bet / 2
        print("Your bet on " + str(choose_nb.number) + " and the winning number " + str(winning_nb) + " are both even!")
        print("\nNot bad! You lost only the half of your bet. You've got $" + str(money.bet / 2) + " left.")
    elif (choose_nb.number % 2 != 0) and (winning_nb % 2 != 0):
        deposit.bank_deposit = deposit.bank_deposit + money.bet / 2
        print("Your bet on " + str(choose_nb.number) + " and the winning number " + str(winning_nb) + " are both odd!")
        print("\nNot bad! You lost only the half of your bet. You've got $" + str(money.bet / 2) + " left.")
    else:
        print("Sorry pal. You lost your money..")

    print("Your current balance is now: $" + str(deposit.bank_deposit) + ".")

    if (deposit.bank_deposit < 2):
        print("You've got no money left on your bank account.")
        retry = input("Do you want to make another deposit? Y/n\n> ")
        if (retry == "y" or retry == "Y" or retry == "yes" or retry == "Yes"):
            deposit()
        elif (retry == "n" or retry == "N" or retry == "no" or retry == "No"):
            print("Okay mate. See you soon!")
            quit()
        else:
            main()

def main():
    deposit.bank_deposit = 0
    welcome()

    if (deposit.bank_deposit <= 2):
        deposit()

    while (deposit.bank_deposit > 2):
        choose_nb()
        money()
        game()

main()