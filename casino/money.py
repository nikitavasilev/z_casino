from deposit import *
from choose_nb import *

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

if __name__ == "__money__":
    money()