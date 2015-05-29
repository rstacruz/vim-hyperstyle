import sys
if sys.version_info < (3,):
    range = xrange

class Indexer:
    """Indexes definitions

    idx = Indexer()
    idx.index(definitions)
    """
    def __init__(self):
        self.properties = {} # indexed by shorthand ("bg")
        self.statements = {} # indexed by shorthand ("m0a")
        self.full_properties = {} # indexed by long property name ("margin")

    def index(self, defs):
        # Index them
        for (short, prop, options) in defs["properties"]:
            self.properties[short] = (prop, options)
            self.full_properties[prop] = options

        for (short, prop, value, options) in defs["statements"]:
            self.statements[short] = (prop, value, options)

        for (short, prop, options) in defs["properties"]:
            apply_fuzzies(self.properties, short, prop, options)

        for (short, prop, value, options) in defs["statements"]:
            apply_fuzzies(self.statements, short, prop, options)

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

def apply_fuzzies(properties, short, prop, options):
    """Mutates `properties` to apply fuzzy matches
    """
    def iterate(property):
        for key in fuzzify(property):
            if not key in properties:
                properties[key] = properties[short]

    # Create them for the property
    # ("box-sizing" => "boxsizing", "boxsizi", "boxsi", "boxs", "box"...)
    iterate(prop.replace('-', ''))
    iterate(prop)

    # Also add aliases ("bgcolor" => "bgcolo", "bgcol", "bgco", "bgc" ...)
    # This kinda sucks, because aliases should have lowest priority.
    if options and "alias" in options:
        [iterate(alias) for alias in options["alias"]]

def fuzzify(str):
    """Returns a generator with fuzzy matches for a given string.

    >>> for s in fuzzify("border"):
    >>>     print s
    "b", "bo", "bor", "bord", "borde"
    """
    if str:
        for i in range(1, len(str)+1):
            yield str[0:i]
