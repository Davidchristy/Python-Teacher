"""
Since many different files in the project need to collect input
I made this file so these methods aren't repeated many times


to call this frist have this line
from get_input import get_input

than call the method get_input.get_input()

I really need better names...but it works!
"""

import os
import sys
import termios
import contextlib

class get_input(object):
    """
    docstring for input_collector
    remember to document this
    """

    @classmethod        
    def get_input(self, prompt = ""):
        print(prompt)
        #As of now this only works with Unix computer, I'll get windows working soon
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

