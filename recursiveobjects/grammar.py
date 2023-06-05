"""This module is in charge of handling grammar"""

class Grammar:
    def __init__(self):
        self.rules = {}

    def add_rule(self, rule):
        self.rules[rule.variable] = rule

    def generate_sentence_fragment(self):
        pass