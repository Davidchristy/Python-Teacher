'''
A small program to make a slide show of infomation
'''
import os
import sys
#needed for instant input
import termios
import contextlib

def get_input(prompt = ""):
    '''
    This bit of code for get_input was copied from learning_python_script

    It might be a good idea later to put in helper .py file and just import it
    '''
    #As of now this only works with Unix computer, I'll get windows working soon
    print(prompt)
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == chr(4):
                    break
                return ord(ch)
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



class Slideshow(object):
    """docstring for Slideshow"""
    def __init__(self, file_name):
        #Opens the file with the given name
        slides_file = open(file_name, "r")

        self.page_text = [""]
        self.current_page = 0

        for line in slides_file:
            #right now it's 5 equal signs, but might (will) change it later 
            if line == "=====\n":
                self.current_page += 1
                self.page_text.append("")
            else:
                self.page_text[self.current_page] += line

        self.num_of_pages = self.current_page
        self.current_page = 0

        slides_file.close()


        #adds help infomation on the first page, to any slideshow
        help_info = "You can move through the slideshow using the 'a' and 'd' keys\n"
        help_info += "To move to beginning press 'w', while moving to end is 's'\n\n"
        self.page_text[0] = help_info + self.page_text[0]
    
        for current_page in range(len(self.page_text)):
            #at the bottom of every page, there should be a counter
            # with slide number and slides remaining
            self.page_text[current_page] = (chr(9608))  * (current_page + 1) + "[]" * (self.num_of_pages - current_page) + "\n" + self.page_text[current_page]

    def go_to_start(self):
        self.current_page = 0

    def go_to_end(self):
        self.current_page = self.num_of_pages

    def next_page(self):
        print("It gets here?")
        if self.current_page < self.num_of_pages:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def print_page(self):

        #clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        page_text = ""
        for line in self.page_text[self.current_page]:
            page_text += line
        print(page_text)

def main():
    '''
    a slideshow program??

    a weird error with the the read byte method
    When an arrow key is pressed it's read a 3 bytes
    which I don't think will help...
    I have temporary fixed the problem by making the direction keys
    '''
    show = Slideshow("./testSlideShow")

    while True:

        show.print_page()

        temp_input = get_input()
        if not temp_input or temp_input == chr(4):
            break

        if temp_input == 97:
            show.prev_page()
        if temp_input == 100:
            show.next_page()
        if temp_input == 119:
            show.go_to_start()
        if temp_input == 115:
            show.go_to_end()
        

if __name__ == '__main__':
    main()