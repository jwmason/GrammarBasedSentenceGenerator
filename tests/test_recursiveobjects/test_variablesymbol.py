"""This module is in charge of testing variablesymbol.py"""

import unittest
from recursiveobjects.variablesymbol import VariableSymbol
from recursiveobjects.grammar import Grammar
from recursiveobjects.rule import Rule
from recursiveobjects.option import Option
from recursiveobjects.terminalsymbol import TerminalSymbol


class TestVariableSymbol(unittest.TestCase):
    """This class tests the VariableSymbol class and its functions"""
    def test_variablesymbol_attributes(self):
        """This function tests VariableSymbol class attributes"""
        test_var = 'testvar'
        test_grammar = 'GrammarClassPlaceHolder'
        test_variable_symbol = VariableSymbol(test_var, test_grammar)
        self.assertEqual(test_variable_symbol.name, test_var)
        self.assertEqual(test_variable_symbol.grammar, test_grammar)

    def test_generate_sentence_fragment(self):
        """This tests the generate_sentence_fragment()"""
        grammar = Grammar()
        test_option = Option(1, [TerminalSymbol('testresult')])
        test_rule = Rule('test', [test_option])
        grammar.rules['test'] = test_rule
        variablesymbol = VariableSymbol('test', grammar)
        generator = variablesymbol.generate_sentence_fragment()
        result = ' '.join(str(fragment) for fragment in generator)
        self.assertEqual(result, 'testresult')
