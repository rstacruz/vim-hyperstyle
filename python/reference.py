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
    print_top()
    print_headline("Properties")
    print_table(get_property_reference())
    print_headline("Statements")
    print_table(get_statement_reference())
    print_foot()

if "--vim" in sys.argv:
    def print_top():
        print "*vim-hyperstyle*  Style much faster"
        print ""
    def print_foot():
        print "vim:tw=78:ts=8:ft=help:norl:"
    def print_headline(headline):
        print "=" * 80
        print "%-40s%40s" % (headline.upper(), '*hyperstyle-'+headline.lower()+'*')
        print ""
    def print_table(items):
        def fmt(m):
            if m.group(2): return "`%s`[%s]" % (m.group(1), m.group(2))
            else: return "`%s`" % m.group(1)
        for name, aliases in items:
            aliases = re.sub(r'([^ \[\]]+)(?:\[([^ ]+)\])?', fmt, aliases)
            print "  %-35s %s" % ("*%s*"%name.replace(' ','* *'), aliases)
        print ""

else:
    def print_top():
        pass
    def print_foot():
        pass
    def print_headline(headline):
        print "## " + headline
        print ""

    def print_table(items):
        print "| %-35s | %-60s |" % ("Expansion", "Shortcuts")
        print "| --- | --- |"
        def fmt(m):
            if m.group(2): return "__%s__[%s]" % (m.group(1), m.group(2))
            else: return "__%s__" % m.group(1)
        for name, aliases in items:
            aliases = re.sub(r'([^ \[\]]+)(?:\[([^ ]+)\])?', fmt, aliases)
            print "| %-35s | %-60s |" % ("`%s`"%name, aliases)
        print ""

def get_property_reference():
    return get_generic_reference(index.full_properties.items(), index.properties, ':')

def get_statement_reference():
    return get_generic_reference(index.full_statements.items(), index.statements)

def get_generic_reference(items, index, suf=''):
    ref = []
    items = sorted(items)
    for prop, options in items:
        aliases = options.get('aliases')
        aliases_ref = resolve_aliases(aliases, options, index)
        ref.append((prop + suf, aliases_ref))
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
