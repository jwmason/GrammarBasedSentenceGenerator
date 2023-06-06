"""This module is in charge of parsing the grammar file"""

from recursiveobjects.grammar import Grammar
from recursiveobjects.rule import Rule
from recursiveobjects.option import Option
from recursiveobjects.terminalsymbol import TerminalSymbol
from recursiveobjects.variablesymbol import VariableSymbol


def parse_grammar_list(grammar_list_of_lists) -> Grammar:
    """This module is in charge of returning grammar class based on grammar list"""
    # Initialize Grammar object
    grammar = Grammar()
    for rule in grammar_list_of_lists:
        variable = rule[0]
        options = []
        for line in rule[1:]:
            probability, *symbols = line.split()
            symbols = parse_symbols(symbols, grammar)
            # Initialize Option object
            option = Option(int(probability), symbols)
            options.append(option)
        # Initialize Rule object
        rule = Rule(variable, options)
        grammar.add_rule(rule)
    return grammar


def parse_symbols(symbols, grammar) -> list:
    """This module is in charge of parsing symbols"""
    parsed_symbols = []
    for symbol in symbols:
        # Check if it is a Variable Symbol or Terminal Symbol
        if symbol.startswith('[') and symbol.endswith(']'):
            variable_name = symbol[1:-1]
            variable = VariableSymbol(variable_name, grammar)
            parsed_symbols.append(variable)
        else:
            terminal = TerminalSymbol(symbol)
            parsed_symbols.append(terminal)
    return parsed_symbols
