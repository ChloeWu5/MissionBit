#hangman

#create list of words
#pick a random word from that list
#print underscores per letter in word
#at all times: show amount of attempts left
#if input is true, underscores will change into letter
#if word is true, change all underscores to word
#if trys run out, print "you lose!"
#if word == correct, print "you win!"

words = ["barnacle,", "automatic", "equation", "conscious", "willpower", "diplomat", "computing"]

word_length = 0

guess = input()