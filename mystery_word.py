# MYSTERY WORD mystery_word.py
import re
from random import randint

def easy_words(word_list):
    easy_words_list = []         # RETURNS LIST OF EASY WORDS 4-6 CHARACTERS
    for i in range(len(word_list)):
        if len(word_list[i]) >= 4 and len(word_list[i]) <= 6:
            easy_words_list.append(word_list[i])
    return easy_words_list

    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.

    """

def medium_words(word_list):
    medium_words_list = []         # RETURNS LIST OF MEDIUM WORDS 6-8 CHARACTERS
    for i in range(len(word_list)):
        if len(word_list[i]) >= 6 and len(word_list[i]) <= 8:
            medium_words_list.append(word_list[i])
    return medium_words_list

    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """

def hard_words(word_list):
    hard_words_list = []         # RETURNS LIST OF HARD WORDS 8+ CHARACTERS
    for i in range(len(word_list)):
        if len(word_list[i]) >= 8:
            hard_words_list.append(word_list[i])
    return hard_words_list

    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """

def random_word(word_list):

    random_num = randint(0,len(word_list)-1)
    word = word_list[random_num]
    return word

    """
    Returns a random word from the word list.
    """

def display_word(word, guesses):
    game_display = list('_'*len(word))
    for i in range(len(word)):
        for c in range(len(guesses)):
            if word[i] == guesses[c]:
                game_display[i] = guesses[c].upper()

    pretty_game_display = " ".join(game_display)
    return pretty_game_display

    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.

    """

def is_word_complete(word, guesses):
    word_bin = []
    count = 0
    for i in range(len(word)):
        if word[i] not in word_bin:
            word_bin.append(word[i])   # unique letters in the word
    for i in range(len(word_bin)):
        for c in range(len(guesses)):
            if word_bin[i] == guesses[c]:
                count += 1              # count everytime quess matches unique word_bin
    if count == len(word_bin):
        return True
    else:
        return False

    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """

def main():
    print("\nWelcome to the MYSTERY WORD GAME!\n")

    print("Select your difficulty level: \n")
    diff_level = input("E for easy, M for medium, H for hard: \n")

    # if diff_level != "E" or diff_level != "M" or diff_level != "H":
    #     print("If you want to quit type Q\n otherwise select E, M or H.")

    maximum_guesses = 8     #parameterized guess level

    f = open('/usr/share/dict/words')
    next = f.read().lower()     # provides lower case list with \n
    word_list = next.split()    # perfect list of words.

    if diff_level == 'E':
        easy_words_list = easy_words(word_list)
        word = random_word(easy_words_list)
        print("EASY level:\n")

    elif diff_level == 'M':
        medium_words_list = medium_words(word_list)
        word = random_word(medium_words_list)
        print("MEDIUM level:\n")

    elif diff_level == 'H':
        hard_words_list = hard_words(word_list)
        word = random_word(hard_words_list)
        print("HARD level:\n")
    else:
        print('Please enter a difficulty level')

    print("Your word has {} letters.\n". format(len(word)))
    guesses = []
    while is_word_complete(word, guesses) == False:
        display_word(word, guesses)
        for i in range(1, maximum_guesses):
            print("This is guess #: {}". format(range[i]))
            guess = input("Enter your guess as a single letter:")
            guesses.append(guess)
        print("You did not guess.  \nThe word was {}.". format(word))
        repeat = input("Would you like to play again?, Y or N ")
        if repeat == "Y":
            main()
        else:
            break
    print("You guessed the word!\n")
    repeat = input("Would you like to play again?, Y or N ")
    if repeat == "Y":
        main()
    else:
        print("Thanks for playing.")
        quit()


"""
    Runs when the program is called from the command-line.
    TODO - Load all data from external source '/usr/share/dict/words'

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guesss
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
"""

if __name__ == '__main__':
    main()
