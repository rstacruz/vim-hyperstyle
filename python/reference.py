# -*- coding: utf-8 -*-
# This code sucks
# Really
# Don't even look at it

import re
from definitions import definitions
from indexer import Indexer

# Indexing
index = Indexer()
index.index(definitions)

def print_reference():
    print_properties()
    print_statements()

def print_properties():
    props = {}
    for name in index.properties:
        val = index.properties[name]
        if val == None: continue
        (prop, options) = val
        if not props.get(prop):
            props[prop] = { "aliases": [], "canonical": options["canonical"] }
        if options["canonical"] != name:
            props[prop]["aliases"].append(name)

    print_heading("Properties")
    print "These will expand when you press <kbd>:</kbd>, <kbd>Spacebar</kbd> or <kbd>Tab ⇥</kbd>.\n"
    print_table(props, "Property")

def print_statements():
    props = {}
    for name in index.statements:
        val = index.statements[name]
        if val == None: continue
        (prop, value, options) = val
        key = "%s: %s" % (prop, value)
        if not props.get(key):
            props[key] = { "aliases": [], "canonical": options["canonical"] }
        if options["canonical"] != name:
            props[key]["aliases"].append(name)

    print_heading("Statements")
    print "These will expand when you press <kbd>;</kbd>, <kbd>Enter ⏎</kbd> or <kbd>Tab ⇥</kbd>.\n"
    print_table(props, "Statement")

def print_heading(name):
    print "## %s" % name
    print ""

def print_table(table, name):
    print "| %s | Shortcuts |" % name
    print "| --- | --- |"
    for key in sorted(table.keys()):
        options = table[key]
        aliases = sorted(options["aliases"])
        canon = options["canonical"]
        aliases.insert(0, '**%s**' % canon)
        print "| `%s` | %s |" % (key, ', '.join(aliases))

if __name__ == '__main__':
    print_reference()
