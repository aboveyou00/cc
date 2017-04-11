from syntax.Syntax import *
from emit.FunctionBuilder import *

class ParamListSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count, params):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.params = params
        self.fnT = None
    
    def registerNames(self, declspace):
        for param in self.params:
            param.registerNames(declspace)
    
    def resolveNames(self):
        for param in self.params:
            param.resolveNames()
    
    def createFunctionT(self, declspace, funcDecl):
        self.fnT = FunctionBuilder(funcDecl.name, len(self.params), funcDecl)
        overload = declspace.registerFnOverload(funcDecl.name, self.fnT)
        
        for i, param in enumerate(self.params):
            param.setFunctionT(self.fnT, i)
        
        return self.fnT
    
    def __str__(self):
        return ', '.join(map(str, self.params))
