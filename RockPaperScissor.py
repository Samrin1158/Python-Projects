import random
def get_choices():
    player_choice=input("Enter a choice (Rock, Paper ,Scissors):")
    options=["rock","paper","Scisssor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer": computer_choice}
    return choices
# choice=get_choices()
# print(choice)
def check_win(player , computer):
    print(f"You chose {player} ,computer chose  {computer}")
    if player ==computer:
        return "It's a tie!"
    elif player =="rock":
      if computer == "Scissors":
        return"Rock smashes scissors! You win!"
      else:
        return "Paper covers rock! you lose."
    elif player == "paper"  :
      if computer == "rock":
        return "Paper covers rock! You win!"
      else:
       return"Scissors cuts paper! You lose"
    elif player == "scissors" :
      if computer == "paper":
       return " Scissors cuts paper! You win!"
    else:
       return "Rock smashes scissors! You lose."


choices=get_choices()
result =check_win(choices["player"],choices ["computer"])
print(result)