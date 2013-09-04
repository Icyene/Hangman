#!/usr/bin/python
import os
import sys

NOOSE = [
    ' /-----',
    '|',
    '|',
    '|',
    '|',
    '|',
    '|',
    '|',
    '|',
    ]
VICTIM = [[
    '',
    '     |',
    '     |',
    '     O ',
    '       ',
    '       ',
    '       ',
    ], [
    '',
    '     |',
    '     |',
    '     O ',
    '    /| ',
    '       ',
    '       ',
    ], [
    '',
    '     |',
    '     |',
    '     O ',
    '    /|\\',
    '       ',
    '       ',
    ], [
    '',
    '     |',
    '     |',
    '     O ',
    '    /|\\',
    '     | ',
    '    / ',
    ], [
    '',
    '     |',
    '     |',
    '     O  ',
    '    /|\\',
    '     |  ',
    '    / \\',
    ]]

def game():
    clear()
    print 'Welcome to a Python console implementation of the classic hangman game.\n'
    word = raw_input('Please enter the key word: ').upper()
    clear()

    turn = 0
    letters = []
    wrong = []

    while turn < 5:
        print 'Hangman. Wrongs: %s/5.' % turn
        print '--------------------------------\n'
        draw_noose(turn)

        print "You've already guessed the letters:", ', '.join(wrong)

        decoded = ''
        for char in word:
            decoded += (char if char in letters else '*')
        print "So far, you've decoded '%s'" % decoded

        letter = raw_input('\nInput a letter: ').upper()
        if len(letter) != 1:
            print 'You must type one character at a time.'
            raw_input()
        elif letter in letters or letter in wrong:
            print "You've already guessed that letter!"
            raw_input()
        elif letter in word:
            for i in xrange(word.count(letter)):
                letters.append(letter)
            if len(letters) == len(word):
                clear()
                print 'Congratulations, you won! Hit enter to exit.'
                raw_input()
                clear()
                return
        else:
            wrong.append(letter)
            turn += 1
        clear()

    draw_noose(turn)
    print "\nYou lost, try again!"
    print "The word in question was '%s'. You got so far as '%s.\n" % (word, decoded)
    print 'Thanks for playing! Hit enter to exit.'
    raw_input()
    clear()

def draw_noose(stage):
    for i in xrange(0, 9):
        print NOOSE[i] + ((VICTIM[stage - 1][i] if stage != 0 and i < 7 else ''))

def clear():
    os.system(os.name == 'nt' and 'cls' or 'clear')

if __name__ == '__main__':
    game()