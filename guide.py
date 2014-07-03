"""
Document this sucker
"""

import os
from get_input import get_input
import answer_checker
from learning_python_script import exit


class Guide(object):
    """docstring for Guide"""

    def print_page(self, body_text, extra_text = ""):
        counter = chr(9608)  * (self.current_q + 1) * 2
        counter += chr(9617) * (self.num_of_q - self.current_q) * 2 + "\n"
        counter += "=============================================================\n"
        page_text = counter
        
        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        page_text += body_text
        page_text += "\n" + extra_text 
        print(page_text)
    
    def run_guide(self):
        running = True
        while running:
            '''
            This is the loop keeping the whole guide running
            '''
            extra_text = ""
            passed = False
            while True:
                '''
                This is the loop keeping us in one problem until otherwise
                noted
                '''
                q = self.questions[self.current_q]
                self.print_page(self.questions[self.current_q].q_text, extra_text)

                extra_text = ""

                first_ch = get_input.get_input()
            
                if first_ch == chr(ord("")):
                    running = False
                    break

                if not first_ch:
                    exit()

                print(first_ch,end="",flush=True)
                temp_answer = input()
                temp_answer = first_ch + temp_answer
                #if the input is blank, skip everything and ask again
                if temp_answer == "":
                    continue


                passed_tests = answer_checker.test_methods(temp_answer)

                if q.q_answer in passed_tests:
                    #if it passes the right test it gets by
                    passed = True
                    

                for test in passed_tests:
                    
                    '''
                    This needs to have some upkeep done to it
                    so it looks better at giving hints
                    '''
                    if test in q.q_hints:
                        extra_text += q.q_hints[test] + "\n"
                #if the answer did was not in the passed tests
                #it might be a litteral answer typed out, see if
                #it matches
                if temp_answer == q.q_answer:
                    passed = True
                
                if passed:
                    running = self.next()
                    if running:
                        extra_text += "Congrats, you got it right!\n"
                        extra_text += "Press any key to move onto the next problem"
                    else:
                        extra_text += "You've finished this section of the guide!\n"
                        extra_text += "Press any key to go back to menu\n"
                    self.print_page(extra_text)
                    wait = get_input.get_input()
                    break

                #run through the list of hints to see if the guide file
                #file has any help for them
                for key in q.q_hints:
                    if key == temp_answer:
                        extra_text += q.q_hints[key] + "\n"

                # if extra text is still empty give the general advice
                if extra_text == "":
                    if "General" in q.q_hints:
                        extra_text += q.q_hints["General"]
                    else:
                        extra_text += "\nPlease try again"
                

    '''
    Not sure if these two work, I'm going t0 bed..self.
    '''
    def next(self):
        if self.current_q < self.num_of_q:
            self.current_q += 1
            return True
        return False

    def prev(self):
        if self.current_q > 0:
            self.current_q -= 1
            return True
        return False

    q_section = ""
    def __init__(self, file_name):
        #Opens the file with the given name
        guides_file = open(file_name, "r")
        
        self.questions = []
        #q == question
        self.current_q = -1

        for line in guides_file:
            #what section of the file is it on
            if line == "=====Question=====\n":
                q_section = "question"
                self.questions.append(Question())
                self.current_q += 1
            elif line == "=====Answer=====\n":
                q_section = "answer"

            elif line[:5] == "=====" and line[-6:] == "=====\n":
                #this section is for hints
                method = line[5:-6]
                q_section = method
                self.questions[self.current_q].q_hints[q_section] = ""
                # self.hints[method] = ""
            else:
                #depending on the section of the file
                #we want to to different things
                if q_section == "question":
                    self.questions[self.current_q].q_text += line
                elif q_section == "answer":
                    self.questions[self.current_q].q_answer += line.replace("\n","")
                else:
                    #must be a hint by this point
                    self.questions[self.current_q].q_hints[q_section] += line

        self.num_of_q = self.current_q
        self.current_q = 0

        guides_file.close()

        self.run_guide()


class Question(object):
    """docstring for Question"""
    def __init__(self):
        self.q_text = ""
        self.q_answer = ""
        self.q_hints = {}



def escape_everything(text):
    '''
    I don't think I need this any more...
    '''
    temp_text = ""
    for i in range(len(text)):
        #escaping any of the quotation marks so they don't mess up exec() method
        if text[i] == '"' or text[i] == "'":
            temp_text += "\\" + text[i]
        #if there is a \ right before quotes it means they are trying to escape something
        #Therefor we should leave it there, however things like \n should be left alone
        elif text[i] == '\\' and i > 0 and (text[i + 1] == '"' or text[i + 1] == "'"):
            temp_text += "\\" + text[i]
        else:         
            temp_text += text[i]
    return temp_text

    

def main():

    temp = Guide("./variables/guide.txt")
    

if __name__ == '__main__':
    main()

