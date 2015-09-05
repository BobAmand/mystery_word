# MYSTERY WORD mystery_word.py
import re

def easy_words(word_list):
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
    """
    Returns a random word from the word list.
    """
    # TODO
    pass


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
        # - Any size word to be entered
        # - size of the pattern = len(word)

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.
        # - insert the space with 'sep=' '' embedded function

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
    # Read data in

    # with open('/usr/share/dict/words') as f:
    #     for i in range(10):
    #         print(list(f))  #.read().rstrip('\n'))

    f = open('/usr/share/dict/words')
    word_list = list(f.read())
    print(word_list)

    # print(word_list)
                #need to strip off the "\n"

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
                - display grid "[__________]"
                - character replace in selected word
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
                TODO: 8 try loop
    5. Giving the user the option to play again
    """
    # TODO

if __name__ == '__main__':
    main()
