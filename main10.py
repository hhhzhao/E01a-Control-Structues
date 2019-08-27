#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
#creating a list that contains colors
colors = ['red','orange','yellow','green','blue','violet','purple']
#Having a empty veribale called play_again
play_again = ''
best_count = sys.maxsize            # the biggest number
#starting a loop that ends when play_again="n" or "no"
while (play_again != 'n' and play_again != 'no'):
    #randomly choose a color from the colors list.
    match_color = random.choice(colors)
    #set the count = 0, which means how many times user is playing the game.
    count = 0
    #having a empty veriable called color.
    color = ''
    #starting a loop that ends when color user's input is equal to the match color.
    while (color != match_color):
        #ask user to input a color that user like
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #strip out the space and lower case the word
        color = color.lower().strip()
        #count +1 which means user played one round
        count += 1
        #if color = match color, it will print correct.
        if (color == match_color):
            print('Correct!')
          #else, it will ask user to try again, tell them how many times they have already used.  
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} tries!'.format(count))
    if (count < best_count):
        #if count number is ismaller than the best_count, count=best_count
        print('This was your best guess so far!')
        best_count = count
    #user will play again, they can type n or no to quit
    play_again = input("\nWould you like to play again? ").lower().strip()
print('Thanks for playing!')