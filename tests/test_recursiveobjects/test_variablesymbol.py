"""This module is in charge of testing variablesymbol.py"""

import unittest
import inspect
from recursiveobjects.variablesymbol import VariableSymbol
from recursiveobjects.grammar import Grammar
from recursiveobjects.rule import Rule


class TestVariableSymbol(unittest.TestCase):
    """This class tests the VariableSymbol class and its functions"""
    def test_variablesymbol_attributes(self):
        """This function tests VariableSymbol class attributes"""
        test_var = 'testvar'
        test_grammar = 'GrammarClassPlaceHolder'
        test_variable_symbol = VariableSymbol(test_var, test_grammar)
        self.assertEqual(test_variable_symbol.name, test_var)
        self.assertEqual(test_variable_symbol.grammar, test_grammar)

    # Fix this test after completing Rule class
    def test_generate_sentence_fragment(self):
        grammar = Grammar()
        rule = Rule('test', 'testoptions')
        grammar.rules['test'] = rule
        variablesymbol = VariableSymbol('test', grammar)
        generator = variablesymbol.generate_sentence_fragment()
