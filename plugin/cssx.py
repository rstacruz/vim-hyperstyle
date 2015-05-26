import re
from definitions import properties, expressions

line_expr = re.compile(r'^(\s*)(.*?)$')

"""
Expands a snippet.
"""
def expand_expression(line):
    (indent, snippet) = split_line(line)

    for shortcut in expressions:
        if snippet == shortcut:
            expansion = expressions[shortcut]
            return "%s%s: %s;" % (indent, expansion[0], expansion[1])

    return indent + snippet

"""
Expands a snippet.
"""
def expand_property(line):
    (indent, snippet) = split_line(line)

    for shortcut in properties:
        if snippet == shortcut:
            expansion = properties[shortcut]
            return "%s%s:" % (indent, expansion["name"])

"""
(Private) splits a line into its indentation and meat.

> (indent, snippet) = split_line("  db")
"""
def split_line(line):
    match = line_expr.match(line)
    return (match.group(1), match.group(2))
