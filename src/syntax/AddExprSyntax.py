from syntax.ExprSyntax import *
from syntax.MultExprSyntax import *
from syntax.TermExprSyntax import *

class AddExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, op, rhs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    
    def isHigherPrecedence(self, other):
        return type(other) in [MultExprSyntax, TermExprSyntax]
    
    def __str__(self):
        return self.precendenceParens(self.lhs) + ' ' + self.op + ' ' + self.precendenceParens(self.rhs)
