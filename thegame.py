import random


from hangman_words import word_list
from hangman_art import *

print(logo)
word = random.choice(word_list)

word_lenght = len(word)

success = 0
deneme = 6
guess = " "
letter = " "
the_man = 6


try_word = ""
for i in range(0, word_lenght):
    try_word += "_"





while the_man > 0 and success == 0:
    print(try_word)
    guess = input("Guess a letter: ")
    if word.count(guess.lower()) == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(try_word)
        the_man -= 1
        print(stages[the_man])


    elif try_word.count(guess.lower()) != 0:
        print(f"You have already guessed {guess}")

    else:
        for i in range(0, word_lenght):
            letter = word[i]
            if letter == guess:
                try_word = try_word[:i] + letter + try_word[i+1:]

        print(try_word)
        print(stages[the_man])


    if try_word == word:
        success = 1
        print("You win!")




if (the_man == 0 and success == 0):
    print("You loooseee!")
    print(f"The word was {word}")
