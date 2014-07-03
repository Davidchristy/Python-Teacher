'''
Programmers: David and Josh
Program: This is a script to teach you the basics of python programming
Dependency: Python 3.x
'''

import os
import sys
from get_input import get_input
import slideShow
import guide

user_name = ""

#a bunch of helper methods here
def menu_helper(menu_string, num_of_options):
    temp_answer = 0
    while temp_answer > num_of_options or temp_answer < 1:
        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print(menu_string)
        temp_answer = get_input.get_input()

        if not temp_answer:
            exit()

        if temp_answer.isdigit():
            temp_answer = int(temp_answer)
        else:
            temp_answer = 0

    return temp_answer

def main_menu(added_prompt = ""):
    if added_prompt:
        added_prompt += '\n'
    main_menu_text = """

    {}Welcome, {}, to the main menu. Please select the option
    you would like to learn more about.
    [1] Variables
    [2] Printing Text
    [3] Arithmetic
    [4] Boolean Logic
    [5] Game Making
    [6] Exit
    """.format(added_prompt, user_name)

    temp_answer = menu_helper(main_menu_text, 6)

    # Who needs switch statements? Functions are first-class members!
    options = [
            variables_main,
            printing_text_main,
            arithmetic_main,
            boolean_logic_main,
            game_making_main,
            exit
            ]

    options[temp_answer - 1]()

def variables_main(added_prompt = ""):
    varible_main_text = added_prompt + "\n"
    varible_main_text += "Welcome to the variables section!\n"
    varible_main_text += "[1] What are variables?\n"
    varible_main_text += "[2] Interactive guide\n"
    varible_main_text += "[3] Test your skill\n"
    varible_main_text += "[4] Back to main Menu\n"


    temp_answer = menu_helper(varible_main_text, 4)

    if temp_answer == 1:
        slideShow.SlideShow("./variables/info.txt")
        variables_main()
    if temp_answer == 2:
        guide.Guide("./variables/guide.txt")
        variables_main()
    if temp_answer == 3:
        variables_test()
    if temp_answer == 4:
        main_menu()

def variables_intro():
    print("")

def printing_text_main():
    print("printing_text")

def arithmetic_main():
    print("arithmetic")

def boolean_logic_main():
    print("boolean_logic")

def game_making_main():
    print("game_making")

def exit():
    print("Thanks for coming and hope to see you soon")
    sys.exit()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #Intro starting text
    prompt = "Hello, and welcome to this self learning python script"
    print(prompt)

    #asking for the name of the user
    global user_name
    user_name = input("What is your name?\n")

    prompt = "Hello " + user_name + ", Is this the first time you've been here? [y]/n"
    temp_question = get_input.get_input(prompt)

    if temp_question == "\n" or temp_question[0].lower() == "y":
        prompt = "Welcome! For starters we are going to"
        prompt += " start learning what variables are and move on from there."

        #sends you to the right location
        variables_main(prompt)
    else:
        prompt = "Welcome back!\n"

        #lets you pick a place to go
        main_menu(prompt)


if __name__ == '__main__':
    main()
