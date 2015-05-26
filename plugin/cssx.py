import re
from definitions import properties, expressions

line_expr = re.compile(r'^(\s*)(.*?)$')
value_expr = re.compile(r'^([^\.\d-]+)(-?\d*\.?\d+)(p|x|m|px|em|%|)$')

"""
Expands a snippet expression.
"""
def expand_expression(line, semi = ';'):
    (indent, snippet) = split_indent(line)

    # Check if its an expression
    # (db => display: block)
    expansion = expressions.get(snippet)
    if expansion:
        return "%s%s: %s%s" % (indent, expansion[0], expansion[1], semi)

    # Check if its a property with value
    (prop, value, unit) = split_value(snippet)
    expansion = properties.get(prop)
    if prop and expansion and expansion[1] and expansion[1].get("value"):
        value = expand_value(value, unit, expansion[1].get("unit"))
        return "%s%s: %s%s" % (indent, expansion[0], value, semi)

    # Else, nada
    return indent + snippet

"""
Expands a value

>>> expand_value("10", "")
"10px"

>>> expand_value("10", "m")
"10em"
"""
def expand_value(value, unit, default_unit = None):
    if value == "0":
        return value

    if unit == "p" or unit == "x":
        unit = "px"
    if unit == "m":
        unit = "em"
    if unit == "":
        unit = (default_unit or "px")

    return value + unit

"""
Splits a snippet into property, value and unit

# margin: 10px
>>> split_value("m10p")
("m", "10", "p")
"""
def split_value(snippet):
    m = value_expr.match(snippet)
    if m:
        return (m.group(1), m.group(2), m.group(3))
    else:
        return (None, None, None)

"""
Expands a property.

>>> expand_property("m")
"margin:"
"""
def expand_property(line):
    (indent, snippet) = split_indent(line)

    expansion = properties.get(snippet)
    if isinstance(expansion, str):
        return "%s%s:" % (indent, expansion)
    if isinstance(expansion, tuple):
        return "%s%s:" % (indent, expansion[0])

"""
(Private) splits a line into its indentation and meat.

>>> (indent, snippet) = split_indent("  db")
("  ", "db")
"""
def split_indent(line):
    match = line_expr.match(line)
    return (match.group(1), match.group(2))
