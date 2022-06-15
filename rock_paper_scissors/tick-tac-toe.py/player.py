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
    pass