from random import randrange

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

  print("You just choosed to bet on the number " + str(choose_nb.number) + ".")

def money():
  money.bet = input("How much money do you want to bet on it?\n> ")
  
  try:
    money.bet = int(money.bet)
    assert money.bet >= 2 and money.bet <= 500000
  except ValueError:
    print("You did not entered any bet.")
    money()
  except AssertionError:
    print("Your bet must be at least $2 and a maximum of $500 000.")
    money()

  print("\nYou bet $" + str(money.bet) + " on the number " + str(choose_nb.number) +".")
  print("\nThe bets are made. May the best win!\n")

def game():
  winning_nb = randrange(50)
  print("The ball stopped at the number " + str(winning_nb) + ".")
  if winning_nb == choose_nb.number:
    money.bet = money.bet * 3
    print("Congratulations! You won $" + str(money.bet) + ".")
  elif (choose_nb.number % 2 == 0) and (winning_nb % 2 == 0):
    money.bet = money.bet * 2
    print("Your bet on " + str(choose_nb.number) + " and the winning number " + str(winning_nb) + " are both even!")
    print("Congrats! You won $" + str(money.bet) + ".")
  elif (choose_nb.number % 3 == 0) and (winning_nb % 3 == 0):
    money.bet = money.bet * 2
    print("Your bet on " + str(choose_nb.number) + " and the winning number " + str(winning_nb) + " are both odd!")
    print("Congrats! You won $" + str(money.bet) + ".")
  else:
    print("Sorry pal. You lost your money..")

def perform():
  choose_nb()
  money()
  game()

perform()