'''
Entry node to be created for hash table lists.
Has 3 types of entries - constant, function, and variable.
All inherit from a generice Entry class
'''


from enum import IntEnum


'''Parent entry class'''
class Entry:
    def __init__(self, lexeme, token, depth):
        self.lexeme = lexeme
        self.token = token
        self.depth = depth
        self.entry_type = None # will hold entry type enum
        self.entry_details = None # will hold var, const, or func entry data 
        self.next = None


class Variable_Entry():
    def __init__(self):
        self.var_type = None
        self.offset = None
        self.size = None


class Constant_Entry():
    def __init__(self):
        self.var_type = None
        self.offset = None
        self.value = None


class Function_Entry():
    def __init__(self):
        self.size_of_local = 0
        self.num_of_params = 0
        self.return_type = None
        self.param_list = None

class Literal_Entry():
    def __init__(self):
        self.value = ""


'''Node to create a single paramenter entry for the function_entry parameter list'''
class Param_Node:
    def __init__(self):
        self.param_type = None
        self.next = None


'''Enumerated variable type'''
class Var_Type(IntEnum):
    charType = 0
    intType = 1
    floatType = 2


'''Enumerated entry type to specify in Entry'''
class Entry_Type(IntEnum):
    constEntry = 0
    varEntry = 1
    functionEntry = 2
    stringEntry = 3
