# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something

from readgrammarfile import read_grammar_file


def main() -> None:
    grammar_file = input()
    # sentence_count = int(input())
    # start_variable = input()
    print(read_grammar_file(grammar_file))

if __name__ == '__main__':
    main()