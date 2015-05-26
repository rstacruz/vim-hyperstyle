expressions = {
        "db" : ("display", "block"),
        "di" : ("display", "inline")
}

def expand(snippet = ""):
    if snippet == 'db':
        return 'display: block;'
    return snippet
