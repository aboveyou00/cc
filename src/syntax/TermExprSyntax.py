from syntax.ExprSyntax import *

class TermExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, val):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.num   = val if type(val) == int else None
        self.ident = val if type(val) == str else None
    
    def __str__(self):
        return str(self.num) if self.num else self.ident
