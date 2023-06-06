"""This module is in charge of testing option.py"""

import unittest
from recursiveobjects.option import Option
from recursiveobjects.terminalsymbol import TerminalSymbol


class TestOption(unittest.TestCase):
    """This class tests the Option class and its functions"""
    def test_option_attributes(self):
        """This function tests option class attributes"""
        test_option = Option(1, 'TerminalSymbolPlaceHolder')
        self.assertEqual(test_option.probability, 1)
        self.assertEqual(test_option.symbols, 'TerminalSymbolPlaceHolder')

    def test_generate_sentence_fragment(self):
        """This function tests generate_sentence_fragment()"""
        terminal = TerminalSymbol('test')
        test_option = Option(1, [terminal])
        generator = test_option.generate_sentence_fragment()
        sentence_fragment = next(generator)
        self.assertEqual(sentence_fragment, 'test')

    def test_generate_sentence_fragment_no_symbols(self):
        """This function tests generate_sentence_fragment() with no symbols"""
        test_option = Option(1, [])
        generator = test_option.generate_sentence_fragment()
        self.assertRaises(StopIteration, next, generator)