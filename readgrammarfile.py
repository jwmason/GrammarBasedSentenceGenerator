"""This module is in charge of reading the grammar file"""

def read_grammar_file(grammar_file) -> list:
    """This reads the contents of the file"""
    grammar_list = []
    with open(grammar_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            grammar_list.append(line)
    return grammar_list
