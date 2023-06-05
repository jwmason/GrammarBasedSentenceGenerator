"""This module is in charge of handling variable symbols"""

class VariableSymbol:
    """This class creates a variable symbol object"""
    def __init__(self, name, grammar):
        """This initiates the object's attributes"""
        self.name = name
        self.grammar = grammar

    def generate_sentence_fragment(self):
        pass