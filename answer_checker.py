'''
Programmer: David
Doc: a program that checks the input with a number of different tests
'''
def is_str(ans_str):
    try:
        if type("") == type(eval(ans_str)):
            return True
        return False
    except Exception: 
        return False        

def is_bool(ans_str):
    try:
        if type(True) == type(eval(ans_str)):
            return True
        return False
    except Exception: 
        return False        

def is_int(ans_str):
    try:
        if type(3) == type(eval(ans_str)):
            return True
        return False
    except Exception: 
        return False        

def is_float(ans_str):
    try:
        if type(3.3) == type(eval(ans_str)):
            return True
        return False
    except Exception: 
        return False        


methods = [is_str, is_bool, is_int, is_float]
def test_methods(ans_str):
    passing_methods = []
    for method in methods:
        #return the names of the passing methods
        if method(ans_str):
            passing_methods.append(str(method).split()[1])
    return passing_methods

def get_methods():
    '''
    Returns a list of strings with the names
    of all the methods tested
    '''
    method_str = []
    for method in methods:
            method_str.append(str(method).split()[1])
    return method_str
