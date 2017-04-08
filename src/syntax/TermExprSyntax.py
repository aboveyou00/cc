from syntax.ExprSyntax import *
from stdtypes.Int import *
from compilation.MethodGroup import *

class TermExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, val):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.num   = val if type(val) == int else None
        self.ident = val if type(val) == str else None
        self.ident_res = None
        self.declspace = None
    
    def registerNames(self, declspace):
        self.declspace = declspace
    
    def resolveNames(self):
        if type(self.ident) == str:
            self.ident_res = self.declspace.resolve(self.ident)
    
    def tryResolveType(self):
        if self.resolvedType():
            return False
        
        if self.ident:
            if not self.ident_res:
                return None
            
            if type(self.ident_res) == MethodGroup:
                self._resolvedType = self.ident_res
                return True
            
            changed = self.ident_res.tryResolveType()
            self._resolvedType = self.ident_res.resolvedType()
            return changed
        
        else:
            self._resolvedType = Int.inst()
            return True
    
    def __str__(self):
        if self.ident:
            return self.ident
        return str(self.num)
