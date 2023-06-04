"""This module is in charge of handling options"""

class Option:
    def __init__(self, probability, symbols):
        self.probability = probability
        self.symbols = symbols

    def generate_sentence_fragment(self):
        pass