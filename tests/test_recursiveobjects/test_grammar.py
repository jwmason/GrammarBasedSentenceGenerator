"""This module is in charge of testing grammar.py"""

import unittest
from recursiveobjects.grammar import Grammar
from recursiveobjects.rule import Rule
from recursiveobjects.option import Option
from recursiveobjects.terminalsymbol import TerminalSymbol


class TestGrammar(unittest.TestCase):
    """This class tests the Grammar class and its functions"""
    def test_grammar_attributes(self):
        """This function tests grammar class attributes"""
        test_grammar = Grammar()
        test_grammar.rules['testkey'] = 'testvalue'
        self.assertEqual(test_grammar.rules, {'testkey': 'testvalue'})

    def test_add_rule(self):
        """This function tests add_rule()"""
        test_grammar = Grammar()
        test_symbol = TerminalSymbol('testsymbol')
        test_option = Option(1, [test_symbol])
        rule = Rule('A', test_option)
        test_grammar.add_rule(rule)
        self.assertEqual(test_grammar.rules['A'], rule)

    def test_get_rule(self):
        """This function tests get_rule()"""
        test_grammar = Grammar()
        test_symbol = TerminalSymbol('testsymbol')
        test_option = Option(1, [test_symbol])
        rule = Rule('A', test_option)
        test_grammar.add_rule(rule)
        retrieved_rule = test_grammar.get_rule('A')
        self.assertEqual(retrieved_rule, rule)

    def test_generate_sentence_fragment(self):
        """This function tests generate_sentence_fragment()"""
        test_grammar = Grammar()
        test_symbol = TerminalSymbol('testsymbol')
        test_option = Option(1, [test_symbol])
        rule = Rule('A', [test_option])
        test_grammar.add_rule(rule)
        retrieved_rule = test_grammar.generate_sentence('A')
        result = next(retrieved_rule)
        self.assertEqual(result, 'testsymbol')