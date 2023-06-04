"""This module is in charge of testing option.py"""

import unittest
from recursiveobjects.option import Option


class TestOption(unittest.TestCase):
    """This class tests the Option class and its functions"""
    def test_option_attributes(self):
        """This function tests option class attributes"""
        test_option = Option(1, 'TerminalSymbolPlaceHolder')
        self.assertEqual(test_option.probability, 1)
        self.assertEqual(test_option.symbols, 'TerminalSymbolPlaceHolder')