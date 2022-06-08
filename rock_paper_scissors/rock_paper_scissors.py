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
  print('''Please enter 'r' for Rock, 'p' for paper, and 's' for scissors''')
  user = input("> ")
  computer = random.choice(['r','p','s'])

  if user == computer:
    return 'It\'s a Tie!'
  
  if is_win(user, computer):
    return 'Congratulations! You Won the Game!'
  
  return 'Shucks, you lost!'

def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True
print(welcomeMessage())
print(play())

# if __name__ == "__main__":
#   welcomeMessage()
#   play()
