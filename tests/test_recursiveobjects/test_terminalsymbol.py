"""This module is in charge of testing terminalsymbol.py"""

import unittest
from recursiveobjects.terminalsymbol import TerminalSymbol


class TestTerminalSymbol(unittest.TestCase):
    """This class tests the TerminalSymbol class and its functions"""
    def test_terminalsymbol_attributes(self):
        """This function tests TerminalSymbol class attributes"""
        test_value = 'testvalue'
        test_terminal_symbol = TerminalSymbol(test_value)
        self.assertEqual(test_terminal_symbol.value, test_value)

    def test_generate_sentence_fragment(self):
        """This function tests TerminalSymbol class sentence generation"""
        test_value = 'testvalue'
        test_object = TerminalSymbol(test_value)
        test_result = test_object.generate_sentence_fragment()
        # Iterate through the generator
        sentence_fragment = next(test_result)
        self.assertEqual(sentence_fragment, 'testvalue')