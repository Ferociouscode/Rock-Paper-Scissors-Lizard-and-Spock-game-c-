import random

print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
print("-" * 48)
user = input("Add your username => ")
tie = 0
user_win = 0
computer_win = 0
rounds = 1

while user_win < 3 and computer_win < 3:
  print("*" * 30)
  print("ROUND", rounds)
  

  user_choice = input("Choose your weapon => ").lower()
  while user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
    print("Invalid choice, please chose Rock, Paper, Scissors, Lizard or Spock")
    user_choice = input("Choose your weapon =>").lower()

  computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])

  
  outcomes = {
    "rock" : {"scissors" : "crushes", "lizard" : "crushes"},
    "paper" : {"rock" : "covers", "spock" : "disproves"},
    "scissors" : {"paper" : "cuts", "lizard" : "decapitates"},
    "lizard" : {"paper" : "eats", "spock" : "poisons"},
    "spock" : {"rock" : "vaporizes", "scissors" : "smash"}
  }
  if user_choice == computer_choice:
    print("Tie! Both players chose", user_choice)
    tie += 1
  elif computer_choice in outcomes[user_choice]:
     print(f"{user_choice.capitalize()} {outcomes[user_choice][computer_choice]} {computer_choice.capitalize()} {user} wins!")
     user_win += 1
  else:
    print(f"{computer_choice.capitalize()} {outcomes[computer_choice][user_choice]} {user_choice.capitalize()} {user} loses!")
    computer_win += 1
  print(f"Score: {user} {user_win} - {computer_win} Computer")
  rounds += 1

print("Thanks for playing!")
if user_win > computer_win:
  print(f"{user} wins the game!")
else:
  print("Computer wins the game!")
