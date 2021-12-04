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
  # word="conscious", guess="conscious"
  print("_")
  guessed = []
  line = []
  lives = 6

  for i in range(len(word)):
    line.append("_")

  for letter in word:
    print(line)
    index = 0
    
    # Idea: Start by comparing each letter of word to each letter of guess
    # Later: Make order not matter.
    
    # Problem: conscious is a full word and letter is only 1 letter

    while guess != letter: 
        print(guess)
        lives = lives - 1
        print("Lives:", lives)
        guessed.append(guess)
        print("Guessed:", guessed)
        print("Try again!")
        guess = input() 
        # Move out of for loop. Wrap all inside while loop
        
    
    if guess in letter:
       #guess="conscious", letter="c"
       print(guess)
       index = word.index(guess)
       print("Lives:", lives)
       guessed.append(guess)
       print("Guessed:", guessed)
       guess = input()

    if lives == 0:
      print("Lives:", lives)
      print("You lose! The word was " + word + ". ")
      break 

    if guess == word:
        print("Lives:", lives)
        print("Correct! You win!")
        break

    if guess in guessed:
        print("You've already tried that.")

  if guess == letter in word:
    word.replace(guess)
    print(index)
    # for i in line:
    #   line[i] = index
    #print(index)

test(word, guess)

