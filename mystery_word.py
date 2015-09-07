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
    all_guesses = []
    all_guesses.append(guesses)

    game_display = list('_'*len(word))
    for i in range(len(word)):
        for c in range(len(all_guesses)):
            if word[i] == all_guesses[c]:
                game_display[i] = all_guesses[c].upper()

    pretty_game_display = " ".join(game_display)
    return pretty_game_display

    '''
    PAUSED
    display_empty = list('_'*len(word))  # underscore list ['_','_', etc]
    display_with_guesses = []
    catch_guess =[]
    count_guess = 1
    print("The word has {} letters.\n". format(len(word)))
    print("There are {} guesses.\n". format(guesses))

    print(" ".join(display_empty))

    while count_guess is < (guesses + 1):
        guess = input("\nEnter your guess: ").upper()
        catch_guess.append(guess)
        count_guess += 1
        print("Guess {} is {}.\nRemaining guesses = {}". format(count_guess, guess, (guesses-count_guess))
        disp
    '''

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
    print("\nWelcome to the MYSTERY WORD GAME!\n")
    # TODO PROMPT FOR DIFFICULTY in caps or not
    diff_level = 'E'
    # TODO PROMPT FOR GUESS change to caps
    guesses = 8     #parameterized guess level
    guess = 'A'
    f = open('/usr/share/dict/words')
    next = f.read().lower()     # provides lower case list with \n
    word_list = next.split()    # perfect list of words.

    # print("Top of TOTAL list: ")
    # for i in range(5):
    #     print(word_list[i])     # prints only a few, includes \n in list.
    #
    # print("\nFinished 'word_list', \ncalling 'easy/medium/hard_words'")

    if diff_level == 'E':
        easy_words_list = easy_words(word_list)
        word = random_word(easy_words_list)
        print("EASY level:\n")
        display_word(word, guesses)
# TODO display_word(word, guess)
    elif diff_level == 'M':
        medium_words_list = medium_words(word_list)
        word = random_word(medium_words_list)
        print("MEDIUM level: your word has {} letters.". format(len(word)))
        print("Your first guess was {}.". format(guess.upper()))
# TODO display_word(word, guess)
    elif diff_level == 'H':
        hard_words_list = hard_words(word_list)
        word = random_word(hard_words_list)
        print("HARD level: your word has {} letters.". format(len(word)))
        print("Your first guess was {}.". format(guess.upper()))
# TODO display_word(word, guess)
    else:
        print('Please enter a difficulty level')

    # print("\nFinished 'easy/medium/hard'_words, \ncalling 'random_word'")
    # print(word)
    # print("\nFinished 'random_word, \ncalling 'display word")
    # print("Here is the random word from main(): {}". format(word))


"""
    Runs when the program is called from the command-line.
    TODO - Load all data from external source '/usr/share/dict/words'

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
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

if __name__ == '__main__':
    main()
