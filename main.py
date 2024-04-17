import random

word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

for _ in range(word_length):
        display += "_"
print(display)

guess = input('guess a letter: ').lower()

for position in range(word_length):
        letter = chosen_word[position]            
        if letter == guess:
                 display[position] = letter
print(display)

