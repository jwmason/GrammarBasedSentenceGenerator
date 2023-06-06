"""This module is in charge of handling grammar"""

class Grammar:
    """This class creates a Grammar object"""
    def __init__(self):
        """This initializes attributes of the object"""
        self.rules = {}

    def add_rule(self, rule):
        """This adds a key and value to the rules dictionary"""
        self.rules[rule.variable] = rule

    def get_rule(self, variable):
        """This gets a value of a rule based on the key"""
        return self.rules[variable]

    def generate_sentence(self, start_variable):
        """This recursively calls on the rule generate_sentence_fragment() function
        after getting the starting rule"""
        rule = self.get_rule(start_variable)
        yield from rule.generate_sentence_fragment()
