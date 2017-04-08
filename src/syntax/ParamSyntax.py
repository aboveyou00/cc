from syntax.Syntax import *

class ParamSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count, name, type = None):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.name = name
        self.type = type
        self.index = None
        self.fnT = None
    
    def registerNames(self, declspace):
        declspace.register(self.name, self)
        if self.type:
            self.type.registerNames(declspace)
    
    def resolveNames(self):
        if self.type:
            self.type.resolveNames()
    
    def setFunctionT(self, fnT, i):
        self.fnT = fnT
        self.index = i
    
    def tryResolveType(self):
        return False
    
    def resolvedType(self):
        if self.fnT and not self.index is None:
            return self.fnT.getArgumentTypes()[self.index]
        return None
    
    def __str__(self):
        type = self.type or self.resolvedType() or '???'
        return self.name + ': ' + str(type)
