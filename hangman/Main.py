import random
import os
from hangman_art import HANGMANPICS,logo

lives = len(HANGMANPICS) - 1
print(logo)
word_list = ["askew", "avenue", "awkward"]
chosen_word = random.choice(word_list)
# empty list for display
display = []
# adding a _ for each char in the chosen word
for char in chosen_word:
    display.append('_')

continueGame = True

while continueGame:
    print(' '.join(display))
    letter = input('Guess a letter: ').lower()
    os.system('cls')  # This is not working for me!!
    found = False
    if len(letter) > 1:
        print('letter is supposed to be of length 1.')
        continue
    elif letter in display:
        print('You have already guessed that letter!!')
        continue
    for num in range(0, len(chosen_word)):
        if chosen_word[num] == letter:
            display[num] = letter
            found = True
            if '_' not in display:
                continueGame = False
    if not found:
        lives -= 1
        if lives == 0:
            continueGame = False
        print(f'{letter} is not in the word, you loose a life.')
        print(HANGMANPICS[-lives - 1])

if '_' not in display:
    print('You Win!!')
else:
    print('You Loose!!')
