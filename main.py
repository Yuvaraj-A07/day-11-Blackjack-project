############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from replit import clear
from art import logo
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
play_again = True
while(play_again):
  print(logo)
  
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
  def calculate_score(List):
    
  # calculate_score(user_cards)
  # calculate_score(computer_cards)
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if(sum(List) == 21) and len(List)==2:
      return 0
    # else:
    #   return sum(List)
  
  
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if(sum(List)> 21 and 11 in List):
      List.remove(11)
      List.append(1)
    return sum(List)

  def compare(user,com):
    ''' display who is the winner '''
    if(user == com):
      return "Draw"
    elif(com == 0):
      return "You lose"
    elif(user == 0):
      return "You win"
    elif(user>21):
      return "You went over you lose"
    elif(com > 21):
      return "You win"
    else:
      if(user>com):
        return "You lose"
      else:
        return "You win"
  #deal_card(cards)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  #user_cards = []
  #computer_cards = []
  user_cards = []
  computer_cards = []
  is_game_over = False
  for i in range(2):
    user = deal_card()
    user_cards.append(user)
    dealer = deal_card()
    computer_cards.append(dealer)
  # print(user_cards)
  # print(computer_cards)
  # print(sum(user_cards))
  
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user=calculate_score(user_cards)
    com=calculate_score(computer_cards)
    print(f"your cards : {user_cards}, current score = {user}")
    print(f"computer's first card : {computer_cards[0]}")
    if(user == 0 or com == 0 or user>21):
      is_game_over = True
    else:
      
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      another_card = input("Type 'y' to get another card; type 'n' to pass : ")
      if(another_card == 'y'):
        user_cards.append(deal_card())
      else:
        is_game_over = True
        
  
  
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while(com != 0 and com<17):
    computer_cards.append(deal_card())
    com = calculate_score(computer_cards)
  
  #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  print(f"your final cards : {user_cards}, final score = {user}")
  print(f"Computer's final hand : {computer_cards}, final score = {com}")

  print(compare(user,com))
  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  
  restart = input("Do you want to play a game blackJack ? Type 'y' or 'n' : ")
  if(restart == 'y'):
    clear()
    play_again = True
  else:
    play_again = False
