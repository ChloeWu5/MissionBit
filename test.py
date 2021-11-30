import random
words = {"barnacle": 8, "automatic": 9, "excessive": 9, "conscious": 9, "willpower": 9, "diplomat": 8, "computing": 9}

word = random.choice(words)
print(word)
guess = input()
guessed = []

lives = 6

guess = word.count(guess)
if guess == letter:
    print(guess)
else:
    print("_")

# If the letter in the index in ‘automatic’ is equal to the index in list, we replace the index in list with that letter