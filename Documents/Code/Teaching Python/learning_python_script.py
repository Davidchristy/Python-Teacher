'''
Programmer: David
Program: This is a script to teach you the basics of python programming
Dependency: Python 3.x
'''

import os
user_name = ""

#a bunch of helper methods here
def menu_helper(menu_string, num_of_options):
    temp_answer = 0
    while temp_answer > num_of_options or temp_answer < 1:
        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(menu_string)
        temp_answer = input()

        if temp_answer.isdigit():
            temp_answer = int(temp_answer)
        else:
            temp_answer = 0

    return temp_answer

def main_menu():
    main_menu_text = "Welcome " + user_name + ", to the main menu please select the option"
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

def varibles_main():
    varible_main_text = "Welcome to the varibles section!\n"
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
    user_name = input("What is a name I can call you by?\n")
    
    prompt = "Hello " + user_name + ", Is this the first time you're here? [y]\n"
    temp_question = input(prompt)

    if temp_question == "" or temp_question[0].lower() == "y":
        prompt = "Welcome! For starters we are going to"
        prompt += " start learning what varibles are and move on from there."
        print(prompt)
        #sends you to the right location
        varibles_main()
    else:
        prompt = "Welcome back!\n"
        print(prompt)
        #lets you pick a place to go
        main_menu()


if __name__ == '__main__':
    main()