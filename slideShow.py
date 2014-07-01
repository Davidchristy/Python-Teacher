'''
A small class to make a slide show of infomation
'''
import os
import sys
#needed for instant input
import termios
import contextlib
from get_input import get_input



class SlideShow(object):
    """docstring for Slideshow"""
    def __init__(self, file_name):
        #Opens the file with the given name
        slides_file = open(file_name, "r")

        self.page_text = ["",""]
        self.current_page = 1

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
        help_info += "To move to beginning press 'w', while moving to end is 's'\n"
        help_info += "To leave the slideshow press 'q'\n"
        self.page_text[0] = help_info + self.page_text[0]
    
        for current_page in range(len(self.page_text)):
            #at the bottom of every page, there should be a counter
            # with slide number and slides remaining
            counter = chr(9608)  * (current_page + 1) * 2
            counter += chr(9617) * (self.num_of_pages - current_page) * 2 + "\n"
            counter += "=============================================================\n\n"
            self.page_text[current_page] = counter + self.page_text[current_page]

        self.run_slide_show()

    def run_slide_show(self):
        while True:
            self.print_page()

            temp_input = get_input.get_input()
            if not temp_input or temp_input == chr(4) or temp_input == chr(113):
                break
            if ord(temp_input) == 97:
                self.prev_page()
            if ord(temp_input) == 100:
                self.next_page()
            if ord(temp_input) == 119:
                self.go_to_start()
            if ord(temp_input) == 115:
                self.go_to_end()

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
