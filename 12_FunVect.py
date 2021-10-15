def superposition(funmod, funseq):
    funcs = []
    for elem in funseq:
        def inner(arg, elem=elem):
            return funmod(elem(arg))
        funcs.append(inner)
    return funcs