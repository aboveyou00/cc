from syntax.DeclSyntax import *

class FuncDeclSyntax(DeclSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, name, params, exprs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.name = name
        self.params = params
        self.exprs = exprs
    
    def __str__(self):
        sig = 'def ' + self.name + '(' + str(self.params) + ')'
        if len(self.exprs) == 1:
            return sig + ' = ' + str(self.exprs[0])
        return sig + '\n  ' + '\n  '.join(map(str, self.exprs)) + '\nend'
