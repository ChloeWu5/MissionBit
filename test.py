import random

# If the letter in the index in ‘automatic’ is equal to the index in list, we replace the index in list with that letter

words = [
    "barnacle", "automatic", "excessive", "conscious", "willpower", "diplomat", "computing", "enigmatic", "telescope"]

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
  print('You have ' + str(lives) + ' Lives Left.')
  print(print_word(word, guessed))
  guess = input('Pick a Letter: ')
  
  if guess in guessed:
    print("You've already tried that.")
    print("Guessed:", guessed)
  elif guess in word:
    print("You guessed correctly!")
    guessed.append(guess)
    print("Guessed:", guessed)
  else:
    print("You guessed incorrectly.")
    lives = lives - 1
    guessed.append(guess)
    print("Guessed:", guessed)

  if word.count("_") == 0:
    print("Correct, the word was", word + ".")
    break

if lives == 0:
  print('You have ' + str(lives) + ' Lives Left.')
  print("Incorrect, the word was", word + ".")