"""This module is in charge of handling variable symbols"""

class VariableSymbol:
    """This class creates a variable symbol object"""
    def __init__(self, name, grammar):
        """This initiates the object's attributes"""
        self.name = name
        self.grammar = grammar

    def generate_sentence_fragment(self):
        """This function generates a sentence fragment based on the object"""
        # Gets the rule object associated with the variable name
        rule = self.grammar.get_rule(self.name)
        yield from rule.generate_sentence_fragment()
