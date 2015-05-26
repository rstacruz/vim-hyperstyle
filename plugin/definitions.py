def apply_synonyms(table, synonyms):
    for key in synonyms:
        for other_key in synonyms[key]:
            if table.get(other_key):
                raise IndexError("Key already taken: %s" % other_key)
            table[other_key] = table[key]

"""
A list of CSS properties to expande.
"""
properties = {
    "bg": ("background", { "value": "color" }),
    "m": ("margin", { "value": "size", "unit": "em" }),
    "w": ("width", { "value": "size" }),
    "h": ("height", { "value": "size" }),
    "mh": ("min-height", { "value": "size" }),
    "mw": ("min-width", { "value": "size" }),
    "p": ("padding", { "value": "size", "nospace": True }),
    "pa": ("padding", { "value": "size" }),
    "bo": ("border", { "value": "border" }),
    "o":  ("outline", { "value": "border" }),
    "l": ("left", { "value": "size" }),
    "t": ("top", { "value": "size" }),
    "bot": ("bottom", { "value": "size" }),
    "r": ("right", { "value": "size" }),

    "d": ("display"),

    "fl": ("float", { "value": None }),

    "f": ("font", { "value": None }),
    "fs": ("font-size", { "value": "size", "unit": "em" }),
    "fst": ("font-style"),
    "fw": ("font-weight", { "value": None }),
    "lh": ("line-height", { "value": "size", "unit": "em" }),
    "ls": ("letter-spacing", { "value": "size" }),
    "tt": ("text-transform"),

    "br": ("border-right", { "value": "border" }),
    "bl": ("border-left", { "value": "border" }),
    "bt": ("border-top", { "value": "border" }),
    "bb": ("border-bottom", { "value": "border" }),

    "bw": ("border-width", { "value": "size" }),
    "brw": ("border-right-width", { "value": "size" }),
    "blw": ("border-left-width", { "value": "size" }),
    "btw": ("border-top-width", { "value": "size" }),
    "bbw": ("border-bottom-width", { "value": "size" }),

    "bra": ("border-radius", { "value": "size" }),
    "brad": ("border-radius", { "value": "size" }),

    "ct": ("content"),
    "con": ("content"),
    "cont": ("content"),

    "cur": ("cursor"),

    "ani": ("animation"),
    "anim": ("animation"),

    "bg": ("background"),
    "bgc": ("background-color"),
    "bgs": ("background-size"),
    "bgp": ("background-position"),

    "c": ("color"),

    "bs": ("box-shadow"),
    "bsize": ("box-sizing"),
}

# uhh.. maybe auto fuzzy these at some point.
apply_synonyms(properties, {
    "d": ["di", "dis", "disp"],
    "c": ["co", "col", "colo"],
    "l": ["le", "lef"],
    "t": ["to"],
    "r": ["ri", "rig"],
    "fl": ["flo", "floa"],
    "ls": ["let", "lett", "lette", "letter"],
    "mw": ["minw", "minwidth"],
    "mh": ["minh", "minheight"],
    "cur": ["curs", "curso"],
    "bgc": ["bgcolor"],
    "bgp": ["bgpos"],
    "bgs": ["bgsize"],
    "bsize": ["bsi", "bsz", "bsiz", "bsizing"],
})

"""
A list of CSS expressions to expand.
"""
expressions = {
    "db": ("display", "block"),
    "di": ("display", "inline"),
    "dib": ("display", "inline-block"),
    "dt": ("display", "table"),
    "dtc": ("display", "table-cell"),
    "dtr": ("display", "table-row"),
    "dn": ("display", "none"),

    "fl": ("float", "left"),
    "fr": ("float", "right"),
    "fn": ("float", "none"),

    "bold": ("font-weight", "bold"),

    "fsi": ("font-style", "italic"),
    "fsn": ("font-style", "normal"),

    "m0a": ("margin", "0 auto"),

    "fwb": ("font-weight", "bold"),

    "f1": ("font-weight", "100"),
    "f2": ("font-weight", "200"),
    "f3": ("font-weight", "300"),
    "f4": ("font-weight", "400"),
    "f5": ("font-weight", "500"),
    "f6": ("font-weight", "600"),
    "f7": ("font-weight", "700"),
    "f8": ("font-weight", "800"),
    "f9": ("font-weight", "900"),

    "bcc": ("border-collapse", "collapse"),
    
    "brx": ("background-repeat", "repeat-x"),
    "bry": ("background-repeat", "repeat-y"),
    "brn": ("background-repeat", "no-repeat"),

    "cover": ("background-size", "cover"),
    "contain": ("background-size", "contain"),

    "cup": ("cursor", "pointer"),
    "cuw": ("cursor", "wait"),
    "cub": ("cursor", "busy"),
    "cut": ("cursor", "text"),

    "cont": ("content", "''"),
    "con": ("content", "''"),
    "ct": ("content", "''"),

    "ttu": ("text-transform", "uppercase"),
    "ttn": ("text-transform", "none"),

    "under": ("text-decoration", "underline"),
    "tdu": ("text-decoration", "underline"),
    "tdn": ("text-decoration", "none"),

    "bsb": ("box-sizing", "border-box"),
    "bsp": ("box-sizing", "padding-box"),
    "bsc": ("box-sizing", "content-box"),
}

apply_synonyms(expressions, {
    "ttu": ["up"],
    "fsi": ["it", "ita", "ital", "italic"],
    "fwb": ["fb"],
    "f1": ["fw1"],
    "f2": ["fw2"],
    "f3": ["fw3"],
    "f4": ["fw4"],
    "f5": ["fw5"],
    "f6": ["fw6"],
    "f7": ["fw7"],
    "f8": ["fw8"],
    "f9": ["fw9"],
    "dt": ["table"],
    "dtc": ["table-cell", "tablecell", "cell"],
    "dtr": ["table-row", "tablerow", "row"],
})
