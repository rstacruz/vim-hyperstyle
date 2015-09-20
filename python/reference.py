# -*- coding: utf-8 -*-
# This code sucks, really, don't even look at it

import re
from definitions import definitions
from indexer import Indexer
import sys

# Indexing
index = Indexer()
index.index(definitions)

tags = [
    'a', 'p', 'br', 'b', 'i', 'li', 'ul', 'div', 'em', 'sup', 'big', 'small',
    'sub'
]

def print_reference():
    if "--vim" in sys.argv:
        print(VimPrinter().to_s())
    else:
        print(MarkdownPrinter().to_s())

class VimPrinter:
    def to_s(self):
        self.lines = []
        self.top()
        self.headline("Properties")
        self.table(references["properties"])
        self.headline("Statements")
        self.table(references["statements"])
        self.foot()
        return "\n".join(self.lines)
    def l(self, line):
        self.lines.append(line)
    def top(self):
        self.l("*hyperstyle*  Style much faster")
        self.l("")
    def foot(self):
        self.l("vim:tw=78:ts=8:ft=help:norl:")
    def headline(self, headline):
        self.l("=" * 80)
        self.l("%-40s%40s" % (headline.upper(), '*hyperstyle-'+headline.lower()+'*'))
        self.l("")
    def table(self, items):
        def fmt(m):
            left = m.group(1)
            if len(left) <= 5: left = "`"+left+"`"
            if m.group(2): return "%s[%s]" % (left, m.group(2))
            else: return left
        for name, aliases in items:
            aliases = re.sub(r'([^ \[\]]+)(?:\[([^ ]+)\])?', fmt, aliases)
            self.l("  %-35s %s" % ("*%s*"%name.replace(' ','* *'), aliases))
        self.l("")

class MarkdownPrinter(VimPrinter):
    def top(self):
        pass
    def foot(self):
        pass
    def headline(self, headline):
        self.l("## " + headline)
        self.l("")
    def table(self, items):
        self.l("| %-35s | %-60s |" % ("Expansion", "Shortcuts"))
        self.l("| --- | --- |")
        def fmt(m):
            left = m.group(1)
            if len(left) <= 5: left = "<kbd>"+left+"</kbd>"
            else: left = "<u>"+left+"</u>"
            if m.group(2): return "%s%s" % (left, m.group(2))
            else: return left
        for name, aliases in items:
            aliases = re.sub(r'([^ \[\]]+)(?:\[([^ ]+)\])?', fmt, aliases)
            id = re.sub(r'[^a-zA-Z0-9]+', ' ', name).strip()
            id = re.sub(r' ', '-', id)
            anchor = "<a name='%s' href='#%s'>•</a>" % (id, id)
            self.l("| %s %-35s | %-60s |" % (anchor, "**%s**"%name, aliases))
        self.l("")

def get_property_reference():
    """
    Returns a reference table. This is a `list` with a tuple in each item.

    >>> get_property_reference()
    [ ('float:', 'fl[oat]'),
      ('margin-left', 'ml[eft]'), ... ]
    """

    return get_generic_reference(index.full_properties.items(), index.properties, ':')

def get_statement_reference():
    """
    Returns a reference table. This is a `list` with a tuple in each item.

    >>> get_statement_reference()
    [ ('margin-left: 0 auto', 'moa m0a'),
      ('float: left', 'fl[eft]'), ... ]
    """
    return get_generic_reference(index.full_statements.items(), index.statements)

def get_generic_reference(items, index, suf=''):
    ref = []
    items = sorted(items)
    for prop, options in items:
        aliases = options.get('aliases')
        aliases_ref = resolve_aliases(aliases, options, index)
        ref.append(("%s%s" % (prop, suf), aliases_ref))
    return ref

def resolve_aliases(aliases, this, index):
    """
    Given a bunch of `aliases`, shorten them in documentation format.

    Do this by looking for the "root" of each alias: that is, the shortest the
    alias can be typed. For instance, `texalign` has the root of `tex`, because
    `te` will evaluate to something else already.

    >>> resolve_aliases(['talign', 'textalign'], options, index.properties)
    "ta[lign] tex[align]"
    """
    taken = {}

    def referencify(alias):
        root_length = 1
        for i in range(len(alias), 0, -1):
            newalias = alias[0:i]
            if index.get(newalias) == this:
                root_length = i

        if len(alias) == root_length:
            return alias
        else:
            root = alias[0:root_length]
            if root in taken or root in tags:
                return alias
            else:
                taken[root] = True
                return "%s[%s]" % (root, alias[root_length:])

    refs = [referencify(a) for a in aliases]
    return " ".join(refs)

references = {
    "properties": get_property_reference(),
    "statements": get_statement_reference()
}

if __name__ == '__main__':
    print_reference()
