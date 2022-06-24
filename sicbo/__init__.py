__author__ = 'Deza Farras Tsany<deza.ftsany@gmail.com>'
__version__ = '1.0.0'

from .shuffleDice import (SicboDice)

def getDice():
    """
    This function will determine the results of shuffling the dice that will be used in the Sicbo game.
    """
    return SicboDice().getDice()