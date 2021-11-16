import random

#hangman
#create list of words
#pick a random word from that list
#print underscores per letter in word
#at all times: show amount of attempts left
#if input is true, underscore(s) will change into letter
#if word is true, change all underscores to word
#if trys run out, print "you lose!"
#if letter not equal to letters in word, trys -1, print "try again!"
#if word == correct, print "you win!"

words = ["barnacle,", "automatic", "excessive", "conscious", "willpower", "diplomat", "computing"]

word = random.choice(words)
print(word)
word_length = word.count()
print(word_length)
guess = input()
lives = 6

for letter in word:
  word.count(guess)
  if guess == letter:
    print(guess)
  else:
    print("_")


