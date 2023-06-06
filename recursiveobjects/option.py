"""This module is in charge of handling options"""

class Option:
    """This class creates an Option object"""
    def __init__(self, probability, symbols):
        """This initializes the attributes of the Option object"""
        self.probability = probability
        self.symbols = symbols

    def generate_sentence_fragment(self):
        """This function generates sentence fragment based on if the symbol
        is a Terminal or Variable Symbol"""
        for symbol in self.symbols:
            yield from symbol.generate_sentence_fragment()
