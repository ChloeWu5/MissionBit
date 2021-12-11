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


def test(word):
    guessed = []
    # 1st time: guessed = ["a"]
    # 2st time: guessed = ["a", "l"]
    # 3st time: guessed = ["a", "l", "e"]

    lives = 6

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
        guessed.append(guess)
        print("Guessed:", guessed)
        if guess in guessed:
            print("You've already tried that.")
        if guess in word:
            print("Correct!")
            print("Lives:", lives)
        else:
            print("Incorrect, try again.")
            lives = lives - 1
            print("Lives:", lives)
        if line == word:
            print("Congrats, you won!")
            break

    if lives == 0:
        print("You lose, the word was", word + ".")

    # "some_string"  # This is just a "list" of characters
    # 123 in [100, 200, 300]
    # 123 in [100, 123]
    # "a" in ["p", "l"]
    # "a" in ["p", "a", "l"]

    # Can we rewrite this a bit?
    # Human form: Is the character the person typed lin the word


test(word)
