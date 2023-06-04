"""This module is in charge of handling variable symbols"""

class VariableSymbol:
    def __init__(self, name, grammar):
        self.name = name
        self.grammar = grammar

    def generate_sentence_fragment(self):
        pass