# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something

from readgrammarfile import read_grammar_file, sort_grammar_list
from parsegrammarfile import parse_grammar_list

def main() -> None:
    grammar_file = input()
    sentence_count = int(input())
    start_variable = input()
    grammar_list = read_grammar_file(grammar_file)
    sorted_grammar_list_of_lists = sort_grammar_list(grammar_list)
    grammar = parse_grammar_list(sorted_grammar_list_of_lists)

    for _ in range(sentence_count):
        sentence = grammar.generate_sentence(start_variable)
        print(' '.join(sentence))

if __name__ == '__main__':
  main()
