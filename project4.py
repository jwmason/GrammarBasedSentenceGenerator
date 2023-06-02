# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something

from readgrammarfile import read_grammar_file, sort_grammar_list


def main() -> None:
    grammar_file = input()
    # sentence_count = int(input())
    # start_variable = input()
    result = read_grammar_file(grammar_file)
    print(result)
    print(sort_grammar_list(result))


if __name__ == '__main__':
    main()