# from __future__ import print_function
# import torch
from what_is_pytorch import examples as wip


def p(text, newlines=3):
    """Another print option
    
    Arguments:
        text {string} -- text to print in a slightly formatted way.
        newlines {int} -- number of preceding new lines to print
    """
    nl = '\n' * int(newlines)
    print(f'{nl}{text}:\n')