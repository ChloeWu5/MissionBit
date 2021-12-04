import random

#project hangman

#create list of words
#pick a random word from that list
#print underscores per letter in word
#at all times: show amount of attempts left
#if input is true, underscore(s) will change into letter
#if word is true, change all underscores to word
#if trys run out, print "you lose!"
#if letter not equal to letters in word, trys -1, print "try again!"
#if word == correct, print "you win!"

words = [
    "barnacle", "automatic", "excessive", "conscious", "willpower", "diplomat",
    "computing", "enigmatic", "telescope"
]

# Hello, tomas here!

word = random.choice(words)
print(word)
lives = 6
guessed = []

def print_word(word, guessed):
  output_word = ''
  for letter in word:
    if letter in guessed:
      output_word += letter
    else:
      output_word += '_'
  return output_word


while lives > 0:
  print('You have ' + str(lives) + ' Lives Left')
  print(print_word(word, guessed))
  guess = input('Pick a Letter:')
  if guess in guessed:
    print("You've already tried that.")
  elif guess in word:
    print("You've guessed Right!")
    guessed.append(guess)
  else:
    print("You've guessed Wrong!")
    lives = lives - 1
    guessed.append(guess)

