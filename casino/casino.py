from welcome import *
from deposit import *
from choose_nb import *
from game import *
from money import *

def main():
    deposit.bank_deposit = 0
    welcome()

    if (deposit.bank_deposit <= 2):
        deposit()

    while (deposit.bank_deposit > 2):
        choose_nb()
        money()
        game()

if __name__ == "__main__":
  main()