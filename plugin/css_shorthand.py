import re
from definitions import properties, statements, full_properties
from utils import fuzzify

line_expr = re.compile(r'^(\s*)(.*?)$')
value_expr = re.compile(r'^([^\.\d-]*)(-?\d*\.?\d+)(p|x|m|px|e|em|s|ms|%|)$')
rule_expr = re.compile(r'^((?:[a-z]+-)*[a-z]+): *([^\s].*);?$')

"""
Expands a statement line. Executed when pressing <Enter>. If `semi` is a blank
string, then treat the language as an indented syntax (like Sass).

>>> expand_statement("db")
"display: block;"

>>> expand_statement("db", '')
"display: block"

>>> expand_statement("m3m")
"margin: 3em;"
"""
def expand_statement(line, semi = ';'):
    indent, snippet = split_indent(line)

    # Check if its a simple statement
    # (db => display: block)
    def expand_simple_statement():
        expansion = statements.get(snippet)
        if not expansion: return

        key, value, _ = expansion
        return "%s%s: %s%s" % (indent, key, value, semi)

    # Check if its a property with value
    # (m10em => margin: 10em)
    def expand_property_with_value():
        short, value, unit = split_value(snippet) # ("m","10","em")
        expansion = properties.get(short) # ("margin", {"unit": "px"})
        if not expansion: return

        prop, options = expansion
        value = expand_full_value(value + unit, prop)
        if value: return "%s%s: %s%s" % (indent, prop, value, semi)

    # (margin: 3 => margin: 3px)
    def expand_unit_value():
        m = rule_expr.match(snippet) # ("margin", "3")
        if not m: return

        prop, value = m.group(1), m.group(2)
        new_value = expand_full_value(value, prop)
        return "%s%s: %s%s" % (indent, prop, new_value or value, semi)

    # add semicolon if needed
    def expand_semicolon():
        if semi == ';' and is_balanced_rule(snippet):
            return "%s%s;" % (indent, snippet)

    return \
        expand_simple_statement() or \
        expand_property_with_value() or \
        expand_unit_value() or \
        expand_semicolon()

"""
Splits a snippet into property, number and unit.

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

The 2nd argument is there to keep the API same with expand_statement(). Vim
might pass a semicolon for it.

>>> expand_property("m")
"margin:"
"""
def expand_property(line, semi=';'):
    indent, snippet = split_indent(line)

    tuple = properties.get(snippet)
    if tuple:
        prop, options = tuple
        return "%s%s:" % (indent, prop)

    # Not recommend,d but this will expand "dib_" into "display: inline-block;_"
    # expr = expand_statement(line, semi)
    # if expr: return expr

"""
Expands a value of a given property `prop`. Returns the expanded value.

>>> e("3", "margin")
"3px"

>>> e("3x", "margin")
"3px"

>>> e("a", "margin")
"auto"

>>> e("l", "float")
"left"
"""
def expand_full_value(val, prop):
    options = full_properties.get(prop)
    if not options: return

    # Account for default units
    # ('margin', '3') => '3px'
    default_unit = options.get('unit')
    if default_unit:
        _, number, unit = split_value(val)
        if number:
            return expand_numeric_value(number, unit, default_unit)

    # Account for preset value keywords
    # ('float', 'l') => 'left'
    values = options.get('values')
    if values:
        return expand_keyword_value(val, values)

"""
Finds the closest match to a `value` given a list of `keywords`.

>>> expand_keyword_value('l', ['left', 'right', 'auto'])
"left"

>>> expand_keyword_value('xxx', ['inherit', 'auto'])
None
"""
def expand_keyword_value(value, keywords):
    for word in keywords:
        if re.match('^'+value, word): return word 
    for word in keywords:
        if re.match(value, word): return word

"""
Expands a single numeric value.

>>> expand_numeric_value("10", "", "px")
"10px"

>>> expand_numeric_value("10", "m")
"10em"
"""
def expand_numeric_value(number, unit, default_unit):
    if number == "0":
        return number

    if unit == "p" or unit == "x":
        unit = "px"
    if unit == "m" or unit == "e":
        unit = "em"
    if unit == "":
        if default_unit == "_":
            unit = ""
        else:
            unit = (default_unit or px)

    return number + unit

"""
(Private) splits a line into its indentation and meat.

>>> (indent, snippet) = split_indent("  db")
("  ", "db")
"""
def split_indent(line):
    match = line_expr.match(line)
    return (match.group(1), match.group(2))

"""
Checks if a line is a balanced rule that can be auto-terminated with a
semicolon.

>>> is_balanced_rule("margin: 0")
True

>>> is_balanced_rule("margin: scaleX(3)")
True

>>> is_balanced_rule("margin: linear-gradient(to-bottom")
False
"""
def is_balanced_rule(str):
    if str and str[-1] == ';':
        return False

    m = rule_expr.match(str)
    if not m:
        return False

    value = m.group(2)
    return value.count('(') == value.count(')')
