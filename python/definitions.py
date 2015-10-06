"""
A list of CSS properties to expand.
Format:

    (property, [aliases], unit, [values])

- property : (String) the full CSS property name.
- aliases : (String list) a list of aliases for this shortcut.
- unit : (String) when defined, assumes that the property has a value with a
  unit. When the value is numberless (eg, `margin:12`), the given unit will
  be assumed (`12px`). Set this to `_` for unitless numbers (eg, line-height).
- values : (String list) possible values for this property.

Each property will be accessible through these ways:

- fuzzy matches of the aliases defined
- fuzzy matches of the property name, no dashes (eg: mi, min, minh, minhe,
  minhei...)
- fuzzy matches with dashes (eg: min-h, min-hei, min-heig...)
"""

properties = [
    ("margin", [], "px", ["auto"]),
    ("width", [], "px", ["auto"]),
    ("height", [], "px", ["auto"]),
    ("padding", [], "px", ["auto"]),
    ("border", [], None, None),
    ("outline", [], None, None),
    ("left", [], "px", None),
    ("top", [], "px", None),
    ("bottom", [], "px", None),
    ("right", [], "px", None),
    ("background", ["bground"], None, ["transparent"]),
    ("min-height", ["mheight"], "px", ["auto"]),
    ("min-width", ["mwidth"], "px", ["auto"]),
    ("max-height", ["xheight","mxheight"], "px", ["auto"]),
    ("max-width", ["xwidth","mxheight"], "px", ["auto"]),

    ("margin-left", ["mleft","marleft"], "px", ["auto"]),
    ("margin-right", ["mright","marright"], "px", ["auto"]),
    ("margin-top", ["mtop","martop"], "px", ["auto"]),
    ("margin-bottom", ["mbottom","marbottom"], "px", ["auto"]),

    ("padding-left", ["pleft","padleft"], "px", None),
    ("padding-right", ["pright","padright"], "px", None),
    ("padding-top", ["ptop","padtop"], "px", None),
    ("padding-bottom", ["pbottom","padbottom"], "px", None),

    ("z-index", [], "_", None),

    ("display", [], None, ["none", "block", "inline", "inline-block", "table", "table-cell", "table-row"]),
    ("text-align", ["talign"], None, ["left", "right", "justify", "center", "inherit"]),

    ("overflow", ["oflow"], None, ["visible", "scroll", "hidden", "auto", "inherit"]),
    ("overflow-x", ["ox"], None, ["visible", "scroll", "hidden", "auto", "inherit"]),
    ("overflow-y", ["oy"], None, ["visible", "scroll", "hidden", "auto", "inherit"]),

    ("font", [], None, None),
    ("font-size", ["fsize", "fosize"], "em", None),
    ("font-style", ["fstyle", "fostyle"], None, ["italic","normal","inherit"]),
    ("font-weight", ["fweight", "foweight"], None, ["100","200","300","400","500","600","700","800","900","bold","normal","inherit"]),
    ("font-variant", ["fvariant", "fovariant"], None, None),
    ("font-family", ["ffamily", "family"], None, None),
    ("line-height", ["lheight", "liheight"], "_", None),
    ("letter-spacing", ["lspacing", "lespacing"], "px", None),

    ("transition", ["trans", "tn", "tsition"], None, None),
    ("transform", ["tform", "xform"], None, None),
    ("text-transform", ["ttransform"], None, ["uppercase", "lowercase", "capitalize", "none", "full-width", "inherit"]),
    ("text-decoration", ["tdecoration"], None, ["underline", "none", "line-through", "overline", "inherit", "initial"]),
    ("text-decoration-line", ["tdline"], None, ["underline", "none", "line-through", "overline", "inherit", "initial"]),
    ("text-indent", ["tindent"], "px", None),
    ("text-shadow", ["tshadow", "teshadow"], None, ["none"]),
    ("table-layout", ["tlayout", "talayout"], None, ["fixed", "auto", "inherit"]),
    ("vertical-align", ["valign"], None, ["middle","top","bottom","baseline","text-top","text-bottom","sub","super"]),

    ("transition-duration", ["tduration"], "ms", None),

    ("float", [], None, ["left", "right", "none", "inherit"]),
    ("color", [], None, None),
    ("opacity", [], "_", None),

    ("border-right", ["bright", "borright"], None, None),
    ("border-left", ["bleft", "borleft"], None, None),
    ("border-top", ["btop", "bortop"], None, None),
    ("border-bottom", ["bbottom", "borbottom"], None, None),

    ("border-width", ["bwidth"], "px", None),
    ("border-right-width", ["brwidth"], "px", None),
    ("border-left-width", ["blwidth"], "px", None),
    ("border-top-width", ["btwidth"], "px", None),
    ("border-bottom-width", ["bbwidth"], "px", None),

    ("border-image", ["borimage"], None, None),

    ("cursor", [], None, ["wait", "pointer", "auto", "default", "help", "progress", "cell", "crosshair", "text", "vertical-text", "alias", "copy", "move", "not-allowed", "no-drop", "all-scroll", "col-resize", "row-resize", "n-resize", "e-resize", "s-resize", "w-resize", "nw-resize", "ne-resize", "sw-resize", "se-resize", "ew-resize", "ns-resize", "zoom-in", "zoom-out", "grab", "grabbing" ]),
    ("animation", [], None, None),

    ("background-image", ["bgimage", "backimage", "bimage"], None, None),
    ("background-color", ["bgcolor", "backcolor", "bcolor"], None, None),
    ("background-size", ["bgsize", "backsize"], None, None),
    ("background-position", ["bgposition", "backposition", "bposition"], None, ["center", "top", "left", "middle", "bottom", "right"]),
    ("background-repeat", ["bgrepeat", "backrepeat", "brepeat"], None, ["repeat-x", "repeat-y", "no-repeat"]),

    ("border-radius", ["bradius", "boradius"], "px", None),
    ("border-color", ["bcolor", "bocolor", "borcolor"], "px", None),
    ("border-collapse", ["bcollapse", "borcollapse", "collapse"], None, ["collapse","auto","inherit"]),

    ("box-shadow", ["bshadow", "boshadow"], None, ["none"]),
    ("box-sizing", ["bsizing", "bsize", "boxsize"], None, ["border-box", "content-box", "padding-box"]),

    ("position", [], None, ["absolute", "relative", "fixed", "static", "inherit"]),
    ("flex", [], None, None),
    ("white-space", ["wspace", "whispace", "whspace", "wispace"], None, ["nowrap", "normal", "pre", "pre-wrap", "pre-line", "inherit"]),

    ("visibility", [], None, ["visible", "hidden", "collapse", "inherit"]),

    ("flex-grow", ["fgrow", "flgrow", "flegrow"], "_", None),
    ("flex-shrink", ["fshrink", "flshrink", "fleshrink"], "_", None),
    ("flex-direction", ["fdirection", "fldirection", "fledirection"], None, None),
    ("flex-wrap", ["fwrap", "flwrap", "flewrap"], None, None),
    ("align-items", ["aitems", "alitems"], None, ["flex-start", "flex-end", "center", "baseline", "stretch", "inherit"]),
    ("justify-content", ["jcontent", "jucontent", "juscontent", "justcontent"], None, ["flex-start", "flex-end", "center", "space-around", "space-between", "inherit"]),
    ("order", [], "_", None),

    ("page-break-after", ["pbafter"], None, ["always", "auto", "avoid", "left", "right", "inherit"]),
    ("page-break-before", ["pbbefore"], None, ["always", "auto", "avoid", "left", "right", "inherit"]),
    ("perspective", [], None, None),
    ("perspective-origin", ["porigin"], None, None),
    ("word-break", ["wbreak"], None, []),
    ("quotes", [], None, None),
    ("content", [], None, None),
    ("clear", [], None, ["left", "right", "both", "inherit"]),
    ("zoom", [], "_", None),
    ("direction", [], None, ["ltr", "rtl", "inherit"]),

    ("list-style", ["lstyle"], None, ["none", "square", "disc", "inside", "outside", "inherit", "initial", "unset", "decimal", "georgian"]),
]

"""
A list of CSS statements to expand.

This differs from `properties` as this defines shortcuts for an entire statement.
For instance, `dib<Enter>` will expand to `display: inline-block`.

Each line is in this format:

    (property, value, alias)

The following options are available:

- alias : (String list) see `property_list` on how aliases work.
"""

statements = [
    ("display", "block", ["dblock"]),
    ("display", "inline", ["dinline"]),
    ("display", "inline-block", ["diblock"]),
    ("display", "inline-flex", ["diflex"]),
    ("display", "table", ["dtable", "table"]),
    ("display", "table-cell", ["dtcell","cell","tablecell","table-cell"]),
    ("display", "table-row", ["dtrow","row","tablerow","table-row"]),

    ("float", "left", ["fleft", "flleft", "floleft"]),
    ("float", "right", ["fright", "flright", "floright"]),
    ("float", "none", ["fnone", "flnone", "flonone"]),

    ("display", "none", ["dnone"]),
    ("display", "flex", ["dflex", "flex"]),

    ("font-weight", "normal", ["fwnormal"]),
    ("font-weight", "bold", ["fwbold", "bold"]),
    ("font-style", "italic", ["fsitalic", "italic"]),
    ("font-style", "normal", ["fnormal"]),

    ("border", "0", ["b0"]),
    ("padding", "0", ["p0","po"]),
    ("margin", "0", ["m0","mo"]),
    ("margin", "0 auto", ["m0a", "moa"]),

    ("overflow", "hidden", ["ohidden"]),
    ("overflow", "scroll", ["oscroll"]),
    ("overflow", "auto", ["oauto"]),
    ("overflow", "visible", ["ovisible"]),

    ("overflow-x", "hidden", ["oxhidden"]),
    ("overflow-x", "scroll", ["oxscroll"]),
    ("overflow-x", "auto", ["oxauto"]),
    ("overflow-x", "visible", ["oxvisible"]),

    ("overflow-y", "hidden", ["oyhidden"]),
    ("overflow-y", "scroll", ["oyscroll"]),
    ("overflow-y", "auto", ["oyauto"]),
    ("overflow-y", "visible", ["oyvisible"]),

    ("font-weight", "100", ["f100", "fw100"]),
    ("font-weight", "200", ["f200", "fw200"]),
    ("font-weight", "300", ["f300", "fw300"]),
    ("font-weight", "400", ["f400", "fw400"]),
    ("font-weight", "500", ["f500", "fw500"]),
    ("font-weight", "600", ["f600", "fw600"]),
    ("font-weight", "700", ["f700", "fw700"]),
    ("font-weight", "800", ["f800", "fw800"]),
    ("font-weight", "900", ["f900", "fw900"]),

    ("border", "0", ["b0"]),
    ("border-collapse", "collapse", ["bccollapse"]),
    ("border-collapse", "separate", ["bcseparate"]),

    ("background-repeat", "repeat-x", [ "brx", "rx", "bgrx", "repeatx" ]),
    ("background-repeat", "repeat-y", [ "bry", "ry", "bgry", "repeaty" ]),
    ("background-repeat", "no-repeat", [ "brnorepeat", "norepeat"]),

    ("background-size", "cover", ["cover"]),
    ("background-size", "contain", ["contain"]),

    ("cursor", "pointer", ["cupointer", "curpointer"]),
    ("cursor", "wait", ["cuwait", "curwait"]),
    ("cursor", "busy", ["cubusy", "curbusy"]),
    ("cursor", "text", ["cutext", "curtext"]),

    ("vertical-align", "middle", ["vamiddle"]),
    ("vertical-align", "top", ["vatop"]),
    ("vertical-align", "bottom", ["vabottom"]),
    ("vertical-align", "sub", ["vasub"]),
    ("vertical-align", "super", ["vasuper"]),
    ("vertical-align", "baseline", ["vabline", "vabaseline", "baseline"]),
    ("vertical-align", "text-top", ["vattop"]),
    ("vertical-align", "text-bottom", ["vattbottom"]),

    ("visibility", "visible", ["vvisible","visible"]),
    ("visibility", "hidden", ["vhidden", "vishidden", "vihidden", "hidden", "hide"]),
    ("visibility", "collapse", ["vcollapse", "viscollapse", "vicollapse"]),

    ("clear", "both", ["cboth"]),
    ("clear", "right", ["cright"]),
    ("clear", "left", ["cleft"]),

    ("content", "''", ["content"]),

    ("text-transform", "uppercase", ["ttupper", "uppercase"]),
    ("text-transform", "lowercase", ["ttlower"]),
    ("text-transform", "none", ["ttnone"]),
    ("text-transform", "capitalize", ["ttcap"]),
    ("text-transform", "full-width", ["ttfull"]),

    ("text-align", "left", ["taleft"]),
    ("text-align", "right", ["taright"]),
    ("text-align", "center", ["tacenter", "center"]),
    ("text-align", "justify", ["tajustify", "justify"]),

    ("text-decoration", "underline", ["tdunderline", "underline"]),
    ("text-decoration", "none", ["tdnone"]),

    ("box-sizing", "border-box", ["bsbox"]),
    ("box-sizing", "padding-box", ["bspadding"]),
    ("box-sizing", "content-box", ["bscontent"]),

    ("margin", "auto", ["mauto"]),
    ("margin-left", "auto", ["mlauto"]),
    ("margin-right", "auto", ["mrauto"]),

    ("width", "auto", ["wauto"]),
    ("height", "auto", ["hauto"]),

    ("position", "relative", ["porelative", "prelative", "relative"]),
    ("position", "fixed", ["pofixed", "pfixed", "fixed"]),
    ("position", "static", ["postatic", "pstatic", "static"]),
    ("position", "absolute", ["poabsolute", "pabsolute", "absolute"]),

    ("white-space", "nowrap", ["nowrap"]),
    ("text-overflow", "ellipsis", ["ellipsis"]),

    ("flex", "auto", ["flauto"]),

    ("align-items", "flex-start", ["aistart"]),
    ("align-items", "flex-end", ["aiend"]),
    ("align-items", "center", ["aicenter"]),
    ("align-items", "stretch", ["aistretch"]),

    ("text-overflow", "ellipsis", ["elip", "ellipsis", "toellipsis"]),

    ("flex-wrap", "wrap", ["fwrap","flexwrap"]),
    ("flex-wrap", "nowrap", ["fnowrap"]),

    ("flex-direction", "row", ["fdrow"]),
    ("flex-direction", "row-reverse", ["fdrreverse"]),
    ("flex-direction", "column", ["fdcolumn"]),
    ("flex-direction", "column-reverse", ["fdcreverse"]),

    ("justify-content", "center", ["jccenter"]),
    ("justify-content", "flex-start", ["jcstart"]),
    ("justify-content", "flex-end", ["jcend"]),

    ("direction", "ltr", ["ltr","dirltr"]),
    ("direction", "rtl", ["rtl","dirrtl"]),

    ("text-shadow", "none", ["tsnone", "teshnone"]),
    ("table-layout", "fixed", ["tlfixed"]),
    ("table-layout", "auto", ["tlauto"]),

    ("list-style", "none", ["lsnone"]),
    ("list-style-type", "none", ["lstnone"]),
]

definitions = { "properties": properties, "statements": statements }
