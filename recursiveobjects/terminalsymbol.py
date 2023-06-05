"""This module is in charge of handling terminal symbols"""

class TerminalSymbol:
    """This class creates a terminal symbol object"""
    def __init__(self, value):
        """This initiates the object's attributes"""
        self.value = value

    def generate_sentence_fragment(self):
        """This function generates a sentence fragment based on the object"""
        yield self.value