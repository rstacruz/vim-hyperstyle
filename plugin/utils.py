"""
Yeah

"""
def apply_synonyms(table, synonyms):
    for key in synonyms:
        for other_key in synonyms[key]:
            if table.get(other_key):
                raise IndexError("Key already taken: %s" % other_key)
            table[other_key] = table[key]

"""
Mutates `properties` to apply fuzzy matches
"""
def apply_fuzzies(properties):
    # Simple iterator for properties
    def each_property():
        for prop in properties:
            expansion = properties[prop]
            if isinstance(expansion, tuple):
                yield (prop, expansion[0], expansion[1])
            else:
                yield (prop, expansion, {})

    # For each prooperty, apply some of its fuzzy matches
    new_properties = {}
    for (short, prop, options) in each_property():
        def iterate(property):
            for key in fuzzify(property):
                if not key in properties and not key in new_properties:
                    new_properties[key] = properties[short]

        # Create them for the property
        # ("box-sizing" => "boxsizing", "boxsizi", "boxsi", "boxs", "box"...)
        iterate(prop.replace('-', ''))

        # Also add aliases ("bgcolor" => "bgcolo", "bgcol", "bgco", "bgc" ...)
        if options and "alias" in options:
            [iterate(alias) for alias in options["alias"]]

    # Propagate the fuzzy matches back to properties
    # We do this separately because we can't edit a dict while it's being
    # iterated
    for key in new_properties:
        properties[key] = new_properties[key]

"""
Returns a generator with fuzzy matches for a given string.

>>> for s in fuzzify("border"):
>>>     print s
"b", "bo", "bor", "bord", "borde"
"""
def fuzzify(str):
    if str:
        for i in xrange(1, len(str)+1):
            yield str[0:i]

