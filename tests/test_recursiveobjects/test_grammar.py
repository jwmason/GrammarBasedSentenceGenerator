"""This module is in charge of testing grammar.py"""

import unittest
from recursiveobjects.grammar import Grammar


class TestGrammar(unittest.TestCase):
    """This class tests the Grammar class and its functions"""
    def test_grammar_attributes(self):
        """This function tests grammar class attributes"""
        test_grammar = Grammar()
        test_grammar.rules['testkey'] = 'testvalue'
        self.assertEqual(test_grammar.rules, {'testkey': 'testvalue'})