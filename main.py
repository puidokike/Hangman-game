from graphics import stages
from words import words
from random import choice

word = choice(words)
letters = []
for letter in word:
    letters.append(letter)

covered = list('_' * len(word))
print(''.join(covered))

incorrect_player_letters = []

while stages:
    guess = input("Guess the letter: ")
    if word == ''.join(covered):
        print(f'Nice job. The word is {word} indeed.')
        break

    if guess in letters:
        for position in range(len(word)):
            letter = word[position]
            if guess == letter:
                covered[position] = letter
                print(''.join(covered))
                print("Nice job")

    else:
        incorrect_player_letters.append(guess)
        print(stages[0])
        stages.pop(0)
        print("Try again")
        print(f'Incorrect letters: {incorrect_player_letters}')
        print(''.join(covered))

    if not stages:
        print(f'Sorry. Correct word was: {word}')



