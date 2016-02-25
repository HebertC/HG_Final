from random import randrange
from tkinter import *
import sys


def draw_man(option):
    if option == 1:
        # Create the base
        C.create_line(580, 150, 580, 350, width=4, fill="darkblue")
        C.create_line(450, 350, 595, 350, width=4, fill="darkblue")
        # create the head
        C.create_oval(510, 150, 560, 200, width=2, fill='PeachPuff')


    if option == 2:
        # create the middle part
        C.create_line(535, 200, 535, 290, width=2)

    if option == 3:
        # Create the left leg
        C.create_line(535, 290, 510, 320, 500, 320, width=2)

    if option == 4:
        # create the right leg
        C.create_line(535, 290, 560, 320, 550, 320, width=2)

    if option == 5:
        # Create the left hand
        C.create_line(535, 230, 510, 250, 500, 250, width=2)

    if option == 6:
        # Create right hand
        C.create_line(535, 230, 560, 250, 550, 270, width=2)

    if option == 7:
        # Create the string
        C.create_line(535, 210, 580, 210, width=4, fill="darkblue")
        #Create the X
        C.create_line(450, 350, 595, 150 , width= 5 , fill='red' )
        C.create_line(450, 150, 595, 350, width=5 , fill='red')


def get_word():
    global secret_word, opportunities, game_end, wrong_guess, guess_word, letters

    # open the documents of words
    # only reading
    try:
        fp = open("Countries.txt", "r")
    except IOError:
        print("The application cant open the document ")
        sys.exit()


    # get a random number
    num = randrange(1, 118, 1)

    # getting the word to guess for the user
    for i in range(1, 118, 1):
        if i == num:
            secret_word = (fp.readline()).split(" ")
        else:
            fp.readline()
    fp.close()

    # list to show to the user
    guess_word = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # to show the list of the wrong letters for the user
    letters = [" ", " ", " ", " ", " ", " ", " "]

    # game variables
    opportunities = 7
    game_end = 0
    # number of wrong guesses
    wrong_guess = 0

    i = 0
    while i < len(secret_word) - 1:
        guess_word[i] = '_'
        i = i + 1

    # J: to position the J letter to the right .
    i = 0
    j = 0
    while i < len(secret_word) - 1:
        C.create_text(50 + j, 200, text=guess_word[i], font='Times', fill='blue')
        j = j + 20
        i = i + 1


def hangman():
    global single_letter, opportunities, secret_word, game_end, wrong_guess, guess_word, letters
    # self.entry.delete(0, 'end')
    i = 0
    letter_counter = 0
    """
    get the input text length and make sure it must be single character
    """
    if len(single_letter.get()) != 1:
       # Modification of text event
        C.create_text(
            75, 370, text="Please Enter One LETTER At One Time", font='Times 10 bold', fill='blue',tag='del_text' )
    else:
        while i < len(secret_word) - 1:
            #delete the text warning
            C.delete("del_text")
            # put the upper method to convert the in put character in upper
            # case
            if secret_word[i] == single_letter.get().upper():
                guess_word[i] = single_letter.get()
                letter_counter = 1
            i = i + 1
        print ("Guessing", secret_word)
        print ("WORD", guess_word)
        if letter_counter == 0:
            opportunities = opportunities - 1
            letters[wrong_guess] = single_letter.get()
            wrong_guess = wrong_guess + 1

        i = 0
        j = 0
        while i < len(guess_word) - 1:
            C.create_text(
                50 + j, 200, text=guess_word[i], font='Times', fill='blue')
            j = j + 20
            i = i + 1

        i = 0
        j = 0
        while i < len(letters) - 1:
            C.create_text(
                50 + j, 320, text=letters[i], font='Times', fill='blue')
            j = j + 20
            i = i + 1

        if wrong_guess == 1:
            draw_man(1)
        if wrong_guess == 2:
            draw_man(2)
        if wrong_guess == 3:
            draw_man(3)
        if wrong_guess == 4:
            draw_man(4)
        if wrong_guess == 5:
            draw_man(5)
        if wrong_guess == 6:
            draw_man(6)
        if wrong_guess == 7:
            draw_man(7)

        # to check if I lost the game
        if opportunities == 0:
            C.create_text(
                75, 370, text="You LOST", font='Times 10 bold', fill='blue')
            C.create_text(100 , 400,text="THE WORDS WAS ", font='Times 10 bold', fill='blue')
            i = 0
            j = 0
            while i < len(secret_word) - 1:
                C.create_text(
                    50 + j, 420, text=secret_word[i], font='Times 10 bold', fill='blue')
                j = j + 20
                i = i + 1
                #boton.tkButtonLeave()

    # to check if I won the game
    i = 0
    full_word = 0
    while i < len(guess_word) - 1:
        if guess_word[i] != '_':
            full_word = full_word + 1
        i = i + 1

    if full_word == len(guess_word) - 1:
        C.create_text(
            75, 370, text="You Won!!!", font='Times 14 bold', fill='blue')
        #boton.tkButtonLeave()

    entry_text.delete(0, END)


# -------------------------------------------------------------------
#                                game
# -------------------------------------------------------------------

root = Tk()
title1 = 'Hangman Game'
title2 = '\n\nUSE ANY OF THESE LETTERS \n\nA B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
C = Canvas(root, width=600, height=450, background='ivory')
C.create_text(300, 70, justify='center', text=title1 + title2,
              font='Times 14 bold', fill='blue')

# elements to position on the canvas

single_letter = StringVar()
instruction_label = Label(root, text="ENTER A LETTER : ")
entry_text = Entry(root, textvariable=single_letter)
play_button = Button(root, text=" P  L  A  Y  ", command=hangman, width=20)
exit_button = Button(root, text="E  X  I  T", command=C.quit, width=20)
C.grid(row=1, column=1, columnspan=4)
instruction_label.grid(row=2, column=1)
entry_text.grid(row=2, column=2)
play_button.grid(row=2, column=3)
exit_button.grid(row=2, column=4)

# to get the word
get_word()
#to loop all the events
root.mainloop()
