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

word = random.choice(words)
print(word)
guess = input()

def test(word, guess):
  print("_")
  guessed = []
  line = []
  lives = 6
  
  for letter in word:
    line.append("_")
    print(line)

    if guess == letter:
       print("Lives:", lives)
       guessed.append(guess)
       print("Guessed:", guessed)
       guess = input()
 
    if guess != letter:
      print("Lives: ", lives)
      lives = lives - 1
      guessed.append(guess)
      print("Guessed:", guessed)
      guess = input()

      if lives == 0:
        print("Lives:", lives)
        print("You lose! The word was " + word + ". ")
        break    
  
  if guess == letter in word:
    #line[] = guess
    word.replace(guess)

  if guess == word:
    print("You win!")
  
  if guess == guessed.count(guess):
    print("You've already tried that.")

test(word, guess)