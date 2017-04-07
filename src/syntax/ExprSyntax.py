from syntax.Syntax import *

class ExprSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__(cunit, tok_start_idx, tok_count)
    
    def precendenceParens(self, other):
        if self.isHigherPrecedence(other) == False or other.isHigherPrecedence(self):
            return '(' + str(other) + ')'
        
        return str(other)
    
    def isHigherPrecedence(self, other):
        return False
