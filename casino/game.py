from deposit import *
from choose_nb import *
from money import *
from casino import *
from random import randrange

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

    if (deposit.bank_deposit > 2):
        end = input("\nDo you want to quit the table? [Y/n]\n> ")
        if (end.lower() == "y" or end.lower() == "yes"):
            print("Your earnings are estimated at $" + str(deposit.bank_deposit) + ".")
            print("You leave the casino with your winnings.")
            quit()
    else:
        print("You've got no money left on your bank account.")
        retry = input("Do you want to make another deposit? [Y/n]\n> ")
        if (retry.lower() == "y" or retry.lower() == "yes"):
            deposit()
        elif (retry.lower() == "n" or retry.lower() == "no"):
            print("Okay mate. See you soon!")
            quit()
        else:
            main()

if __name__ == "__game__":
    game()