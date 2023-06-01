"""This module is in charge of testing readgrammarfile.py"""

import unittest
import tempfile
import os
from readgrammarfile import read_grammar_file


class TestReadGrammarFile(unittest.TestCase):
    def test_read_grammar_file(self):
        """This tests the read_grammar_file()"""
        expected_result = ['line1', 'line2', 'line3']
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'line1\nline2\nline3\n')
            temp_file.seek(0)
            result = read_grammar_file(temp_file.name)
        self.assertEqual(result, expected_result)
        os.remove(temp_file.name)


if __name__ == '__main__':
    unittest.main()
