# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
import string
import os
clear = lambda: os.system('cls')

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"
UNGUESSED_LETTER = "_"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    for secret_letter in secret_word:
        if secret_letter not in letters_guessed:
            return False
    else:
        return True

def print_alphabet():
    global letters_guessed
    output = []
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            output.append('*')
        else:
            output.append(letter)
    return ''.join(output)

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    output = []

    for secret_letter in secret_word:
        if secret_letter in letters_guessed:
            output.append(secret_letter)
        else:
            output.append(UNGUESSED_LETTER)
    return ''.join(output)

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    secret_word  = get_word()

    while True:
        print (MAX_GUESSES - mistakes_made), 'incorrect guesses left.'
        print print_alphabet()        
        print print_guessed()        
        guessed_letter = string.lower(raw_input("Your guess: "))
        clear()
        if guessed_letter in letters_guessed:
            print "You already guessed that!"
        else:
            letters_guessed.append(guessed_letter)
            if guessed_letter in secret_word:
                if word_guessed():
                    print "You win!"
                    break
                else:
                    print "Yep!"
            else:
                print "Nope!"
                mistakes_made += 1
                if mistakes_made == MAX_GUESSES:
                    print "You lose! The word was", secret_word
                    break 
    return None

play_hangman()