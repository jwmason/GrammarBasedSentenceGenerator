"""This module is in charge of testing readgrammarfile.py"""

import unittest
import tempfile
import os
from readgrammarfile import read_grammar_file, sort_grammar_list


class TestReadGrammarFile(unittest.TestCase):
    """Tests read_grammar_file()"""
    def test_read_grammar_file(self):
        """This tests the read_grammar_file()"""
        expected_result = ['line1', 'line2', 'line3']
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'line1\nline2\nline3\n')
            temp_file.seek(0)
            result = read_grammar_file(temp_file.name)
        self.assertEqual(result, expected_result)
        os.remove(temp_file.name)


class TestSortGrammarList(unittest.TestCase):
    """Tests sort_grammar_list()"""
    def test_sort_grammar_list(self):
        """Tests overall functionality"""
        # Test with a single pair of braces
        my_list = [1, 2, "{", 3, 4, "}", 5, 6]
        expected_result = [[3, 4]]
        result = sort_grammar_list(my_list)
        self.assertEqual(result, expected_result)

    def test_multiple_pairs(self):
        """Test with multiple pairs of braces"""
        my_list = [1, 2, "{", 3, 4, "}", "{", 5, 6, 7, "}", 8]
        expected_result = [[3, 4], [5, 6, 7]]
        result = sort_grammar_list(my_list)
        self.assertEqual(result, expected_result)

    def test_no_pairs(self):
        """Test with no pairs of braces"""
        my_list = [1, 2, 3, 4, 5]
        expected_result = []
        result = sort_grammar_list(my_list)
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        """Test with an empty list"""
        my_list = []
        expected_result = []
        result = sort_grammar_list(my_list)
        self.assertEqual(result, expected_result)

    def test_no_open_brace(self):
        """Test with no open brace"""
        my_list = [1, 2, "}", 3, 4]
        expected_result = []
        result = sort_grammar_list(my_list)
        self.assertEqual(result, expected_result)