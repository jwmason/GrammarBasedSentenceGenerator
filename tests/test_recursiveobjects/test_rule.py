"""This module is in charge of testing rule.py"""

import unittest
from recursiveobjects.rule import Rule
from recursiveobjects.terminalsymbol import TerminalSymbol
from recursiveobjects.option import Option


class TestRule(unittest.TestCase):
    """This class tests the Rule class and its functions"""
    def test_rule_attributes(self):
        """This function tests rule class attributes"""
        test_var = 'testvar'
        test_option = 'testoptionclassnotimplementedyet'
        test_rule = Rule(test_var, test_option)
        self.assertEqual(test_rule.variable, test_var)
        self.assertEqual(test_rule.options, test_option)

    def test_generate_sentence_fragment(self):
        """This function tests generate_sentence_fragment()"""
        terminal = TerminalSymbol('test')
        test_option = Option(1, [terminal])
        test_rule = Rule('test', [test_option])
        generator = test_rule.generate_sentence_fragment()
        sentence_fragment = next(generator)
        self.assertEqual(sentence_fragment, 'test')