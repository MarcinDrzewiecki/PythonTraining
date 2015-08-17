__author__ = 'drzewko'
import random

dictionary = ("slowo", "glupstwo", "mama", "powiesc", "pieniadz", "milosc", "wladza")

guess_the_word = random.choice(dictionary)
print guess_the_word
num_of_words = len(guess_the_word)
tries = 5

print "Guess the word containing", num_of_words, "letters."
print "You have", tries, "tries"

for i in range(tries):
    letter_guess = raw_input("What letter is in this word?\n")
    if letter_guess in guess_the_word:
        print "Yes!!"
    else:
        print "Nope :("
    print "You have", tries - i - 1, "available letter guesses left"

user_guess = raw_input("\nNow guess the word\n")
if user_guess == guess_the_word:
    print "Brawo!"
else:
    print "Sorry, not this time"

raw_input("\nPress ENTER to finish the game")
