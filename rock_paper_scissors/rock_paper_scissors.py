import random

def welcomeMessage():
  print("""
*********************************************
**    Welcome to the Rock Paper Scissors   **
**         Start this fun game NOW!        **
**                                         **
**      To quit at any time, type "quit"   **
*********************************************
        """)

def play():
  user = input("Please enter 'r' for Rock, 'p' for paper, and 's' for scissors")
  computer = random.choice(['r','p','s'])

  if user == computer:
    return 'Its a Tie!'

def to_win(player, opponent):
  pass
