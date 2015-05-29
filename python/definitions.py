"""
A list of CSS properties to expand.

This will be indexed as `properties` (a dict). We define it as a list first
because the order will matter in fuzzifying.

Each entry is in this format:

    (short, property, { options })

Where:

- short : the canonical shortcut for this property. This will always expand to
  the property.
- property : the full CSS property name.
- options : defines some optional behavior for this shortcut.

These options are available:

- unit : (String) when defined, assumes that the property has a value with a
  unit. When the value is numberless (eg, `margin:12`), the given unit will
  be assumed (`12px`). Set this to `_` for unitless numbers (eg, line-height).
- alias : (String list) a list of aliases for this shortcut.
- values : (String list) possible values for this property.

Each property will be accessible through these ways:

- the primary `short` (eg: m)
- fuzzy matches of the property name, no dashes(eg: mi, min, minh, minhe,
  minhei...)
- fuzzy matches with dashes (eg: min-h, min-hei, min-heig...)
- fuzzy matches of aliases defined (eg: td, tde, tdec, tdeco, tdecor, tdecora...)
"""

properties_list = [
    ("m", "margin", { "unit": "px", "values": ["auto"] }),
    ("w", "width", { "unit": "px", "values": ["auto"] }),
    ("h", "height", { "unit": "px", "values": ["auto"] }),
    ("p", "padding", { "unit": "px" }),
    ("bo", "border", {}), # because `b` is for bold.
    ("o", "outline", {}),
    ("l", "left", { "unit": "px" }),
    ("t", "top", { "unit": "px" }),
    ("bot", "bottom", { "unit": "px" }), # because `b` and `bo` are taken.
    ("r", "right", { "unit": "px" }),
    ("bg", "background", { "values": ["transparent"] }),
    ("mh", "min-height", { "unit": "px", "values": ["auto"] }),
    ("mw", "min-width", { "unit": "px", "values": ["auto"] }),
    ("xh", "max-height", { "unit": "px", "values": ["auto"], "alias": ["xheight", "mxheight"] }),
    ("xw", "max-width", { "unit": "px", "values": ["auto"], "alias": ["xwidth", "mxwidth"] }),

    ("ml", "margin-left", { "unit": "px", "values": ["auto"], "alias": ["mleft", "marleft"] }),
    ("mr", "margin-right", { "unit": "px", "values": ["auto"], "alias": ["mright", "marright"] }),
    ("mt", "margin-top", { "unit": "px", "values": ["auto"], "alias": ["mtop", "martop"] }),
    ("mb", "margin-bottom", { "unit": "px", "values": ["auto"], "alias": ["mbottom", "marbottom"] }),

    ("pl", "padding-left", { "unit": "px", "alias": ["padleft", "pleft"] }),
    ("pr", "padding-right", { "unit": "px", "alias": ["padright", "pright"] }),
    ("pt", "padding-top", { "unit": "px", "alias": ["padtop", "ptop"] }),
    ("pb", "padding-bottom", { "unit": "px", "alias": ["padbottom", "pbottom"] }),

    ("zi", "z-index", { "unit": "_" }),

    ("d", "display", { "values": ["none", "block", "inline", "inline-block", "table", "table-cell", "table-row"] }),
    ("ta", "text-align", { "values": ["left", "right", "justify", "center", "inherit"] }),

    ("of", "overflow", { "values": ["visible", "scroll", "hidden", "auto", "inherit"] }),
    ("ofx", "overflow-x", { "alias": "ox", "values": ["visible", "scroll", "hidden", "auto", "inherit"] }),
    ("ofy", "overflow-y", { "alias": "oy", "values": ["visible", "scroll", "hidden", "auto", "inherit"] }),

    ("f", "font", {}),
    ("fs", "font-size", { "alias": ["fosize", "fsize"], "unit": "em" }),
    ("fst", "font-style", { "alias": ["fostyle", "fstyle"], "values": ["italic", "normal", "inherit"] }),
    ("fw", "font-weight", { "alias": ["foweight", "fweight"], "values": ["100","200","300","400","500","600","700","800","900","bold","normal"] }),
    ("fv", "font-variant", { "alias": ["fovariant", "fvariant"] }),
    ("ff", "font-family", { "alias": ["fofamily", "ffamily"] }),
    ("lh", "line-height", { "unit": "_" }),
    ("ls", "letter-spacing", { "alias": ["lespacing", "lspacing"], "unit": "px" }),

    ("tn", "transition", { "alias": ["tsition"] }),
    ("tf", "transform", { "alias": ["tform", "xform"] }),
    ("tt", "text-transform", { "alias": ["ttransform"], "values": ["uppercase", "none", "capitalize", "lowercase", "full-width", "inherit"] }),
    ("td", "text-decoration", { "alias": ["tdecoration"], "values": ["underline", "none", "line-through", "overline"] }),
    ("tdl", "text-decoration-line", { "values": ["underline", "none", "line-through", "overline", "inherit", "initial"] }),
    ("ti", "text-indent", { "alias": ["tindent", "texindent", "indent"], "unit": "px" }),
    ("ts", "text-shadow", { "values": ["none"], "alias": ["teshadow", "tshadow"] }),
    ("tl", "table-layout", { "alias": ["talayout", "tlayout"], "values": ["fixed", "auto", "inherit"] }),
    ("va", "vertical-align", { "unit": "px", "alias": ["valign"], "values": ["middle","top","bottom","baseline","text-top","text-bottom","sub","super"] }),

    ("tnd", "transition-duration", { "unit": "ms", "alias": ["tduration"] }),

    ("fl", "float", { "values": ["left", "right", "none", "inherit"] }),

    ("bri", "border-right", { "alias": ["bright", "borright"] }),
    ("bl", "border-left", { "alias": ["bleft", "borleft"] }),
    ("bt", "border-top", { "alias": ["btop", "bortop"] }),
    ("bb", "border-bottom", { "alias": ["bbottom", "borbottom"] }),

    ("bw", "border-width", { "unit": "px" }),
    ("brw", "border-right-width", { "unit": "px" }),
    ("blw", "border-left-width", { "unit": "px" }),
    ("btw", "border-top-width", { "unit": "px" }),
    ("bbw", "border-bottom-width", { "unit": "px" }),

    ("brad", "border-radius", { "unit": "px", "alias": ["borradius", "bradius"] }),
    ("boc", "border-color", { "unit": "px", "alias": ["borcolor", "bcolor"] }),
    ("bocoll", "border-collapse", { "alias": ["borcollapse", "bcollapse"], "values": ["collapse","separate","inherit"] }),

    ("c", "color", {}),
    ("op", "opacity", { "unit": "_" }),

    ("cur", "cursor", { "values": ["wait", "pointer", "auto", "default", "help", "progress", "cell", "crosshair", "text", "vertical-text", "alias", "copy", "move", "not-allowed", "no-drop", "all-scroll", "col-resize", "row-resize", "n-resize", "e-resize", "s-resize", "w-resize", "nw-resize", "ne-resize", "sw-resize", "se-resize", "ew-resize", "ns-resize", "zoom-in", "zoom-out", "grab", "grabbing" ] }),
    ("ani", "animation", {}),

    ("bg", "background", {}),
    ("bgc", "background-color", { "alias": ["backcolor", "bgcolor"] }),
    ("bgs", "background-size", { "alias": ["backsize", "bgsize"] }),
    ("bgp", "background-position", { "alias": ["backposition", "bgposition"] }),

    ("bsize", "box-sizing", { "values": ["border-box", "content-box", "padding-box"], "alias": ["bsizing", "bsize","boxsize"] }),
    ("bs", "box-shadow", { "values": ["none"], "alias": ["boshadow", "bshadow"] }),

    ("pos", "position", { "values": ["absolute", "relative", "fixed", "static", "inherit"] }),
    ("flex", "flex", {}),
    ("ws", "white-space", { "values": ["nowrap", "normal", "pre", "pre-wrap", "pre-line", "inherit"], "alias": ["whispace", "whspace", "wispace", "wspace"] }),

    ("vis", "visibility", { "values": ["visible", "hidden", "collapse", "inherit"] }),

    ("fg", "flex-grow", { "unit": "_", "alias": ["flegrow", "flgrow", "fgrow"] }),
    ("fsh", "flex-shrink", { "unit": "_", "alias": ["fleshrink", "flshrink", "fshrink"] }),
    ("fdr", "flex-direction", { "alias": ["fledirection", "fldirection", "fdirection"] }),
    ("fwr", "flex-wrap", { "alias": ["flewrap", "flwrap", "fwrap"] }),
    ("ai", "align-items", { "alias": ["alitems", "aitems"] }),
    ("jc", "justify-content", { "alias": ["justcontent", "juscontent", "jucontent", "jcontent"], "values": ["center", "flex-start", "flex-end"] }),
    ("or", "order", {}),

    ("pba", "page-break-after", {}),
    ("pbb", "page-break-before", {}),
    ("per", "perspective", {}),
    ("porig", "perspective-origin", {}),
    ("wb", "word-break", { "alias": ["worbreak", "wobreak", "wbreak"], "values": ["normal", "break-all", "keep-all", "inherit"] }),
    ("q", "quotes", {}),
    ("con", "content", {}),
    ("cl", "clear", { "values": ["left", "right", "both", "inherit"]}),
    ("zo", "zoom", { "unit": "_" }),
    ("dir", "direction", { "values": ["ltr", "rtl", "inherit"] }),
]

"""
A list of CSS statements to expand.

This differs from `property_list` as this defines shortcuts for an entire statement.
For instance, `dib<Enter>` will expand to `display: inline-block`.

Each line is in this format:

    (short, property, value, options)

The following options are available:

- alias : (String list) see `property_list` on how aliases work.
"""

statements_list = [
    ("db", "display", "block", {}),
    ("di", "display", "inline", {}),
    ("dib", "display", "inline-block", {}),
    ("dif", "display", "inline-flex", {}),
    ("dt", "display", "table", { "alias": ["table"] }),
    ("dtc", "display", "table-cell", { "alias": ["cell", "table-cell", "tablecell"] }),
    ("dtr", "display", "table-row", { "alias": ["row", "table-row", "tablerow"] }),
    ("dn", "display", "none", {}),
    ("df", "display", "flex", { "alias": ["dflex", "flex"] }),

    ("fl", "float", "left", { "alias": ["fleft", "flleft", "floleft"] }),
    ("fr", "float", "right", { "alias": ["fright", "flright", "floright"] }),
    ("fn", "float", "none", { "alias": ["fnone", "flnone", "flonone"] }),

    ("fwn", "font-weight", "normal", {}),
    ("fwb", "font-weight", "bold", { "alias": ["bold"] }),
    ("fsi", "font-style", "italic", { "alias": ["italic"] }),
    ("fsn", "font-style", "normal", {}),

    ("b0", "border", "0", {}),
    ("p0", "padding", "0", { "alias": ["po"] }),
    ("m0", "margin", "0", { "alias": ["mo"] }),
    ("m0a", "margin", "0 auto", { "alias": ["moa"] }),

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

    ("f1", "font-weight", "100", { "alias": ["f100", "fw100"] }),
    ("f2", "font-weight", "200", { "alias": ["f200", "fw200"] }),
    ("f3", "font-weight", "300", { "alias": ["f300", "fw300"] }),
    ("f4", "font-weight", "400", { "alias": ["f400", "fw400"] }),
    ("f5", "font-weight", "500", { "alias": ["f500", "fw500"] }),
    ("f6", "font-weight", "600", { "alias": ["f600", "fw600"] }),
    ("f7", "font-weight", "700", { "alias": ["f700", "fw700"] }),
    ("f8", "font-weight", "800", { "alias": ["f800", "fw800"] }),
    ("f9", "font-weight", "900", { "alias": ["f900", "fw900"] }),

    ("b0", "border", "0", {}),
    ("bcc", "border-collapse", "collapse", {}),
    ("bcs", "border-collapse", "separate", {}),
    
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

    ("vv", "visibility", "visible", { "alias": ["visible"] }),
    ("vh", "visibility", "hidden", { "alias": ["vishidden", "vihidden", "hidden", "hide"] }),
    ("vc", "visibility", "collapse", { "alias": ["viscollapse", "vicollapse", "vcillapse", "hide"] }),

    ("cb", "clear", "both", {}),
    ("cr", "clear", "right", {}),
    ("cl", "clear", "left", {}),

    ("cont", "content", "''", {}),

    ("ttu", "text-transform", "uppercase", {}),
    ("ttl", "text-transform", "lowercase", {}),
    ("ttn", "text-transform", "none", {}),
    ("ttc", "text-transform", "capitalize", {}),
    ("ttf", "text-transform", "full-width", {}),

    ("tal", "text-align", "left", {}),
    ("tar", "text-align", "right", {}),
    ("tac", "text-align", "center", {}),
    ("taj", "text-align", "justify", {}),

    ("tdu", "text-decoration", "underline", { "alias": ["underline"] }),
    ("tdn", "text-decoration", "none", {}),

    ("bsb", "box-sizing", "border-box", {}),
    ("bsp", "box-sizing", "padding-box", {}),
    ("bsc", "box-sizing", "content-box", {}),

    ("ma", "margin", "auto", {}),
    ("mla", "margin-left", "auto", {}),
    ("mra", "margin-right", "auto", {}),

    ("por", "position", "relative", { "alias": ["porelative", "prelative", "relative"] }),
    ("pof", "position", "fixed", { "alias": ["pofixed", "pfixed", "fixed"] }),
    ("pos", "position", "static", { "alias": ["postatic", "pstatic", "static"] }),
    ("poa", "position", "absolute", { "alias": ["poabsolute", "pabsolute", "absolute"] }),

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

    ("toe", "text-overflow", "ellipsis", { "alias": ["elip", "ellipsis", "toellipsis"] }),

    ("jcc", "justify-content", "center", {}),
    ("jcs", "justify-content", "flex-start", {}),
    ("jce", "justify-content", "flex-end", {}),

    ("ltr", "direction", "ltr", { "alias": [ "dirltr" ]}),
    ("rtl", "direction", "rtl", { "alias": [ "dirrtl" ]}),

    ("tsn", "text-shadow", "none", { "alias": [ "teshnone" ]}),
    ("tlf", "table-layout", "fixed", {}),
    ("tla", "table-layout", "auto", {}),

    ("wa", "width", "auto", { "alias": ["wauto"] }),
    ("ha", "height", "auto", { "alias": ["hauto"] }),
]

definitions = { "properties": properties_list, "statements": statements_list }
