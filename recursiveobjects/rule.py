"""This module is in charge of handling rules"""

import random


class Rule:
    """This class creates a Rule object"""
    def __init__(self, variable, options):
        """This initializes the attributes of the object"""
        self.variable = variable
        self.options = options

    def generate_sentence_fragment(self):
        """This function calls on the option generate_sentence_fragment(), using recursion.
        It also calculates the chances of a certain option occurring based on its probability"""
        # Makes a list comprehension of all the probabilities
        option_list = [option.probability for option in self.options]
        # Chooses an option based on probability using 'random' function
        option = random.choices(self.options, option_list)[0]
        yield from option.generate_sentence_fragment()
