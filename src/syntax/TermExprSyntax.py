from syntax.ExprSyntax import *

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
    
    def __str__(self):
        if self.ident:
            if self.ident_res:
                return '<' + str(type(self.ident_res).__name__) + '::' + self.ident + '>'
            return self.ident
        return str(self.num)
