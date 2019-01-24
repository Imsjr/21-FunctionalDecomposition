"""
Hangman.

Authors: Jason Ims and Christina Rogers.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# Done: 2. Implement Hangman using your Iterative Enhancement Plan.

import random

def main():
    guesses = 5
    currentWord = []
    win = False
    word = min_length(pick_word())
    for k in word:
        currentWord = currentWord + ['_ ']
    check_guess(word, get_guess(), currentWord, guesses)
    while True:
        if guesses == 0:
            print('You lose, better luck next time :(')
            break
        guesses = check_guess(word, get_guess(), currentWord, guesses)
        for item in currentWord:
            win = True
            if item == '_ ':
                win = False
        if win == True:
            print('You win, good job :)')
            break

def flatten(currentWord):
    stringCurrentWord = ''
    for letter in currentWord:
        stringCurrentWord = stringCurrentWord + letter + ' '
    print('     ', stringCurrentWord)

def min_length(words):
    minimum = int(input('What is the minimum length for the word: '))
    while True:
        if len(words) < (minimum):
            words = pick_word()
        else:
            break
    return (words)

def get_guess():
    guess = str(input('Please enter your guess: '))
    return guess

def check_guess(word, guess, currentWord, guesses):
    correct = False
    for k in range (len(word)):
        if guess == word[k]:
            currentWord[k] = word[k]
            correct = True
    if correct == False:
        guesses = guesses - 1
        print('     Guess is incorrect. You have', guesses, 'guesses remaining')
    else:
        print('     Your guess is in the word! You have', guesses, 'guesses remaining')

    flatten(currentWord)
    return (guesses)

def pick_word():
    with open('words.txt')as f:
        f.readline()
        string = f.read()
        words = string.split()
    r = random.randrange(0, len(words))
    item = words[r]
    print(item)
    return item

while True:
    main()
    if str(input('Do you want to play again (Y or N):')) == 'N':
        break
####### Do NOT attempt this assignment before class! #######

