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
def apply_fuzzies(list, properties):
    def iterate(property):
        for key in fuzzify(property):
            if not key in properties:
                properties[key] = properties[short]

    # For each property, apply some of its fuzzy matches
    for (short, prop, options) in list:

        # Create them for the property
        # ("box-sizing" => "boxsizing", "boxsizi", "boxsi", "boxs", "box"...)
        iterate(prop.replace('-', ''))

        # Also add aliases ("bgcolor" => "bgcolo", "bgcol", "bgco", "bgc" ...)
        if options and "alias" in options:
            [iterate(alias) for alias in options["alias"]]

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
