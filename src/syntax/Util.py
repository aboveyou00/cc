

def isSubclassOfAny(obj, types):
    otype = type(obj)
    isotype = lambda base: issubclass(otype, base)
    return any(map(isotype, types))
