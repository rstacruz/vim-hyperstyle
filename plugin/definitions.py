from utils import fuzzify, apply_synonyms, apply_fuzzies

"""
A list of CSS properties to expand.

This will be indexed as `properties` (a dict). We define it as a list first
because the order will matter in fuzzifying.
"""

properties_list = [
    ("bg", "background", {}),
    ("m", "margin", { "unit": "px" }),
    ("w", "width", { "unit": "px" }),
    ("h", "height", { "unit": "px" }),
    ("mh", "min-height", { "unit": "px" }),
    ("mw", "min-width", { "unit": "px" }),
    ("p", "padding", { "unit": "px", "nospace": True }),
    ("pa", "padding", { "unit": "px" }),
    ("b", "border", {}),
    ("o", "outline", {}),
    ("l", "left", { "unit": "px" }),
    ("t", "top", { "unit": "px" }),
    ("bot", "bottom", { "unit": "px" }),
    ("r", "right", { "unit": "px" }),

    ("ml", "margin-left", { "unit": "px" }),
    ("mr", "margin-right", { "unit": "px" }),
    ("mt", "margin-top", { "unit": "px" }),
    ("mb", "margin-bottom", { "unit": "px" }),

    ("pl", "padding-left", { "unit": "px" }),
    ("pr", "padding-right", { "unit": "px" }),
    ("pt", "padding-top", { "unit": "px" }),
    ("pb", "padding-bottom", { "unit": "px" }),

    ("d", "display", {}),
    ("ta", "text-align", {}),

    ("f", "font", {}),
    ("fs", "font-size", { "unit": "em" }),
    ("fst", "font-style", {}),
    ("fw", "font-weight", { "value": None }),
    ("lh", "line-height", { "unit": "em" }),
    ("ls", "letter-spacing", { "unit": "px" }),

    ("tt", "text-transform", {}),
    ("td", "text-decoration", {}),
    ("ti", "text-indent", { "unit": "px" }),

    ("fl", "float", {}),

    ("br", "border-right", { "value": "border" }),
    ("bl", "border-left", { "value": "border" }),
    ("bt", "border-top", { "value": "border" }),
    ("bb", "border-bottom", { "value": "border" }),

    ("bw", "border-width", { "unit": "px" }),
    ("brw", "border-right-width", { "unit": "px" }),
    ("blw", "border-left-width", { "unit": "px" }),
    ("btw", "border-top-width", { "unit": "px" }),
    ("bbw", "border-bottom-width", { "unit": "px" }),

    ("brad", "border-radius", { "unit": "px" }),

    ("con", "content", {}),
    ("cur", "cursor", {}),
    ("ani", "animation", {}),

    ("bg", "background", {}),
    ("bgc", "background-color", { "alias": ["bgcolor"] }),
    ("bgs", "background-size", { "alias": ["bgsize"] }),
    ("bgp", "background-position", { "alias": ["bgposition"] }),

    ("c", "color", {}),
    ("op", "opacity", {}),

    ("bs", "box-shadow", {}),
    ("bsize", "box-sizing", {}),

    ("pos", "position", {}),
    ("flex", "flex", {}),
]

properties = {}
for (short, prop, options) in properties_list:
    properties[short] = (prop, options)

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
    "df": ("display", "flex"),

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

    "b0": ("border", "0"),
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

    "ttu": ("text-transform", "uppercase"),
    "ttn": ("text-transform", "none"),

    "tal": ("text-align", "left"),
    "tar": ("text-align", "right"),
    "tac": ("text-align", "center"),
    "taj": ("text-align", "justify"),

    "under": ("text-decoration", "underline"),
    "tdu": ("text-decoration", "underline"),
    "tdn": ("text-decoration", "none"),

    "bsb": ("box-sizing", "border-box"),
    "bsp": ("box-sizing", "padding-box"),
    "bsc": ("box-sizing", "content-box"),

    "ma": ("margin", "auto"),
    "mla": ("margin-left", "auto"),
    "mra": ("margin-right", "auto"),

    "por": ("position", "relative"),
    "pof": ("position", "fixed"),
    "pos": ("position", "static"),
    "poa": ("position", "absolute"),
}

expression_synonyms = {
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
    "df": ["flex"],
    "dtc": ["table-cell", "tablecell", "cell"],
    "dtr": ["table-row", "tablerow", "row"],
    "cont": ["con", "cn"]
}

apply_fuzzies(properties_list, properties)
apply_synonyms(expressions, expression_synonyms)
