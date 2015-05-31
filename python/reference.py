# -*- coding: utf-8 -*-
# This code sucks, really, don't even look at it

import re
from definitions import definitions
from indexer import Indexer
import sys

# Indexing
index = Indexer()
index.index(definitions)

def print_reference():
    print_headline("Properties")
    print_table(get_property_reference())
    print_headline("Statements")
    print_table(get_statement_reference())

if "--vim" in sys.argv:
    def print_headline(headline):
        print headline + ":"
        print ""
    def print_table(items):
        for name, aliases in items:
            aliases = re.sub(r'^([a-z0-9]+)', r'`\1`', aliases)
            print "    %-35s %s" % ("*%s*"%name, aliases)
        print ""
else:
    def print_headline(headline):
        print "## " + headline
        print ""

    def print_table(items):
        print "| %-35s | %-60s |" % ("Expansion", "Shortcuts")
        print "| --- | --- |"
        for name, aliases in items:
            aliases = re.sub(r'^([a-z0-9]+)', r'**\1**', aliases)
            print " | %-35s | %-60s |" % ("`%s`"%name, aliases)
        print ""

def get_property_reference():
    return get_generic_reference(index.full_properties.items(), index.properties)

def get_statement_reference():
    return get_generic_reference(index.full_statements.items(), index.statements)

def get_generic_reference(items, index):
    ref = []
    items = sorted(items)
    for prop, options in items:
        aliases = options.get('aliases')
        aliases_ref = resolve_aliases(aliases, options, index)
        ref.append((prop, aliases_ref))
    return ref

def resolve_aliases(aliases, this, index):
    """
    >>> resolve_aliases(['talign', 'textalign'], options, index.properties)
    "ta[lign] tex[align]
    """
    def referencify(alias):
        root_length = 1
        for i in range(len(alias), 0, -1):
            newalias = alias[0:i]
            if index.get(newalias) == this:
                root_length = i

        if len(alias) == root_length:
            return alias
        else:
            return "%s[%s]" % (alias[0:root_length], alias[root_length:])

    refs = [referencify(a) for a in aliases]

    return " ".join(refs)

if __name__ == '__main__':
    print_reference()
