import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)

  while '-' in word or ' ' in word:
    word = random.choice(words)
  
  return word.upper()
  # make sure to add the upper (uppercase all letters to match with the input)

def hangman():
  word = get_valid_word(words)
  word_letters = set(word) 
  # variable that saves letters in a word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  # keeps track of what the user has already guessed.

  #getting user input so long as the length of the letters is greater than 0
  while len(word_letters) > 0:
    # what letter have the user already used?
    print('You have used these letters: ', ' '.join(used_letters))
    # change the iterable into a string separated by whatever the string is before the .join
    #  ie: ' '.join(['a', 'b', 'cd']) -> 'a b cd'

    # what current word is (ie: W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    # provides the letter only if the input letter has been correctly guessed (as stored used_letters)
    # otherwise will still have a '-' in the string
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
    # if the input letter is recognized as part of the alphabet and hasn't been used yet, add to the set.
      if user_letter in word_letters:
      # if the guessed letter is in the word, remove the input letter from word_letters
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
      print('Oops! You already guessed that letter. Please enter another letter.')
    else:
      print('Invalid letter! Please enter a valid letter')

hangman()