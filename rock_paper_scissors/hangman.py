import random
from random_generator import words
import string

def get_valid_words():
  word = random.choice(words)

  while '-' in word or ' ' in word:
    word = random.choice(words)
  
  return word

def hangman():
  word = get_valid_words(word)
  word_letters = set(word) 
  # variable that saves letters in a word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  # what the user has already guessed.