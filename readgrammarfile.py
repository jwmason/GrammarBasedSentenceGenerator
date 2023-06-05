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


def sort_grammar_list(grammar_list) -> list:
    """This sorts the contents of the list"""
    grammar_list_of_lists = []
    stack = []
    for item in grammar_list:
        if item == "{":
            stack.append([])
        elif item == "}":
            if stack:
                grammar_list_of_lists.append(stack.pop())
        else:
            if stack:
                stack[-1].append(item)
    return grammar_list_of_lists