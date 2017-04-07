from syntax.PrimaryExprSyntax import *

class InvocationExprSyntax(PrimaryExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, args):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.args = args
    
    def __str__(self):
        return str(self.lhs) + '(' + ', '.join(map(str, self.args)) + ')'
