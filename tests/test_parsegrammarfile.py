"""This module is in charge of testing readgrammarfile.py"""

import unittest
from parsegrammarfile import parse_grammar_list


class TestParsingFunctions(unittest.TestCase):
    """This class tests parsegrammarfile.py"""
    def test_parsing(self):
        """This function tests parsing of grammar list and symbols"""
        grammar_list_of_lists = [
            ['HowIsBoo', '1 Boo is [Adjective] today'],
            ['Adjective', '1 happy', '1 perfect', '1 relaxing']
        ]
        grammar = parse_grammar_list(grammar_list_of_lists)
        self.assertEqual(len(grammar.rules), 0)
