###############################################################################
# battleship                                                                  #
#                                                                             #
# Originally based off of the battleship game that the Python course on       #
# Codecademy had users build. Now expanded and in desperate need of polishing.#
###############################################################################

# Note: This game's multiplayer function, in effect, just causes the code
# to have the same thing twice.

from random import randint
import sys # Imports stuff for restart program
import os # Imports stuff for restart program and for clearing the screen

def restart_program(): # Restarts program function
    python = sys.executable
    os.execl(python, python, * sys.argv)

def clear_screen(): # Clears screen function
    os.system('cls' if os.name == 'nt' else 'clear')

one_board = [] # Initilizes the game board
two_board = []

for x in range(5): # Generates the empty game boards
    one_board.append(["O"] * 5)
for x in range(5):
    two_board.append(["O"] * 5)

def print_board(board): # Prints the board
    for row in board:
        print " ".join(row) # Removes the formatting when the 'board' is printed

def random_row(board): # Generates a random integer in the range 0-4
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def verify_int(input): # Checks to see if input is an integer
    try: # Tries...
        val = int(input) # If input is an integer...
        return val # Returns input if it is an integer
    except ValueError: # If an error is returned...
        return 0 # Returns a "0"

one_ship_row = random_row(one_board) # Randomly picks the ship's first
one_ship_col = random_col(one_board) # compnent's row
two_ship_row = random_row(two_board)
two_ship_col = random_col(two_board)

one_direc = randint(1, 4) # Decides the direction of the ship's second component
two_direc = randint(1, 4) # 1 = North, 2 = East, 3 = South, 4 = West

status = 0

while status == 0: # Decides the direction of the ship's second component
    if one_direc == 1: # north
        one_sec_ship_row = one_ship_row - 1 # The row above is selected
        one_sec_ship_col = one_ship_col # The same column is selected
        if one_sec_ship_row < 0: # If the row selected is outside of the bounds:
            one_sec_ship_row = one_sec_ship_row + 2 # Reverses direction to the
                                                    # other side
            status = 1 # Begins the selection of player 2's second component
        else: # If the row selected is inside of the bounds...
            status = 1 # Begins the selection of player 2's second component
    elif one_direc == 2: # east
        one_sec_ship_row = one_ship_row
        one_sec_ship_col = one_ship_col + 1
        if one_sec_ship_col > 4:
            one_sec_ship_col = one_sec_ship_col - 2
            status = 1
        else:
            status = 1
    elif one_direc == 3: # south
        one_sec_ship_row = one_ship_row + 1
        one_sec_ship_col = one_ship_col
        if one_sec_ship_row > 4:
            one_sec_ship_row = one_sec_ship_row - 2
            status = 1
        else:
            status = 1
    elif one_direc == 4: # west
        one_sec_ship_row = one_ship_row
        one_sec_ship_col = one_ship_col - 1
        if one_sec_ship_col < 0:
            one_sec_ship_col = one_sec_ship_col + 2
            status = 1
        else:
            status = 1
    else:
        print "Error 1: Player 1 Ship, Component 2"

while status == 1: # The same as above, but for ship 2
    if two_direc == 1:
        two_sec_ship_row = two_ship_row - 1
        two_sec_ship_col = two_ship_col
        if two_sec_ship_row < 0:
            two_sec_ship_row = two_sec_ship_row + 2
            status = 2 # Begins the actual game
        else:
            status = 2
    elif two_direc == 2:
        two_sec_ship_row = two_ship_row
        two_sec_ship_col = two_ship_col + 1
        if two_sec_ship_col > 4:
            two_sec_ship_col = two_sec_ship_col - 2
            status = 2
        else:
            status = 2
    elif two_direc == 3:
        two_sec_ship_row = two_ship_row + 1
        two_sec_ship_col = two_ship_col
        if two_sec_ship_row > 4:
            two_sec_ship_row = two_sec_ship_row - 2
            status = 2
        else:
            status = 2
    elif two_direc == 4:
        two_sec_ship_row = two_ship_row
        two_sec_ship_col = two_ship_col - 1
        if two_sec_ship_col < 0:
            two_sec_ship_col = two_sec_ship_col + 2
            status = 2
        else:
            status = 2
    else:
        print "Error 2: Player 2 Ship, Component 2"

clear_screen()
# The following few lines are the beginning instructions.
print "Battleship"
print ""
print ("Type in your desired number and press 'Enter' when prompted. Only "
       "enter in a single number in the range of 1 to 5. The ship fills up "
       "exactly 2 adjacent blocks. The following is how the grid is "
       "organized.")

'''
print "Battleship"
print ""
print ("Type in your desired number and press 'Enter' when prompted. Only "
       "enter in a single number in the range of 1 to 5. The ship fills up "
       "exactly 2 adjacent blocks. The following is how the grid is "
       "organized."
        + " (" + str(one_ship_row + 1) + ", " + str(one_ship_col + 1) + ")"
        + " (" + str(one_sec_ship_row + 1) + ", " + str(one_sec_ship_col + 1)
        + ") &" + " (" + str(two_ship_row + 1) + ", " + str(two_ship_col + 1)
        + ")" + " (" + str(two_sec_ship_row + 1) + ", "
        + str(two_sec_ship_col + 1) + ")") # Everything after the first '#' is
                                           # used to print the answers to this
                                           # game. It's only used for debugging
                                           # purposes.
'''

print ""
print "O O O O O <- Row 1"
print "O O O O O <- Row 2"
print "O O O O O <- Row 3"
print "O O O O O <- Row 4"
print "O O O O O <- Row 5"
#print "^1  ^3  ^5"
#print "  ^2  ^4"
print "^ Column 1"
print "  ^ Column 2"
print "    ^ Column 3"
print "      ^ Column 4"
print "        ^ Column 5"
print ""
raw_input("Press 'Enter' to begin the game")
clear_screen()

answer = raw_input("Would you like to use your own names instead of generic nam"
                   "es? ")
if answer.strip() in "y Y yes Yes YES".split():
    player_one_name = raw_input("What's Player 1's name? ")
    player_two_name = raw_input("What's Player 2's name? ")
    clear_screen()
else:
    player_one_name = "Player 1"
    player_two_name = "Player 2"

while True: # The infinite loop that is actual gameplay.
    while status == 2: # Player 2's turn
        print "It is now %s's Turn." % player_two_name
        print ""
        print "%s's Board" % player_one_name
        print ""
        print_board(one_board) # Prints player one's board
        print ""
        guess_row = verify_int(raw_input("Guess Row: ")) # Asks for input and
                                                         # checks to see if it's
                                                         # an integer
        guess_row = guess_row - int(1) # Corrects it to what actually gets
                                       # processed by subtracting 1
        guess_col = verify_int(raw_input("Guess Col: ")) # Does the same as
                                                         # above
        guess_col = guess_col - int(1) # Does the same as above
        if ((guess_row == one_ship_row and guess_col == one_ship_col) or
            (guess_row == one_sec_ship_row and guess_col == one_sec_ship_col)):
                                                            # The winner branch
            one_board[guess_row][guess_col] = "0" # Marks the board as the
                                                  # correct answer
            print ""
            print ("Hit!")
            if ((one_board[one_ship_row][one_ship_col] == "0") and
                (one_board[one_sec_ship_row][one_sec_ship_col] == "0")):
                # ^ Checks to see if both components of the ship have been
                # found, if so...
                print ""
                print "You won!"
                status = 4 # Begins the celebratory statement below
            else: # If both components have NOT been found this branch is
                  # invoked.
                raw_input("Press 'Enter' to begin " + str(player_one_name) + "'s turn")
                clear_screen()
                status = 3 # Begins Player 1's turn
        else: # The loser branch
            if ((guess_row < 0 or guess_row > 4) or
                (guess_col < 0 or guess_col > 4)): # Is the answer within the
                                                   # range of 0 to 4?
                print ""
                print "Your guess isn't on the grid. Try again."
            elif one_board[guess_row][guess_col] == "X": # Has the chosen area
                                                         # already been guessed?
                print ""
                print "You've already guessed this space. Try again."
            elif one_board[guess_row][guess_col] == "O": # Is the chosen area
                                                         # unchosen thus far?
                print ""
                print "You missed!"
                one_board[guess_row][guess_col] = "X" # Marks the area as chosen
                raw_input("Press 'Enter' to begin " + str(player_one_name) + "'s turn")
                clear_screen()
                status = 3 # Begins Player 2's turn
            else: # The 'just-in-case' error branch used for debugging
                print "Error 3: Player 1 Turn"
    else:
        a = 0 # Indicates that everything ran fine

    while status == 3:
        print "It is now %s's Turn." % player_one_name
        print ""
        print "%s's Board" % player_two_name
        print ""
        print_board(two_board)
        print ""
        guess_row = verify_int(raw_input("Guess Row: "))
        guess_row = guess_row - int(1)
        guess_col = verify_int(raw_input("Guess Col: "))
        guess_col = guess_col - int(1)
        if ((guess_row == two_ship_row and guess_col == two_ship_col) or
            (guess_row == two_sec_ship_row and guess_col == two_sec_ship_col)):
            two_board[guess_row][guess_col] = "0"
            print ""
            print ("Hit!")
            if ((two_board[two_ship_row][two_ship_col] == "0") and
                (two_board[two_sec_ship_row][two_sec_ship_col] == "0")):
                print "You won!"
                status = 5
            else:
                raw_input("Press 'Enter' to begin " + str(player_two_name) + "'s turn")
                clear_screen()
                status = 2 # Begins Player 2's turn
        else:
            if ((guess_row < 0 or guess_row > 4)
                or (guess_col < 0 or guess_col > 4)):
                print ""
                print "Your guess isn't on the grid. Try again."
            elif two_board[guess_row][guess_col] == "X":
                print ""
                print "You've already guessed this space. Try again."
            elif two_board[guess_row][guess_col] == "O":
                print ""
                print "You missed!"
                two_board[guess_row][guess_col] = "X"
                raw_input("Press 'Enter' to begin " + str(player_two_name) + "'s turn")
                clear_screen()
                status = 2
            else:
                print "Error 4: Player 2 Turn"
    else: # Something has to be here as the changing of turns, for Player 2 to
          # Player 1, causes the second layered loop (while status == 3) to
          # break. Which causes the original while loop to go through the
          # remainder of the program until it loops back around to the beginning
          # of Player 1's loop (status ==3).
        a = 0

    if status == 4: # If Player 2 wins...
        print "%s wins!" % player_two_name
        break # Breaks the initial while loop
    elif status == 5: # If Player 1 wins...
        print "Player %s wins!" % player_one_name
        break
    else: # Something has to be here as the changing of turns, for Player 2 to
          # Player 1, causes the second layered loop (while status == 3) to
          # break. Which causes the original while loop to go through the
          # remainder of the program until it loops back around to the beginning
          # of Player 1's loop (status ==3).
        a = 0
else: # Used for debugging only
    print "Error 5: End Error"

answer = raw_input("Do you want to subject yourself to another game? ")
if answer.strip() in "y Y yes Yes YES".split(): # Examines 'answer' for any
                                                # synonyms for 'yes'
    restart_program() # Restarts program if found. If not, the program
                      # terminates.
