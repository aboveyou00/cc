from syntax.ExprSyntax import *

class AddExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, op, rhs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    
    def __str__(self):
        return '(' + str(self.lhs) + ') ' + self.op + ' (' + str(self.rhs) + ')'
