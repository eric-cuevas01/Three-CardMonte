# Eric Cuevas,
# 26 January 2023
# A betting game called Three Card Monte where a player guess a specific card's location in a deck of three; two kings and a queen

import random
import check_input


def main():
  """Generates a randomized location for the queen's card in the deck. The player's money is set to $100 and the game is live. It will end once the player runs out of money or decides to quit."""

  money = 100
  # User starts with $100 as betting money
  play_again = True
  while play_again:

    while money > 0:
      queen_location = random.randint(1, 3)
      # Randomly hides the queen's card in one of three randomized places

      # Prompt the user for their betting amount
      bet = int(input("Enter your bet (you have $" + str(money) + "): "))
      if bet > money:
        print("Invalid bet, you do not have enough money.")

      print()
      print("+-----+ +-----+ +-----+")
      print("|     | |     | |     |")
      print("|  1  | |  2  | |  3  |")
      print("|     | |     | |     |")
      print("+-----+ +-----+ +-----+")
      print()
      
      guess = int(input("Enter your guess (1, 2, or 3): "))
      # Prompt the user for their guess, which is limited to choices 1, 2, or 3
      if guess < 1 or guess > 3:
        print("Invalid guess, please enter a number between 1 and 3.")
        continue

      if guess == queen_location:
        # Check if the user's guess is correct
        print("Congratulations! You won $" + str(bet) + "!")
        money += bet

        print()
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        if queen_location == 1:
          print("|  Q  | |  K  | |  K  |")
        elif queen_location == 2:
          print("|  K  | |  Q  | |  K  |")
        else:
          print("|  K  | |  K  | |  Q  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        print()
        
      else:
        print("That's unlucky, the queen was under card " +
              str(queen_location) + ".")
        
        print()
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        if queen_location == 1:
          print("|  Q  | |  K  | |  K  |")
        elif queen_location == 2:
          print("|  K  | |  Q  | |  K  |")
        else:
          print("|  K  | |  K  | |  Q  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        print()
        
        money -= bet

      if money <= 0:
        play_again = False
        print("You have run out of money. It's game over.")
        # Check if the user has run out of money
        break
      else:
        play_again = check_input.get_yes_no(
          "Would you like to play again? (y/n): ")
        # Ask if the user wants to play again or quit the game
        break


main()
