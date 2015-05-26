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
    "bg": { "name": "background", "value": "color" },
    "m": { "name": "margin", "value": "size", "unit": "em" },
    "w": { "name": "width", "value": "size" },
    "h": { "name": "height", "value": "size" },
    "mh": { "name": "min-height", "value": "size" },
    "mw": { "name": "min-width", "value": "size" },
    "p": { "name": "padding", "value": "size", "nospace": True },
    "pa": { "name": "padding", "value": "size" },
    "bo": { "name": "border", "value": "border" },
    "o":  { "name": "outline", "value": "border" },
    "l": { "name": "left", "value": "size" },
    "t": { "name": "top", "value": "size" },
    "bot": { "name": "bottom", "value": "size" },
    "r": { "name": "right", "value": "size" },

    "d": { "name": "display" },

    "fl": { "name": "float", "value": None },

    "f": { "name": "font", "value": None },
    "fs": { "name": "font-size", "value": "size", "unit": "em" },
    "fst": { "name": "font-style" },
    "fw": { "name": "font-weight", "value": None },
    "lh": { "name": "line-height", "value": "size", "unit": "em" },
    "ls": { "name": "letter-spacing", "value": "size" },
    "tt": { "name": "text-transform" },

    "br": { "name": "border-right", "value": "border" },
    "bl": { "name": "border-left", "value": "border" },
    "bt": { "name": "border-top", "value": "border" },
    "bb": { "name": "border-bottom", "value": "border" },

    "bw": { "name": "border-width", "value": "size" },
    "brw": { "name": "border-right-width", "value": "size" },
    "blw": { "name": "border-left-width", "value": "size" },
    "btw": { "name": "border-top-width", "value": "size" },
    "bbw": { "name": "border-bottom-width", "value": "size" },

    "bra": { "name": "border-radius", "value": "size" },
    "brad": { "name": "border-radius", "value": "size" },

    "ct": { "name": "content" },
    "con": { "name": "content" },
    "cont": { "name": "content" },

    "cur": { "name": "cursor" },

    "ani": { "name": "animation" },
    "anim": { "name": "animation" },

    "bg": { "name": "background" },
    "bgc": { "name": "background-color" },
    "bgs": { "name": "background-size" },
    "bgp": { "name": "background-position" },

    "c": { "name": "color" },

    "bs": { "name": "box-shadow" },
    "bsize": { "name": "box-sizing" },
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
