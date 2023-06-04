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