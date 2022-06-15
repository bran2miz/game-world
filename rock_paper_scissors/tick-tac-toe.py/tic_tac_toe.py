
class TicTacToe:
  def __init__(self):
    self.board = [' ' for i in range(9)]
    # single list to represent the 3 x 3 tic tac toe board
    self.current_winner = None
    # this will keep track whether there is a current winner of this game
  
  def print_board(self):
    for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
      # choosing which row:
      # ie 
      # 0: 0*3 = 0: (0 + 1 = 1) * 3 (O -> 3)
      # 1: 1*3 = 3: (1 + 1 = 2) * 3 (3 -> 6)
      # 2: 2*3 = 6: (2 + 1 = 3) * 3 (6 -> 9)
      print('| ' + ' | '.join(row) + ' |')
  
  @staticmethod
  # static method because it doesn't pass in a self, it will print which numbers correspond to which spot.
  def print_board_nums():
    # 0 | 1 | 2 etc (tell what number will correspond to what spot)
    number_board = [[str(i) for i in range(j*3, (j + 1) * 3)] for j in range(3)]
    # '| 0 | 1 | 2 |' index j[0]
    # '| 3 | 4 | 5 |' index j[1]
    # '| 6 | 7 | 8 |' index j[2]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')
  
  def available_moves(self):
    moves = []
    for (i, spot) in enumerate(self.board):
    # enumerate creates a lists and assign tuples, that have the index and the value.
    # ie ['x', 'x', 'o'] -> [(0, 'x'), (1, 'x'), (2, 'o')]
      if spot == ' ':
        moves.append(i)
    return moves
    # List Comprehension:
    # return[i for i, spot in enumerate(self.board) if spot == ' ']
  
  def empty_squares(self):
    return ' ' in self.board
  
  def num_empty_squares(self):
    return self.board.count(' ')
  
  def make_move(self, square, letter):
    # if valid move, then make the move (assign square to letter)
    # then return true. if invalid, return false
    if self.board[square] == ' ':
      self.board[square] = letter
      # check if that move was the winning move
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
      game.print_board_nums()
    
    letter= 'X' # starting letter
    # iterate while the game still has empty squares
    # return the winner which ends cyclic loop.

    while game.empty_squares():
      # get the move from the appropriate player
      if letter == 'O':
        square = o_player.get_move(game)
      
      else:
        square = x_player.get_move(game)
      
      if game.make_move(square, letter):
        if print_game:
          print(letter + f' makes a move to square {square}')
          game.print_board()
          print('') # empty line to break text

      if game.current_winner:
        # if there is current winner, the next move wont initiate and the game is over.
        if print_game:
          print(letter + ' wins!')
        return letter


      # after move is made, need alternate letters
      letter = 'O' if letter == 'X' else 'X'
      # if letter == 'X':
      #     letter = 'O'
      # else:
      #     letter= 'X

      if print_game:
        print('It\'s a tie!')

