import random

#project hangman

#create list of words
#pick a random word from that list
#print underscores per letter in word
#at all times: show amount of attempts left
#if input is true, underscore(s) will change into letter
#if input matches a letter from word, underscore(s) will change into letter
#if word is true, change all underscores to word
#if trys run out, print "you lose!"
#if letter not equal to letters in word, trys -1, print "try again!"
#if word == correct, print "you win!"

words = [
    "barnacle", "automatic", "excessive", "conscious", "willpower", "diplomat",
    "computing", "enigmatic", "telescope"
]

#word = random.choice(words)
word = "apples"
print(word)



def test(word):
    guessed = []
    # 1st time: guessed = ["a"]
    # 2st time: guessed = ["a", "l"]
    # 3st time: guessed = ["a", "l", "e"]

    lives = 6

    def add_numbers(a, b):
        summ = a + b
        return summ

    d = add_numbers(1, 2)

    def print_line():
        line = ''
        for letter in word:
            if guess == letter:
                line += letter
            elif letter in guessed:
                line += letter
            else:
                line += '_'
        print(line)  # Here, line could be "a__le" or "____" or "apple"
        return line
    # Let user guess until lives run out
    while lives > 0:
        guess = input()
        line = print_line()
        guessed.append(guess)
        if guess in word:
            print("Correct!")
        else:
            print("No, try again.")
            lives = lives - 1
            print("Lives:", lives)
        if line == word:
            print("yay")
            break



    # "some_string"  # This is just a "list" of characters
    # 123 in [100, 200, 300]
    # 123 in [100, 123]
    # "a" in ["p", "l"]
    # "a" in ["p", "a", "l"]

    # Can we rewrite this a bit?
    # Human form: Is the character the person typed lin the word

    """
      # Every time: letter = "e"

      # word:      apple
      # Beginning: _____
      # Geuss l:   ___l_
      # Guess a:   a__l_
      # Guess p:   appl_

      #



    while lives > 0:
            if guess == letter:  # problem: letter is always last letter of word
                  print(guess)
                  print("Lives:", lives)
                  guessed.append(guess)
                  print("Guessed:", guessed)
                  guess = input()


     elif guess != letter:
  
               print(guess)
                  lives = lives - 1
                  print("Lives:", lives)
                  guessed.append(guess)
                  print("Guessed:", guessed)
                  print("Try again!")
                  guess = input()
 
                # Move out of for loop. Wrap all inside while loop


       # if guess in guessed:
           #print("You've already tried that.")

            if guess == word:
                  print("Lives:", lives)
                  print("Correct! You win!")
                  break

            if lives == 0:
                  print("Lives:", lives)
                  print("You lose! The word was " + word + ". ")
                  break

    """

test(word)
