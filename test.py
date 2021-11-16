import random
words = {"barnacle": 8, "automatic": 9, "excessive": 9, "conscious": 9, "willpower": 9, "diplomat": 8, "computing": 9}

word = random.choice(words.keys)
word_length = word.values
print(word)
print(word_length)
guess = input()

guess = word.count(guess)
if guess == letters:
    print(guess)
else:
    print("_")