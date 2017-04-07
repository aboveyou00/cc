from syntax.ExprSyntax import *

class TermExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, num):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.num = num
    
    def __str__(self):
        return str(self.num)
