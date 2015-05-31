import sys
if sys.version_info < (3,):
    range = xrange

class Indexer:
    """Indexes CSS property and statement definitions.

    >>> idx = Indexer()
    >>> idx.index(definitions)

    >>> idx.properties.get("pad")
    {
      "property": "padding",
      "values": ["auto"],
      "unit": "px"
    })

    >>> idx.full_properties.get("padding")
    # same as above

    >>> idx.statements.get("m0a")
    {
      "property": "margin",
      "value": "auto"
    }
    """
    def __init__(self):
        self.properties = {} # indexed by shorthand ("bg")
        self.statements = {} # indexed by shorthand ("m0a")
        self.full_properties = {} # indexed by long property name ("margin")
        self.full_statements = {} # indexed by long property name ("margin: auto")

    def index(self, defs):
        """Adds definitions to the index.

        >>> idx.index({ "properties": [...], "definitions": [...] })
        """

        self.index_full_props(defs)
        self.index_aliases(defs)

    def index_full_props(self, defs):
        for (prop, aliases, unit, values) in defs["properties"]:
            options = {}
            options["property"] = prop
            options["aliases"] = aliases[:]
            options["unit"] = unit
            options["values"] = values
            update_aliases(options)
            self.full_properties[prop] = options

        for (prop, value, aliases) in defs["statements"]:
            options = {}
            options["property"] = prop
            options["value"] = value
            options["aliases"] = aliases
            key = "%s: %s" % (options["property"], options["value"])
            self.full_statements[key] = options

    def index_aliases(self, defs):
        for (prop, _, __, ___) in defs["properties"]:
            options = self.full_properties[prop]
            index_item(self.properties, options)

        for (prop, value, __) in defs["statements"]:
            key = "%s: %s" % (prop, value)
            options = self.full_statements[key]
            index_item(self.statements, options)

        self.remove_tags()

    def remove_tags(self):
        """Workaround to stop tags from being expanded. This will allow you to type
        `li:before` without `li:` being expanded to `line-height:`.
        
        This is also important for indented syntaxes, where you might commonly
        type `p` on its own line (in contrast to `p {`).
        """
        tags = ['a', 'p', 'br', 'b', 'i', 'li', 'ul', 'div', 'em', 'sup', \
                'big', 'small', 'sub']
        for tag in tags:
            self.statements[tag] = None
            self.properties[tag] = None

def fuzzify(str):
    """Returns a generator with fuzzy matches for a given string.

    >>> for s in fuzzify("border"):
    >>>     print s
    "b", "bo", "bor", "bord", "borde"
    """
    if str:
        for i in range(1, len(str)+1):
            yield str[0:i]

def update_aliases(options):
    """Updates options['aliases'] with property defaults
    """
    prop = options.get('property')

    # If the property has dashes, add non-dashed versions
    if '-' in prop:
        options["aliases"].append(prop.replace('-', ''))

    # Insert the property itself
    options["aliases"].append(prop)

def index_item(properties, options):
    """Takes aliases and puts them into the properties index"""
    for alias in options["aliases"]:
        for key in fuzzify(alias):
            if not key in properties:
                properties[key] = options
