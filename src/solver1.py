from helpers import training_words, all_words, playWordle
from random import randint

# currently guesses randomly
def solver1(guessed_words, guessed_letters):
    rand_idx = randint(0, len(training_words)-1)
    return all_words[rand_idx]

average_guess = playWordle(solver1, training_words)

print(f"\n Averaged {average_guess} guesses per wordle!")