"""This module is in charge of testing rule.py"""

import unittest
from recursiveobjects.rule import Rule


class TestRule(unittest.TestCase):
    """This class tests the Rule class and its functions"""
    def test_rule_attributes(self):
        """This function tests rule class attributes"""
        test_var = 'testvar'
        test_option = 'testoptionclassnotimplementedyet'
        test_rule = Rule(test_var, test_option)
        test_rule.rules['testkey'] = 'testvalue'
        self.assertEqual(test_rule.variable, test_var)
        self.assertEqual(test_rule.options, test_option)