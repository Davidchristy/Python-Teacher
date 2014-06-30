'''
Programmer: David
Program: This is a script to teach you the basics of python programming
Dependency: Python 3.x
'''

import os
import sys
#needed for instant input
import termios
import contextlib

user_name = ""

#a bunch of helper methods here
def menu_helper(menu_string, num_of_options):
    temp_answer = 0
    while temp_answer > num_of_options or temp_answer < 1:
        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(menu_string)
        temp_answer = get_input()

        if temp_answer.isdigit():
            temp_answer = int(temp_answer)
        else:
            temp_answer = 0
    
    return temp_answer

def get_input(prompt = ""):
    #As of now this only works with Unix computer, I'll get windows working soon
    print(prompt)
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == chr(4):
                    break
                return ch
        except (KeyboardInterrupt, EOFError):
            pass

#This method came from here:
# http://stackoverflow.com/questions/11918999/key-listeners-in-python
@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)
    

def main_menu(added_prompt = ""):
    main_menu_text = added_prompt
    main_menu_text += "Welcome " + user_name + ", to the main menu please select the option"
    main_menu_text += " you want to learn more about.\n\n"
    main_menu_text += "[1] Varibles\n"
    main_menu_text += "[2] Printing Text\n"
    main_menu_text += "[3] Arithmetic\n"
    main_menu_text += "[4] Boolean Logic\n"
    main_menu_text += "[5] Game Making\n"
    main_menu_text += "[6] Exit\n"

    temp_answer = menu_helper(main_menu_text, 6)
    
    #What? No Case switch in python? oh well, time to go old style
    if temp_answer == 1:
        varibles_main()
    if temp_answer == 2:
        printing_text_main()
    if temp_answer == 3:
        arithmetic_main()
    if temp_answer == 4:
        boolean_logic+main()
    if temp_answer == 5:
        game_making_main()
    if temp_answer == 6:
        exit()

def varibles_main(added_prompt = ""):
    varible_main_text = added_prompt + "\n"
    varible_main_text += "Welcome to the varibles section!\n"
    varible_main_text += "[1] What are varibles?\n"
    varible_main_text += "[2] Interactive guide\n"
    varible_main_text += "[3] Test your skill\n"
    varible_main_text += "[4] Back to main Menu\n"


    temp_answer = menu_helper(varible_main_text, 4)

    if temp_answer == 1:
        varibles_intro()
    if temp_answer == 2:
        varibles_guides()
    if temp_answer == 3:
        varibles_test()
    if temp_answer == 4:
        main_menu()

def varibles_intro():
    print("")

def printing_text():
    print("printing_text")

def arithmetic():
    print("arithmetic")

def boolean_logic():
    print("boolean_logic")

def game_making():
    print("game_making")

def exit():
    print("Thanks for coming and hope to see you soon")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #Intro starting text
    prompt = "Hello, and welcome to this self learning python script"
    print(prompt)

    #asking for the name of the user
    global user_name  
    user_name = input("What is your name?\n")
    
    prompt = "Hello " + user_name + ", Is this the first time you've been here? [y]/n"
    temp_question = get_input(prompt)

    if temp_question == "\n" or temp_question[0].lower() == "y":
        prompt = "Welcome! For starters we are going to"
        prompt += " start learning what varibles are and move on from there."

        #sends you to the right location
        varibles_main(prompt)
    else:
        prompt = "Welcome back!\n"

        #lets you pick a place to go
        main_menu(prompt)


if __name__ == '__main__':
    main()