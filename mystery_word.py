# MYSTERY WORD mystery_word.py
import re
from random import randint

def easy_words(word_list):
    easy_words_list = []         # RETURNS LIST OF EASY WORDS 4-6 CHARACTERS
    for i in range(len(word_list)):
        if len(word_list[i]) >= 4 and len(word_list[i]) <= 6:
            easy_words_list.append(word_list[i])
            # easy_words now has a good list of easy words.
    print("\nTop of Easy word list:")
    for c in range(5):
        print(easy_words_list[c])        # printing a few to confirm (\n) included
    return easy_words_list

    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    # - easy_words = words of length between 4 and 6 letters.
    # - read in based on length

    """
    # TODO
    pass


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    # TODO
    pass


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    # TODO
    pass


def random_word(word_list):

    random_num = randint(0,len(word_list)-1)
    word = word_list[random_num]
    print("Random word generated: {} ". format(word))
    return word

    """
    Returns a random word from the word list.
    """

def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
        # - loop to prompt for 8 guesses
        # - Any size word to be entered
        # - size of the pattern = len(word)

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.
        # - insert the space with 'sep=' '' embedded function __.upper()

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
        # - loop through a comparison between the word and the guessed letter.
        # - loop through the display to swap out 'space' indexed letters.
        # - adjust the index to count the space between letters
        # - swap out the underscore with the letter at all locations

    """
    # TODO
    pass


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.

    """
    # TODO
    pass


def main():
    diff_level = 'E'            # drive into def easy_words()
    f = open('/usr/share/dict/words')
    next = f.read().lower()     # provides lower case list with \n
    word_list = next.split()    # perfect list of words.
    print("Top of TOTAL list: ")
    for i in range(5):
        print(word_list[i])     # prints only a few, includes \n in list.
    # return word_list
    print("\nFinished 'word_list', \ncalling 'easy_words'")
    if diff_level == 'E':
        easy_words_list = easy_words(word_list)
    elif diff_level == 'N':
        medium_words(word_list) # TODO medium_words_list function return
    elif diff_level == 'H':
        hard_words(word_list)   # TODO hard_words_list function return
    else:
        print('Please enter a difficulty level')

    print("\nFinished 'easy_words, \ncalling 'random_word'")
    random_word(easy_words_list)
    print("\nFinished 'random_word, \ncalling 'display word")


    # print(word_list)            # word_list is a list of lower case words.
"""
    Runs when the program is called from the command-line.
    TODO - Load all data from external source '/usr/share/dict/words'

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
                TOD0: direct to the appropriate word filter function.
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
                TODO: index those letters guessed and put in place
                - display grid "[_ _ _ _ _ _ _ _ _ _]"
                - character replace in selected word
       d. Prompting the user for a letter to guesss
    4. Finishing the game and displaying whether the user has won or lost
                TODO: 8 try loop
    5. Giving the user the option to play again
"""
    # TODO

if __name__ == '__main__':
    main()
