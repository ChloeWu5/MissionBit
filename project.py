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
    "computing", "enigmatic", "telescope", "malapropism", "cantle", "regnant",
    "clerisy", "ostensible", "syntactic", "allocate", "momentous", "evanescent", "sagacity", "anecdote", "rancorous", "orator", "ephemeral"
]

word = random.choice(words)


def hangman(word):
    guessed = set()
    # 1st time: guessed = {"a"}
    # 2st time: guessed = {"a", "l"}
    # 3st time: guessed = {"a", "l", "e"}

    lives = 6
    #starting number of lives

    def print_line():
        line = ''
        for letter in word:
            if guess == letter:
                line += letter
            elif letter in guessed:
                line += letter
            else:
                line += '_'
        print(line)
        return line

    # Let user guess until lives run out
    # "a" in "apples"
    # "pple" in "apples"
    while lives > 0:
        guess = input("Pick a letter: ")
        line = print_line()
        
        if guess in guessed:
            print("You've already tried that.")
        elif guess in word:
            print("Correct!")
        else:
            print("Incorrect, try again.")
            lives -= 1
        if line == word:
            print("Congrats, you won!")
            break
        guessed.add(guess)
        print("Guessed:", guessed)
        print("Lives:", lives)

    if lives == 0:
        print(f"You lose, the word was {word}.")

hangman(word)
