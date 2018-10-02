import random
import os

#hangman function - accepts 'word' variable as parameter
#player 2 must guess this word
#the variable 'wrong' is used to keep up with how many incorrect letters have been guessed
#'stages' variable  is a list of strings that draws the hangman
#'rletters' variable is a list containing each character in variable 'word', keeping track of unguessed letters
#'board' variable is a list of strings used to keep track of hints (guessed letters in word)
#'win' variable keeps track of whether or not the game has been won
def hangman(word):
    wrong = 0 
    stages = ["",
                   "________                        ",
                   "|                               ",
                   "|               |               ",
                   "|              O                ",
                   "|             / | \             ",      
                   "|              / \              ",
                   "|                               "
                    ]
    rletters = list(word)
    board = ["__"] * len(word) #populates board list
    win = False
    print("Welcome to Hangman")
    
    #loop that keeps the game going
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                .index(char)
            board[cind] = char
            rletters[cind] = '$'#only first occurrence of character is found, this changes it for next time around
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True 
            break#if True, loop is broken and game is over
            #if not True, hangman and "You Lose!" are printed
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You Lose! It was " + "'" + "{}".format(word) +"'.")

        

os.path.join("dict.txt" )
word = open("dict.txt").read()

print(word[0:9])

#print(word.split(" ", 1)[0])

#hangman(text)   
   
   
   
   
   
   
   

   
