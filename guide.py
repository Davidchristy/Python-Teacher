"""
Document this sucker

"""

import os
from get_input import get_input

class Guide(object):
    """docstring for Guide"""

    def run_tests(self, q, temp_answer):
        output = ""
        for hint in q.hints:
            exec(hint)
            # output += "lol"
        print(output)
        wait = input()

    def run_guide(self):
        for q in self.questions:
            passed = False
            while True:
                print_page(q)
                temp_answer = input()
                passed = eval(q.q_answer)
                if passed:
                    break
                self.run_tests(q, temp_answer)


    q_section = ""

    def __init__(self, file_name):
        #Opens the file with the given name
        guides_file = open(file_name, "r")
        
        self.questions = []
        #q == question
        self.current_q = 0
        curr_hint_text = ""

        for line in guides_file:
            #what section of the file is it on
            if line == "=====Question=====\n":
                q_section = "question"
                self.questions.append(Question())
            elif line == "=====Answer=====\n":
                q_section = "answer"
            elif line == "=====Hint=====\n":
                q_section = "hint"
                # curr_hint_text = escape_everything(curr_hint_text)
                self.questions[self.current_q].hints.append(curr_hint_text)
                curr_hint_text = ""
            elif line == "=====End_Question=====\n":
                if q_section == "hint":
                    # curr_hint_text = escape_everything(curr_hint_text)
                    self.questions[self.current_q].hints.append(curr_hint_text)
                    #getting rid of empty first element
                    self.questions[self.current_q].hints = self.questions[self.current_q].hints[1:]
                    curr_hint_text = ""
                    self.current_q += 1
            else:
            #depending on the section of the file
            #we want to to different things
                if q_section == "question":
                    self.questions[self.current_q].q_text += line
                if q_section == "answer":
                    self.questions[self.current_q].q_answer += line
                if q_section == "hint":
                    curr_hint_text += line

        self.num_of_q = self.current_q + 1
        self.current_q = 0

        guides_file.close()


        self.run_guide()



class Question(object):
    """docstring for Question"""
    def __init__(self):
        self.q_text = ""
        self.q_answer = ""
        self.hints = []        

def print_page(question, hint_needed = -1):
        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        page_text = ""
        for line in question.q_text:
            page_text += line
        print(page_text)


def escape_everything(text):
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
    '''
    There might be trouble down the road to use eval or exec...
    '''



    temp = Guide("./variables/guide.txt")
    

if __name__ == '__main__':
    main()