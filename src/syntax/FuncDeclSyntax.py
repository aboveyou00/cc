from syntax.DeclSyntax import *

class FuncDeclSyntax(DeclSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, name, params, exprs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.name = name
        self.params = params
        self.exprs = exprs
    
    def __str__(self):
        return 'def ' + self.name + '(' + str(self.params) + ')\n  ' + '\n  '.join(map(str, self.exprs)) + '\nend'
