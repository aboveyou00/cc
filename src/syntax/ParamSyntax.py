from syntax.Syntax import *

class ParamSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count, name, type = None):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.name = name
        self.type = type
    
    def __str__(self):
        if self.type:
            return self.name + ': ' + str(self.type)
        
        return self.name
