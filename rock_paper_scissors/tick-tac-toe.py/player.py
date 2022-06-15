import math
import random

class Player:
  def __init__(self, letter):
    # letter is x or  o
    self.letter = letter
  
  def get_move(self, game):
    pass

class RandomComputerPlayer(Player):

  def __init__(self, letter):
    # initalize the superclass
    super().__init__(letter)
    # call the initialization in the super class which is the player
  
  def get_move(self, game):
    square = random.choice(game.available_moves())
    return square

class HumanPlayer(Player):

  def __init__(self, letter):
    super().__init__(letter)
  
  def get_move(self, game):
    valid_square = False
    value = None

    while not valid_square:
      square = input(self.letter + '\'s turn. Input move (0-9):')
      # check that it is a correct value
      # try to cast it to an integer
      # invalid error if its not an integer
      # if the spot is not available, it will also raise error
      try:
        value = int(square)
        if value not in game.available_moves():
          raise ValueError
        valid_square = True # this would happen if is a valid square
      except ValueError:
        print('Invalid square. Try again!')
    return value