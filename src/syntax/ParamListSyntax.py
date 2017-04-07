from syntax.Syntax import *

class ParamListSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count, params):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.params = params
    
    def registerNames(self, declspace):
        for param in self.params:
            param.registerNames(declspace)
    
    def resolveNames(self):
        for param in self.params:
            param.resolveNames()
    
    def __str__(self):
        return ', '.join(map(str, self.params))
