"""This module is in charge of testing variablesymbol.py"""

import unittest
from recursiveobjects.variablesymbol import VariableSymbol


class TestVariableSymbol(unittest.TestCase):
    """This class tests the VariableSymbol class and its functions"""
    def test_variablesymbol_attributes(self):
        """This function tests VariableSymbol class attributes"""
        test_var = 'testvar'
        test_grammar = 'GrammarClassPlaceHolder'
        test_variable_symbol = VariableSymbol(test_var, test_grammar)
        self.assertEqual(test_variable_symbol.name, test_var)
        self.assertEqual(test_variable_symbol.grammar, test_grammar)