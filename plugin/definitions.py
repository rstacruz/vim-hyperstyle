from utils import fuzzify, apply_synonyms, apply_fuzzies

"""
A list of CSS properties to expand.

This will be indexed as `properties` (a dict). We define it as a list first
because the order will matter in fuzzifying.
"""

properties_list = [
    ("m", "margin", { "unit": "px" }),
    ("w", "width", { "unit": "px" }),
    ("h", "height", { "unit": "px" }),
    ("p", "padding", { "unit": "px" }),
    ("b", "border", {}),
    ("o", "outline", {}),
    ("l", "left", { "unit": "px" }),
    ("t", "top", { "unit": "px" }),
    ("bot", "bottom", { "unit": "px" }),
    ("r", "right", { "unit": "px" }),
    ("bg", "background", {}),
    ("mh", "min-height", { "unit": "px" }),
    ("mw", "min-width", { "unit": "px" }),

    ("ml", "margin-left", { "unit": "px" }),
    ("mr", "margin-right", { "unit": "px" }),
    ("mt", "margin-top", { "unit": "px" }),
    ("mb", "margin-bottom", { "unit": "px" }),

    ("pl", "padding-left", { "unit": "px" }),
    ("pr", "padding-right", { "unit": "px" }),
    ("pt", "padding-top", { "unit": "px" }),
    ("pb", "padding-bottom", { "unit": "px" }),

    ("zi", "z-index", { "unit": "_" }),
    ("dir", "direction", { "values": ["ltr", "rtl", "inherit"] }),

    ("d", "display", {}),
    ("ta", "text-align", { "values": ["left", "right", "justify", "center", "inherit"] }),

    ("of", "overflow", { "values": ["scroll", "hidden", "auto", "inherit"] }),
    ("ofx", "overflow-x", { "alias": "ox", "values": ["scroll", "hidden", "auto", "inherit"] }),
    ("ofy", "overflow-y", { "alias": "oy", "values": ["scroll", "hidden", "auto", "inherit"] }),

    ("f", "font", {}),
    ("fs", "font-size", { "unit": "em" }),
    ("fst", "font-style", {}),
    ("fw", "font-weight", {}),
    ("fv", "font-variant", {}),
    ("ff", "font-family", {}),
    ("lh", "line-height", { "unit": "_" }),
    ("ls", "letter-spacing", { "unit": "px" }),

    ("tf", "transform", { "alias": ["tform", "xform"] }),
    ("tn", "transition", { "alias": ["tsition"] }),
    ("tt", "text-transform", { "alias": ["ttransform"] }),
    ("td", "text-decoration", { "alias": ["tdecoration"] }),
    ("ti", "text-indent", { "unit": "px" }),
    ("ti", "text-indent", { "unit": "px" }),
    ("ts", "text-shadow", {}),
    ("va", "vertical-align", { "unit": "px" }),

    ("tnd", "transition-duration", { "unit": "ms", "alias": ["tduration"] }),

    ("fl", "float", { "values": ["left", "right", "none", "inherit"] }),

    ("br", "border-right", {}),
    ("bl", "border-left", {}),
    ("bt", "border-top", {}),
    ("bb", "border-bottom", {}),

    ("bw", "border-width", { "unit": "px" }),
    ("brw", "border-right-width", { "unit": "px" }),
    ("blw", "border-left-width", { "unit": "px" }),
    ("btw", "border-top-width", { "unit": "px" }),
    ("bbw", "border-bottom-width", { "unit": "px" }),

    ("brad", "border-radius", { "unit": "px" }),
    ("boc", "border-color", { "unit": "px", "alias": ["bcolor"] }),

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
    ("va", "vertical-align", { "alias": ["valign"] }),

    ("fg", "flex-grow", { "unit": "_", "alias": ["fgrow"] }),
    ("fsh", "flex-shrink", { "unit": "_", "alias": ["fshrink"] }),
    ("fdr", "flex-direction", { "alias": ["fdirection"] }),
    ("fwr", "flex-wrap", { "alias": ["fwrap"] }),
    ("ai", "align-items", { "alias": ["aitems"] }),
    ("jc", "justify-content", { "alias": ["jcontent"] }),
    ("or", "order", {}),

    ("pba", "page-break-after", {}),
    ("pbb", "page-break-before", {}),
    ("per", "perspective", {}),
    ("porig", "perspective-origin", {}),
    ("wb", "word-break", { "values": ["normal", "break-all", "keep-all", "inherit"] }),
    ("q", "quotes", {}),
]

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

    ("b0", "border", "0", {}),
    ("p0", "padding", "0", {}),
    ("m0", "margin", "0", {}),
    ("m0a", "margin", "0 auto", {}),

    ("oh", "overflow", "hidden", {}),
    ("os", "overflow", "scroll", {}),
    ("oa", "overflow", "auto", {}),
    ("ov", "overflow", "visible", {}),

    ("oxh", "overflow-x", "hidden", {}),
    ("oxs", "overflow-x", "scroll", {}),
    ("oxa", "overflow-x", "auto", {}),
    ("oxv", "overflow-x", "visible", {}),

    ("oyh", "overflow-y", "hidden", {}),
    ("oys", "overflow-y", "scroll", {}),
    ("oya", "overflow-y", "auto", {}),
    ("oyv", "overflow-y", "visible", {}),

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

    ("vam", "vertical-align", "middle", {}),
    ("vat", "vertical-align", "top", {}),
    ("vab", "vertical-align", "bottom", {}),
    ("vasub", "vertical-align", "sub", {}),
    ("vasuper", "vertical-align", "super", {}),
    ("vabl", "vertical-align", "baseline", { "alias": [ "vabase", "baseline" ] }),
    ("vatt", "vertical-align", "text-top", {}),
    ("vatb", "vertical-align", "text-bottom", {}),

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

    ("por", "position", "relative", { "alias": ["relative"] }),
    ("pof", "position", "fixed", {}),
    ("pos", "position", "static", {}),
    ("poa", "position", "absolute", { "alias": ["absolute"] }),

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

    ("ltr", "direction", "ltr", {}),
    ("rtl", "direction", "rtl", {}),
]

# Index them
properties = {} # indexed by shorthand
full_properties = {} # indexed by long property name
for (short, prop, options) in properties_list:
    properties[short] = (prop, options)
    full_properties[prop] = options

expressions = {}
for (short, prop, value, options) in expressions_list:
    expressions[short] = (prop, value, options)

for (short, prop, options) in properties_list:
    apply_fuzzies(properties, short, prop, options)

for (short, prop, value, options) in expressions_list:
    apply_fuzzies(expressions, short, prop, options)

# Workaround to stop tags from being expanded. This will allow you to type
# `li:before` without `li:` being expanded to `line-height:`.
#
# This is also important for indented syntaxes, where you might commonly
# type `p` on its own line (in contrast to `p {`).
for tag in ['a', 'p', 'br', 'b', 'i', 'li', 'ul', 'div', 'em', 'sup', 'big', 'small', 'sub']:
    expressions[tag] = None
    properties[tag] = None
