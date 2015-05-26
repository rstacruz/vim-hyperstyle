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
    ("lh", "line-height", { "unit": "_" }),
    ("ls", "letter-spacing", { "unit": "px" }),

    ("tf", "transform", { "alias": ["tform", "xform"] }),
    ("tn", "transition", { "alias": ["tsition"] }),
    ("tt", "text-transform", { "alias": ["ttransform"] }),
    ("td", "text-decoration", { "alias": ["tdecoration"] }),
    ("ti", "text-indent", { "unit": "px" }),

    ("tnd", "transition-duration", { "unit": "ms", "alias": ["tduration"] }),

    ("fl", "float", { "values": ["left", "right", "none", "inherit"] }),

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
    ("ws", "white-space", {}),

    ("fg", "flex-grow", { "unit": "_", "alias": ["fgrow"] }),
    ("fsh", "flex-shrink", { "unit": "_", "alias": ["fshrink"] }),
    ("fdr", "flex-direction", { "alias": ["fdirection"] }),
    ("fwr", "flex-wrap", { "alias": ["fwrap"] }),
    ("ai", "align-items", { "alias": ["aitems"] }),
    ("jc", "justify-content", { "alias": ["jcontent"] }),
    ("or", "order", {}),
]

properties = {}
for (short, prop, options) in properties_list:
    properties[short] = (prop, options)

"""
A list of CSS expressions to expand.
"""
expressions_list = [
    ("db", "display", "block", {}),
    ("di", "display", "inline", {}),
    ("dib", "display", "inline-block", {}),
    ("dif", "display", "inline-flex", {}),
    ("dt", "display", "table", { "alias": ["table"] }),
    ("dtc", "display", "table-cell", { "alias": ["cell", "table-cell", "tablecell"] }),
    ("dtr", "display", "table-row", { "alias": ["row", "table-row", "tablerow"] }),
    ("dn", "display", "none", {}),
    ("df", "display", "flex", { "alias": ["dflex", "flex"] }),

    ("fl", "float", "left", { "alias": ["fleft"] }),
    ("fr", "float", "right", { "alias": ["fright"] }),
    ("fn", "float", "none", { "alias": ["fnone"] }),

    ("fwb", "font-weight", "bold", { "alias": ["bold"] }),
    ("fsi", "font-style", "italic", { "alias": ["italic"] }),
    ("fsn", "font-style", "normal", {}),

    ("m0a", "margin", "0 auto", {}),

    ("f1", "font-weight", "100", { "alias": ["fw1"] }),
    ("f2", "font-weight", "200", { "alias": ["fw2"] }),
    ("f3", "font-weight", "300", { "alias": ["fw3"] }),
    ("f4", "font-weight", "400", { "alias": ["fw4"] }),
    ("f5", "font-weight", "500", { "alias": ["fw5"] }),
    ("f6", "font-weight", "600", { "alias": ["fw6"] }),
    ("f7", "font-weight", "700", { "alias": ["fw7"] }),
    ("f8", "font-weight", "800", { "alias": ["fw8"] }),
    ("f9", "font-weight", "900", { "alias": ["fw9"] }),

    ("b0", "border", "0", {}),
    ("bcc", "border-collapse", "collapse", {}),
    
    ("brx", "background-repeat", "repeat-x", { "alias": [ "repeatx", "bgrx", "rx" ] }),
    ("bry", "background-repeat", "repeat-y", { "alias": [ "repeaty", "bgry", "ry" ] }),
    ("brn", "background-repeat", "no-repeat", { "alias": ["norepeat"] }),

    ("cover", "background-size", "cover", {}),
    ("contain", "background-size", "contain", {}),

    ("cup", "cursor", "pointer", {}),
    ("cuw", "cursor", "wait", {}),
    ("cub", "cursor", "busy", {}),
    ("cut", "cursor", "text", {}),

    ("cont", "content", "''", {}),

    ("ttu", "text-transform", "uppercase", {}),
    ("ttn", "text-transform", "none", {}),

    ("tal", "text-align", "left", {}),
    ("tar", "text-align", "right", {}),
    ("tac", "text-align", "center", {}),
    ("taj", "text-align", "justify", {}),

    ("under", "text-decoration", "underline", {}),
    ("tdu", "text-decoration", "underline", { "alias": ["underline"] }),
    ("tdn", "text-decoration", "none", {}),

    ("bsb", "box-sizing", "border-box", {}),
    ("bsp", "box-sizing", "padding-box", {}),
    ("bsc", "box-sizing", "content-box", {}),

    ("ma", "margin", "auto", {}),
    ("mla", "margin-left", "auto", {}),
    ("mra", "margin-right", "auto", {}),

    ("por", "position", "relative", {}),
    ("pof", "position", "fixed", {}),
    ("pos", "position", "static", {}),
    ("poa", "position", "absolute", {}),

    ("nowrap", "white-space", "nowrap", {}),
    ("ellip", "text-overflow", "ellipsis", {}),

    ("fla", "flex", "auto", {}),

    ("ais", "align-items", "flex-start", {}),
    ("aie", "align-items", "flex-end", {}),
    ("aic", "align-items", "center", {}),
    ("aistr", "align-items", "stretch", { "alias": ["aistretch"] }),

    ("fwrap", "flex-wrap", "wrap", { "alias": ["flexwrap"] }),
    ("fnowrap", "flex-wrap", "nowrap", {}),

    ("fdr", "flex-direction", "row", {}),
    ("fdrr", "flex-direction", "row-reverse", {}),
    ("fdc", "flex-direction", "column", {}),
    ("fdcr", "flex-direction", "column-reverse", {}),

    ("ellip", "text-overflow", "ellipsis", { "alias": ["elip", "ellipsis"] }),

    ("jcc", "justify-content", "center", {}),
    ("jcstart", "justify-content", "flex-start", {}),
    ("jcend", "justify-content", "flex-end", {}),
]

expressions = {}
for (short, prop, value, options) in expressions_list:
    expressions[short] = (prop, value, options)

for (short, prop, options) in properties_list:
    apply_fuzzies(properties, short, prop, options)

for (short, prop, value, options) in expressions_list:
    apply_fuzzies(expressions, short, prop, options)
