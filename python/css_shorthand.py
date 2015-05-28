import re
from definitions import properties, statements, full_properties
from utils import fuzzify

# Also see http://www.w3.org/TR/css3-values/
semicolon_expr = re.compile(r';\s*$')
value_expr = re.compile(r'^([^\.\d-]*)(-?\d*\.?\d+)(x|p[tcx]?|e[mx]?|s|m[ms]?|rem|ch|v[wh]|vmin|max|%|)$')
line_expr = re.compile(r'^(\s*)(.*?)$')
rule_expr = re.compile(r'^((?:[a-z]+-)*[a-z]+): *([^\s].*?);?$')
selectorlike_expr = re.compile(r'.*(before|placeholder|root|after|focus|hover|active|checked|selected).*')
ends_in_brace_expr = re.compile(r'.*\{\s*$')

def expand_statement(line):
    """Expands a statement line. Executed when pressing <Enter>. If `semi` is a
    blank string, then treat the language as an indented syntax (like Sass).

    >>> expand_statement("db")
    "display: block;"

    >>> expand_statement("db", '')
    "display: block"

    >>> expand_statement("m3m")
    "margin: 3em;"
    """
    indent, snippet = split_indent(line)

    # Check if its a simple statement
    # (db => display: block)
    def expand_simple_statement():
        expansion = statements.get(snippet)
        if not expansion: return

        key, value, _ = expansion
        return "%s%s: %s" % (indent, key, value)

    # Check if its a property with value
    # (m10em => margin: 10em)
    def expand_property_with_value():
        short, value, unit = split_value(snippet) # ("m","10","em")
        expansion = properties.get(short) # ("margin", {"unit": "px"})
        if not expansion: return

        prop, options = expansion
        value = expand_full_value(value + unit, prop)
        if value: return "%s%s: %s" % (indent, prop, value)

    # (margin: 3 => margin: 3px)
    # skip it if it's say 'p:before' or anything selector-like.
    # this will also return the same thing for "complete" rules
    # (eg: "margin: auto"), thereby adding semicolons to them.
    def expand_unit_value():
        # skip non-rules (must match "x: y")
        m = rule_expr.match(snippet)
        if not m: return

        # skip "complete" rules ("...;")
        if semicolon_expr.match(snippet): return

        prop, value = m.group(1), m.group(2) # ("margin", "3")
        if is_selectorlike(value): return

        # skip imbalanced rules (eg, opening of `scaleX(`)
        if value.count('(') != value.count(')'): return

        new_value = expand_full_value(value, prop)
        return "%s%s: %s" % (indent, prop, new_value or value)

    return \
        expand_simple_statement() or \
        expand_property_with_value() or \
        expand_unit_value()

def split_value(snippet):
    """Splits a snippet into `property`, `number` and `unit`. Property and unit are optional.

    >>> # margin: 10px
    >>> split_value("m10p")
    ("m", "10", "p")

    >>> split_value("10p")
    ("", "10", "p")

    >>> split_value("10")
    ("", "10", "")
    """
    m = value_expr.match(snippet)
    if m:
        return (m.group(1), m.group(2), m.group(3))
    else:
        return (None, None, None)

def expand_property(line, semi=''):
    """Expands a property.

    The 2nd argument is not used, but is there to keep the API compatible with
    `expand_statement()`.

    >>> expand_property("m")
    "margin:"
    """
    indent, snippet = split_indent(line)

    tuple = properties.get(snippet)
    if tuple:
        prop, options = tuple
        return "%s%s:" % (indent, prop)

def expand_full_value(val, prop):
    """Expands a value of a given property `prop`. Returns the expanded value.

    >>> e("3", "margin")
    "3px"

    >>> e("3x", "margin")
    "3px"

    >>> e("a", "margin")
    "auto"

    >>> e("l", "float")
    "left"
    """
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

def expand_keyword_value(value, keywords):
    """Finds the closest match to a `value` given a list of `keywords`.

    >>> expand_keyword_value('l', ['left', 'right', 'auto'])
    "left"

    >>> expand_keyword_value('xxx', ['inherit', 'auto'])
    None
    """
    for word in keywords:
        if re.match('^'+value, word): return word 
    for word in keywords:
        if re.match(value, word): return word

def expand_numeric_value(number, unit, default_unit):
    """Expands a single `number` + `unit` value. If the unit is absent (blank
    string), the `default_unit` will be used instead.

    >>> expand_numeric_value("10", "", "px")
    "10px"

    >>> expand_numeric_value("10", "m")
    "10em"
    """
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

def split_indent(line):
    """(Private) splits a line into its indentation and meat.

    >>> (indent, snippet) = split_indent("  db")
    ("  ", "db")
    """
    match = line_expr.match(line)
    return (match.group(1), match.group(2))

def is_balanced_rule(str):
    """Checks if a line is a balanced rule that can be auto-terminated with a
    semicolon.

    >>> is_balanced_rule("margin: 0")
    True

    >>> is_balanced_rule("margin: scaleX(3)")
    True

    >>> is_balanced_rule("margin: linear-gradient(to-bottom")
    False
    """
    if str and str[-1] == ';':
        return False

    m = rule_expr.match(str)
    if not m:
        return False

    value = m.group(2)
    return value.count('(') == value.count(')')

def is_selectorlike(value):
    if selectorlike_expr.match(value) or ends_in_brace_expr.match(value):
        return True

