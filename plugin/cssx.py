import re
from definitions import properties, expressions

line_expr = re.compile(r'^(\s*)(.*?)$')
value_expr = re.compile(r'^([^\.\d-]+)(-?\d*\.?\d+(?:p|x|m|px|em|%)?)$')

"""
Expands a snippet.
"""
def expand_expression(line):
    (indent, snippet) = split_line(line)

    # Check if its an expression
    # (db => display: block)
    if expressions.get(snippet):
        expansion = expressions[snippet]
        return "%s%s: %s;" % (indent, expansion[0], expansion[1])

    # Check if its a property with value
    (prop, value) = split_value(snippet)
    if prop and properties.get(prop):
        expansion = properties[prop]

        if expansion["value"] != None:
            return "%s%s: %s;" % (indent, expansion["name"], value)

    return indent + snippet

def split_value(snippet):
    m = value_expr.match(snippet)
    if m:
        return (m.group(1), m.group(2))
    else:
        return (None, None)

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
