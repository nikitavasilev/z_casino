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

if __name__ == "__deposit__":
    deposit()